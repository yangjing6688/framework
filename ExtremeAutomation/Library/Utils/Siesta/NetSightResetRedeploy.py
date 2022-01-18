import os
import subprocess
import glob
import time
import datetime
import sys

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



start = NetsightInstall()
start.reset_netsight()
