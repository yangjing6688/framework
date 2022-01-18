from __future__ import print_function, with_statement
import setuptools
import shutil
from contextlib import closing
from distutils.command.sdist import sdist
from zipfile import ZipFile, ZIP_DEFLATED
import os
import sys
import zipfile
import tempfile
from subprocess import call

try:
    import paramiko
except ImportError:
    pass
try:
    import pymysql
except ImportError:
    pass
from setuptools.command.install import install
import os.path

# USAGE
# Build NIGHTLY = python setup.py sdist --nightly
# Build PROD = python setup.py sdist --prod

# note: mysql-python, ostinato, protobuf, python-tk are not able to be installed with pip
# sudo pip install --no-binary=protobuf protobuf
# sudo apt-get install python-tk
# mysql should be downloaded
# ostinato should be copied from \\10.52.15.70\Automation\python-ostinato-0.8\ostinato

class InstallExtremeAutomation(install):
    def run(self):
        print("Executing custom install code")
        is_windows = sys.platform.startswith('win')
        if not is_windows:
            print("Linux - install packages")
            print("uninstalling protobuf")
            call(['pip', 'uninstall', 'protobuf','-y'])
            print("Installing protobuf with option pip install --no-binary=protobuf protobuf==3.5.2")
            call(['pip', 'install', '--no-binary=protobuf', 'protobuf==3.5.2'])
            # print("Installing apt-get for python-dev, libmysqlclient-dev and python-tk")
            # call(['sudo', 'apt-get', '--yes', '--force-yes', 'install', 'python-dev', 'libmysqlclient-dev', 'python-tk'])
            print("Completed custom install")
            # installCommon = "sudo apt-get --yes --force-yes install python-dev libmysqlclient-dev"
            # print(installCommon)
            # subprocess.call(installCommon, shell=True)

        else:
            # We can install the windows only package here
            print("Windows - install packages")
            call(['pip', 'install', 'PyAutoGUI==0.9.42'])
            call(['pip', 'install', 'https://github.com/jacexh/pyautoit/archive/master.zip'])

        install.run(self)


class ExtremeAutomationGitsdist(sdist):
    user_options = sdist.user_options + [('nightly', None, "Create a NIGHTLY build"),
                                         ('dev', None, "Create a DEV build"),
                                         ('prod', None, "Create a PROD build"),
                                         ('upload', None, "upload the build to the PROD server (pypi)")]

    def initialize_options(self):
        sdist.initialize_options(self)
        self.formats = 'zip'
        # The current PROD version
        self.current_version = "1.3"
        self.nightly = None
        self.prod = None
        self.dev = None
        self.upload = None
        self.db_host = 'extreme-networks-robot-rds.ce1yriuqod5n.us-east-1.rds.amazonaws.com'
        self.db_user = 'pip_builder'
        self.db_password = 'extreme_root'
        self.db_default_database = 'trm_version_control'
        self.pypi_server_username = 'ubuntu'
        self.pypi_server_ip = '35.168.246.154'
        new_version_parts = self.current_version.split(".")
        new_nightly_minor = int(new_version_parts[1])+1
        self.nightly_version = new_version_parts[0] + "." + str(new_nightly_minor)
        self.dev_version = "0.0"

    def run(self):
        if self.nightly:
            version_parts = self.nightly_version.split(".")
            sp_args = ('ExtremeAutomationNightly', version_parts[0], version_parts[1], 'build', 0, 0, 0)
            new_build_number = self.get_new_version(sp_args)
            if new_build_number:
                suffix = '.dev%s' % new_build_number
                self.distribution.metadata.version = self.nightly_version + suffix
                print("NIGHLTY BUILD: " + self.distribution.metadata.version)

        if self.dev:
            version_parts = self.dev_version.split(".")
            sp_args = ('ExtremeAutomationDev', version_parts[0], version_parts[1], 'build', 0, 0, 0)
            new_build_number = self.get_new_version(sp_args)
            if new_build_number:
                suffix = '.userbuild%s' % new_build_number
                self.distribution.metadata.version = self.dev_version + suffix
                print("DEV BUILD: " + self.distribution.metadata.version)

        if self.prod:
            version_parts = self.current_version.split(".")
            sp_args = ('ExtremeAutomation', version_parts[0], version_parts[1], 'build', 0, 0, 0)
            new_build_number = self.get_new_version(sp_args)
            if new_build_number:
                self.distribution.metadata.version = self.current_version + "." + new_build_number
                print("PROD BUILD: " + self.distribution.metadata.version)

        self.distribution.metadata.install_requires = ""
        if os.path.isfile('requirements.txt'):
            requirement_list = [line.rstrip('\n') for line in open('requirements.txt')]
            for req in requirement_list:
                if "platform_system" in str(req):
                    continue
                else:
                    self.distribution.metadata.install_requires += "'" + req + "',"
            self.distribution.metadata.install_requires = self.distribution.metadata.install_requires[:-1]

        # Build the new pip install file
        sdist.run(self)

        zipFile = os.path.join(os.getcwd(),"dist","ExtremeAutomation-" + self.distribution.metadata.version + ".zip")
        print("Processing ZipFile:" + zipFile)

        # update the version string
        change_dict = {"version='0.0.0'":"version='" + self.distribution.metadata.version+"'",
                       "install_requires=[]":"install_requires=[" + self.distribution.metadata.install_requires + "]"}
        self.updateSetupFile(zipFile,change_dict)

        # upload
        #if self.upload:
        #    self.executeFileUpload()

        print("Completed BUILD: " + self.distribution.metadata.version)

#     def executeFileUpload(self):
#         fileName = "ExtremeAutomation-" + self.distribution.metadata.version + ".zip"
#         localpath = os.path.join(os.getcwd(),"dist", fileName)
#         print("Local Path:" + localpath)
#         remotepath = "/home/ubuntu/pypi/packages/" + fileName
#         ssh = paramiko.SSHClient()
#         is_windows = sys.platform.startswith('win')
#         if is_windows:
#             key_location = "C:\\TRM_DATA\\key\\bbilling_aws_dev_vm.pem"
#         else:
#             key_location = "/TRM_DATA/key/bbilling_aws_dev_vm.pem"
#         pkey = paramiko.RSAKey.from_private_key_file(key_location)
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
#         try:
#             print("Connecting to: " + self.pypi_server_ip + " username: " + self.pypi_server_username)
#             ssh.connect(self.pypi_server_ip,
#                         username=self.pypi_server_username,
#                         pkey=pkey)
#             print("Conneted, open sftp")
#             sftp = ssh.open_sftp()
#             print("uploading file: " + localpath + " to " + remotepath)
#             sftp.put(localpath, remotepath)
#             sftp.close()
#             ssh.close()
#         except Exception as err:
#             print(err)
#             exit()

    def updateSetupFile(self, zipname,replacement_dict):
        file_data = ""
        filename = "setup.py"
        skipDirectory = "Documentation"
        # generate a temp file
        tmpfd, tmpname = tempfile.mkstemp(dir=os.path.dirname(zipname))
        os.close(tmpfd)

        # create a temp copy of the archive without filename
        with zipfile.ZipFile(zipname, 'r') as zin:
            with zipfile.ZipFile(tmpname, 'w') as zout:
                zout.comment = zin.comment # preserve the comment
                for item in zin.infolist():
                    if skipDirectory not in item.filename:
                        if filename not in item.filename:
                            zout.writestr(item, zin.read(item.filename))
                        else:
                            print("Reading in file: " +item.filename)
                            file_data = zin.read(item.filename)

        # replace with the temp archive
        os.remove(zipname)
        os.rename(tmpname, zipname)

        # now add filename with its new data
        with zipfile.ZipFile(zipname, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
            for key, value in replacement_dict.items():
                file_data = file_data.replace(key.encode(),value.encode())
            zf.writestr(os.path.join("ExtremeAutomation-" + self.distribution.metadata.version,filename), file_data)

        # add in the __init__.py files that are required for the pip install
        tempdirpath = tempfile.mkdtemp()
        zip_ref = zipfile.ZipFile(zipname, 'r')
        zip_ref.extractall(tempdirpath)
        zip_ref.close()
        os.remove(zipname)
        self.searchDirectory(tempdirpath)
        self.zipdir(os.path.join(tempdirpath,"ExtremeAutomation-" + self.distribution.metadata.version),zipname)
        shutil.rmtree(tempdirpath)

    def zipdir(self, basedir, archivename):
        assert os.path.isdir(basedir)
        with closing(ZipFile(archivename, "w", ZIP_DEFLATED)) as z:
            for root, dirs, files in os.walk(basedir):
                # NOTE: ignore empty directories
                for fn in files:
                    absfn = os.path.join(root, fn)
                    zfn = absfn[len(basedir) + len(os.sep):]
                    z.write(absfn, zfn)

    def searchDirectory(self, dirName):
        listOfFile = os.listdir(dirName)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if os.path.isdir(fullPath):
                self.addMissingInitFile(fullPath)
                self.searchDirectory(fullPath)

    def addMissingInitFile(self,dirName):
        fileFound = False
        listOfFile = os.listdir(dirName)
        allFiles = list()
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if not os.path.isdir(fullPath):
                if "__init__.py" in fullPath:
                    fileFound = True
                    break
        if not fileFound:
            f = open(os.path.join(dirName, "__init__.py"), "w")

    def get_new_version(self, sp_args, path=os.getcwd()):
        new_build_number = None
        try:
            connection = pymysql.connect(host=self.db_host, 
                                         user=self.db_user,
                                         password=self.db_password,   
                                         database=self.db_default_database)
            cursor = connection.cursor()
            print("DB Passing: " + str(sp_args))
            status = cursor.callproc('isp_insert_build',sp_args)
            print("DB SP Status:" + str(status))
            cursor.close()
            cursor = connection.cursor()
            cursor.execute('SELECT @_isp_insert_build_5')
            print("DB after execute select")
            result_args = cursor.fetchone()
            print("DB fetch:" + str(result_args[0]))
            connection.commit()
            print("DB returned: " + str(result_args[0]))
            new_build_number = str(result_args[0])
        except Exception as err:
            print(err)
            exit()
        finally:
            print("Closing database connection")
            cursor.close()
            connection.close()
        return new_build_number


setuptools.setup(cmdclass={'sdist': ExtremeAutomationGitsdist, 'install': InstallExtremeAutomation},
                 name='ExtremeAutomation',
                 version='0.0.0',
                 description='ExtremeAutomation Framework',
                 url='http://',
                 author='elatour',
                 author_email='elatour@extremenetworks.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 zip_safe=True,
                 package_data={
                     # If any package contains *.txt or *.rst files, include them:
                     '': ['*.txt', '*.robot', '*.csv'],
                 },
                 include_package_data=True,
                 install_requires=[],
                 entry_points={"console_scripts": ["cidd = ExtremeAutomation.Utilities.DataDriven.CI_DD:main"]}
                 )

