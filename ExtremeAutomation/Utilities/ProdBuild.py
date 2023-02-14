import subprocess
import tempfile
import os
import stat
import smtplib
import shutil
import re
import sys
from sys import argv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PIPE = subprocess.PIPE

try:
    import pymysql
except ImportError:
    print("You need to install the pymysql python library in order to do builds.\nTry the pip install command"
          " 'pip install pymysql")
    exit(-100)
try:
    import requests
except ImportError:
    print("You need to install the pymysql python library in order to do builds.\nTry the pip install command"
          " 'pip install pymysql")
    exit(-100)


class BuildProd:
    """
    init function
    """
    def __init__(self):
        self.git_branch = None
        self.git_tag = None
        self.git_repo = "git@github.extremenetworks.com:Engineering/SQA_ROBOT_AUTOMATION"
        self.prod_build_string = "ExtremeAutomation-"
        self.base_build_directory = "SQA_ROBOT_AUTOMATION"
        self.git_dir = None
        self.prod_build_number = 'unknown'
        self.db_host = 'extreme-networks-robot-rds.ce1yriuqod5n.us-east-1.rds.amazonaws.com'
        self.db_user = 'pip_builder'
        self.db_password = 'extreme_root'
        self.db_default_database = 'trm_version_control'

    def __exit(self, code):
        if self.git_dir:
            print("Removing the Temp directory: " + self.git_dir)
            for root, dirs, files in os.walk(self.git_dir, topdown=False):
                for name in files:
                    filename = os.path.join(root, name)
                    try:
                        os.chmod(filename, stat.S_IWUSR)
                    except Exception:
                        pass
                    try:
                        os.remove(filename)
                    except Exception:
                        pass
                for name in dirs:
                    try:
                        os.rmdir(os.path.join(root, name))
                    except Exception:
                        pass
            try:
                shutil.rmtree(self.git_dir, ignore_errors=True)
                os.rmdir(self.git_dir)
            except Exception:
                pass
        exit(code)

    def sendmail(self):
        try:
            email_from = "srv-qaauto@extremenetworks.com"
            email_address_to_list = ["Robot-Dev@extremenetworks.com"]
            msg = MIMEMultipart()
            msg['Subject'] = 'PROD ExtremeAutomation BUILD Detected'
            msg['From'] = email_from
            msg['To'] = ', '.join(email_address_to_list)
            html = """\
                <html>
                  <head>
                    <title>PROD ExtremeAutomation BUILD Detected</title>
                  </head>
                  <body>
                    <h2>PROD ExtremeAutomation BUILD Detected</h2><br>
                    <p>
                       &emsp;&emsp;<b>Git_tag:</b> """ + self.git_tag + """<br>
                       &emsp;&emsp;<b>Git_branch:</b> """ + self.git_branch + """<br>
                       &emsp;&emsp;<b>PIP Release:</b> """ + self.prod_build_number + """<br><br>
                       Thanks<br><br>
                       &emsp;&emsp;-The Build Team<br>
                    </p>
                  </body>
                </html>
            """
            msg.attach(MIMEText(html, 'html'))
            s = smtplib.SMTP('smtp.extremenetworks.com')
            print("Sending email about release")
            s.sendmail(email_from, email_address_to_list, msg.as_string())
            s.quit()
        except Exception:
            print("Error: unable to send email")
            self.__exit(-8)

    def build(self):
        # make sure we have the correct key in place \\10.52.15.70\Automation\Robot\prodkey
        keyname = os.sep + "TRM_DATA" + os.sep + "key" + os.sep + "bbilling_aws_dev_vm.pem"
        if not os.path.isfile(keyname):
            print("SSH key is missing from " + keyname + r". Please download it from: 10.52.15.70\Automation\Robot"
                                                         r"\prodkey and copy it to: " + keyname)
            self.__exit(-20)

        self.__gitsetup()
        if self.git_dir:
            print("Build ExtremeAutomation image")
            git_working_dir = self.git_dir + os.sep + self.base_build_directory
            # python setup.py sdist --prod --upload
            process = subprocess.Popen(['python', 'setup.py', 'sdist', '--prod', '--upload'], stdout=PIPE,
                                       stderr=PIPE, cwd=git_working_dir)
            stdoutput, stderroutput = process.communicate()
            if str(stdoutput).find(self.prod_build_string) != -1:
                # Grab the pip version string
                items = re.findall(self.prod_build_string + ".*$", str(stdoutput), re.MULTILINE)
                for prod_version in items:
                    print(prod_version)
                    test_version = prod_version.split("-")[1]
                    self.prod_build_number = test_version.split("\\r\\n")[0]
                    break
                if self.prod_build_number != "unknown":
                    print(self.prod_build_number)
                    try:
                        data_found = None
                        print("Connecting to database")
                        connection = pymysql.connect(self.db_host, self.db_user, self.db_password,
                                                     self.db_default_database)
                        cursor = connection.cursor()
                        # Check to see if the entry is already in the database
                        print("Checking for git_tag")
                        query = "SELECT * from robot.git_tag_pip_build where git_tag='" + self.git_tag + "'"
                        cursor.execute(query)
                        for (id, git_tag, pip_build) in cursor:
                            data_found = id
                        cursor.close()
                        if data_found:
                            print("DB Git tag found!: " + self.git_tag + ", updating it with new build")
                            # update the current record
                            query = "UPDATE robot.git_tag_pip_build set pip_build='" + self.prod_build_number + \
                                    "' where id=" + str(data_found)
                            print(query)
                            cursor = connection.cursor()
                            cursor.execute(query)
                            connection.commit()
                            cursor.close()
                        else:
                            print("DB Git tag not found: " + self.git_tag + ", creating new build")
                            # update the current record
                            query = "INSERT INTO robot.git_tag_pip_build (pip_build,git_tag) VALUES ('" + \
                                    self.prod_build_number + "','" + self.git_tag + "')"
                            print(query)
                            cursor = connection.cursor()
                            cursor.execute(query)
                            connection.commit()
                            cursor.close()
                    except Exception as err:
                        print(err)
                        self.__exit(-10)
                    else:
                        connection.close()

        else:
            print("Error: unable to create GIT setup... exit")
            self.__exit(-1)
        print("Completed build")

    def test_tracker_access(self, test_browser_url, test_browser_user, test_browser_password):
        try:
            r = requests.get(test_browser_url + '/' + 'cgi/trackerReport.pl', data={},
                             auth=(test_browser_user, test_browser_password), verify=False)
        except Exception as e:
            print(e)
            raise ValueError(
                "Authentication with " + test_browser_url + " Failed. user='" + test_browser_user + "' pass='" +
                test_browser_password + "'")
            return True

        return r.status_code != 200

    def add_build(self, product_id, build_name, release_name, build_date=None):

        # Variables used to add a new build
        browser_action = "saveNewBuild"
        browser_push_bugs = "Yes"
        browser_product_id = product_id
        browser_build_name = build_name
        browser_release_name = release_name
        browser_no_browser = 1
        browser_build_date = build_date if build_date is not None else None

        # Server Settings for authentication and URL
        browser_url = "https://tracker.extremenetworks.com:8001"
        browser_user = "tracker";  ################ PUT YOUR (GENERIC) USER NAME HERE
        browser_password = "tracker";  ################ PUT YOUR (GENERIC) PASSWORD HERE

        # Test Tracker Access
        test_access = self.test_tracker_access(browser_url, browser_user, browser_password)
        if test_access:
            print("ERROR: Tracker access failed, possible URL, User or Password problem.\n")
            sys.exit(1)

        # Populate the fields that will be passed to the web page
        post_fields = {}
        post_fields['action'] = browser_action
        post_fields['pushBugs'] = browser_push_bugs
        post_fields['productId'] = browser_product_id
        post_fields['buildName'] = browser_build_name
        post_fields['releaseName'] = browser_release_name
        post_fields['noBrowser'] = browser_no_browser

        # Add buildDate only if it was provided
        post_fields['buildDate'] = browser_build_date if browser_build_date is not None else browser_build_date;

        # Launch the webpage
        try:
            response = requests.post(browser_url + '/' + 'cgi/productReport.pl', data=post_fields,
                                     auth=(browser_user, browser_password), verify=False)
        except Exception as e:
            print(e)
            raise ValueError(
                "Authentication with " + browser_url + " Failed. user='" + browser_user
                + "' pass='" + browser_password + "'")

        is_success = response.status_code == 200
        return_text = response.text

        # Print the results:  OK means the entry was added to the bug
        if is_success:
            if "OK" in return_text:
                print("Received Reply: " + return_text)
                print("\n\n\'" + browser_build_name + "\' has been added to Tracker\n\n")
                return True
            else:
                print("Warning: Unknown return value from addBuild.py ....verify addBuild.py succeeded.")
                print("Received Reply: " + return_text)

        print("\n\nERROR - Could not add build\n----------------------\n\n")
        return False

    def cleanup(self):
        self.__exit(1)

    def __gitsetup(self):
        self.git_dir = tempfile.mkdtemp()
        print("Created temp directory: " + self.git_dir)

        # GIT clone
        print("Sending Git Clone")
        process = subprocess.Popen(['git', 'clone', self.git_repo], stdout=PIPE, stderr=PIPE, cwd=self.git_dir)
        stdoutput, stderroutput = process.communicate()
        print(str(stderroutput))
        if str(stderroutput).find("fatal:") != -1:
            print("GIT Error detected... exit")
            self.__exit(-2)

        git_working_dir = self.git_dir + os.sep + self.base_build_directory
        print(git_working_dir)

        # GIT checkout git checkout branch
        if self.git_branch and self.git_tag:
            print("Sending Git checkout branch")
            process = subprocess.Popen(['git', 'reset', '--hard', 'origin/' + self.git_branch], stdout=PIPE,
                                       stderr=PIPE, cwd=git_working_dir)
            stdoutput, stderroutput = process.communicate()
            print(str(stderroutput))
            if str(stderroutput).find("fatal:") != -1:
                print("GIT Error detected, is the branch name correct?... exit")
                self.__exit(-3)

            # GIT fetch tags git fetch --all --tags --prune
            print("Sending Git fetch tags")
            process = subprocess.Popen(['git', 'fetch', '--all', '--tags', '--prune'], stdout=PIPE, stderr=PIPE,
                                       cwd=git_working_dir)
            stdoutput, stderroutput = process.communicate()
            print(str(stderroutput))
            if str(stderroutput).find("fatal:") != -1:
                print("GIT Error detected... exit")
                self.__exit(-4)

            print("Sending Git checkout tag")
            process = subprocess.Popen(['git', 'checkout', 'tags/' + self.git_tag], stdout=PIPE, stderr=PIPE,
                                       cwd=git_working_dir)
            stdoutput, stderroutput = process.communicate()
            print(str(stderroutput))
            if str(stderroutput).find("fatal:") != -1 or str(stderroutput).find("error:") != -1:
                print("GIT Error detected, is the tag name correct?... exit")
                self.__exit(-6)
        else:
            print("GIT Branch [" + self.git_branch + "] or Tag [" + self.git_tag + "] [ were not provided... exit")
            self.__exit(-7)

    def parse_arguments(self, arg_v):
        app_args = self.__getopts(arg_v)
        if '-h' in app_args:
            self.print_help()
            exit()
        if '-b' in app_args:
            print("GIT Branch: " + app_args['-b'])
            self.git_branch = app_args['-b']
        if '-t' in app_args:
            print("GIT Tag: " + app_args['-t'])
            self.git_tag = app_args['-t']

    @staticmethod
    def __getopts(arg_v):
        opts = {}
        while arg_v:
            if arg_v[0][0] == '-':
                opts[arg_v[0]] = arg_v[1]
            arg_v = arg_v[1:]
        return opts

    @staticmethod
    def print_help():
        print("This script will allow users to build a PROD version of the ExtremeAutomation library using a"
              " GIT branch and tag.")
        print("Once this is built, the TRMClient.jar will accept the GIT tag for the library version. This means "
              "that users can")
        print("build a PROD version on their own PROD branch and use that version in their PROD tests.")
        print("-b <git branch>")
        print("-t <git tag>")
        print("-h help")


if __name__ == '__main__':
    prod = BuildProd()
    prod.parse_arguments(argv)
    prod.build()
    prod.sendmail()
    prod.cleanup()
    print("Completed Build")
