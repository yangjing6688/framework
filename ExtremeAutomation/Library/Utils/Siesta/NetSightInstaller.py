import os
import urllib
import subprocess
import glob
import time
import datetime
import sys
import requests
import re


class NetsightInstall(object):
    def __init__(self):
        pass

    def reset_netsight(self):
        sys.stdout.write("Resetting Netsight..." + '\n')
        subprocess.call('net stop "NetSight Server Service"')
        time.sleep(90)
        subprocess.call('net start "NetSight Server Service"')
        # take time stamp
        # view netsight log and look for started after timestamp time
        time.sleep(180)
        self.validate_netsight_is_running()
        sys.stdout.write("NetSight Server is ready for Testing..." + '\n')
        time.sleep(10)

    @staticmethod
    def validate_netsight_is_running():
        directory = max(glob.glob('C:\\Program Files\\Extreme Networks\\NetSight\\wildfly\\standalone\\tmp\\vfs\\temp'),
                        key=os.path.getmtime)
        path_time = os.path.getmtime(directory)
        os.chdir('C:\\Program Files\\Extreme Networks\\NetSight\\appdata\\logs')
        found_deployed = False
        found_admin_console = False
        time_end = time.time() + 60 * 30

        while time.time() < time_end and not found_deployed and not found_admin_console:
            if found_admin_console and found_deployed:
                break
            sys.stdout.write("Validating Netsight is running..." + '\n')
            new_first = 0
            ts_sec = 0
            time.sleep(5)
            file_item = open('server.log', 'r')
            file_lines = file_item.readlines()
            file_item.close()
            for line in file_lines:
                new_list = line.split(',')
                sys.stdout.write("Searching Server log..." + '\n')
                try:
                    pt = datetime.datetime.strptime(new_list[0], '%Y-%m-%d %H:%M:%S')
                    ts_sec = time.mktime(pt.timetuple())
                except:
                    pass
                if ts_sec - path_time > 0:
                    if 'Deployed "Connect.ear" (runtime-name : "Connect.ear")' in line:
                        found_deployed = True
                    elif 'Http management interface listening on http://127.0.0.1:9990/management' in line:
                        found_admin_console = True
                    elif found_deployed is True and found_admin_console is False or found_deployed is False and \
                            found_admin_console is True:
                        found_deployed = False
                        found_admin_console = False
                        new_first += 1
                    elif found_deployed is True and found_admin_console is True:
                        break
                    else:
                        pass
                elif new_first > file_lines.__len__():
                    break
                elif found_deployed is True and found_admin_console is True:
                    break
                else:
                    new_first += 1

    @staticmethod
    def download_netsight(version):
        sys.stdout.write("Getting XMC executable" + '\n')
        # accomodates for install with .x at the end such as 8.2.1.x to grab the latest version
        if version[-1] == 'x':
            version = version[:-1]
            branch = version
            version = version.replace('.', '\.')
            response = requests.get('http://nsbuild-linux/release/netsightweb/ns_console/Console/')
            m = re.findall('NETSIGHT_Suite_' + version + '\d+', response.content)
            ver_list = []
            for item in m:
                item = item.replace('NETSIGHT_Suite_', '')
                item = item.replace(branch, '')
                ver_list.append(int(item))
            ver_list.sort()
            version = branch + str(ver_list[-1])            
        os.chdir("C:/Automation/")
        executable_name = "ExtremeManagementCenter_Suite_" + version + "_64bit_install.exe"
        response_url = "http://nsbuild-linux/release/netsightweb/ns_console/Console/NETSIGHT_Suite_" + \
                       version + "/NetSight/"
        sz_url = "http://nsbuild-linux/release/netsightweb/ns_console/Console/NETSIGHT_Suite_" \
                 + version + "/NetSight/" + executable_name
        sys.stdout.write("Version:" + executable_name + '\n')
        attempts = 0
        max_attempts = 5
        while attempts < max_attempts:
            response = requests.get(response_url)
            if response.status_code == 404:
                attempts += 1
                time.sleep(2)
                sys.stdout.write("404 Error. Trying again..." + '\n')
            else:
                sys.stdout.write("Downloading Netsight..." + '\n')
                urllib.urlretrieve(sz_url, executable_name)
                size = os.path.getsize(executable_name)
                if size < 900000:
                    sys.stderr.write("ERROR DOWNLOADING EXECUTABLE" + "\n")
                else:
                    time.sleep(5)
                    sys.stdout.write("Netsight Downloaded Properly..." + '\n')
                    return executable_name

    @staticmethod
    def install_netsight_license():
        sys.stdout.write("Installing Netsight License..." + '\n')
        license = "0001:NETSIGHTEVAL:0:5b1e82c0:205:Extreme Networks-Engineering-INTERNAL USE ONLY-Exp. " \
                  "02JAN19:0:00000000:VpHiTnn1JmddMOSOqqG/hDgHKpGPUX9O+Z3hvHZjdrIGfTqaIHcujUGVf+HUljuGLLqDok/" \
                  "ixLLFcme6dnJv0Q=="
        path = "C:/Program Files/Extreme Networks/NetSight/appdata/license"
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + "/NetSightEval.lic", "w") as f:
            f.write(license)
            f.close()
            sys.stdout.write("Netsight License Applied..." + '\n')

    @staticmethod
    def install_netsight(executable_name):
        sys.stdout.write("Installing Netsight..." + "\n")
        path = "C:/Automation/" + executable_name + " --silent -Djava.awt.headless=true"
        sys.stdout.write("Version:" + executable_name + "\n")
        subprocess.check_output(path)
        sys.stdout.write("NetSight Installed" + "\n")


# start = NetsightInstall()
# #executable = start.download_netsight(sys.argv[1])
# start.install_netsight(executable)
# start.install_netsight_license()
# start.reset_netsight()
