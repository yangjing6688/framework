import os
import shutil
import sys
from paramiko import SSHClient
import paramiko
import platform
import time


class CopyLog(object):
    def __init__(self):
        pass

    def copy_xmc_log(self, guid, test_engine_ip, test_engine_username, test_engine_pw, log_name):
        sys.stdout.write("Copying Netsight Log...\n")
        log_source = r"C:/Program Files/Extreme Networks/NetSight/appdata/logs/"

        if guid == 'abcd':
            dest_path = r"C:/Automation/xmc_server_logs/"
            if "windows" in platform.platform().lower():
                self.if_windows(dest_path, log_source, log_name)
            else:
                dest_path = r"TRM_DATA/logs/xmc_server_logs"
                self.if_linux(dest_path, dest_path, log_source, log_name, test_engine_ip, test_engine_username,
                              test_engine_pw)
        else:
            guid_path = "/TRM_DATA/logs/" + guid
            dest_path = guid_path + "/xmc_server_logs/"
            self.if_linux(guid_path, dest_path, log_source, log_name, test_engine_ip, test_engine_username,
                          test_engine_pw)

    def if_windows(self, dest_path, log_source, log_name):
        if not os.path.isdir(dest_path) and not os.path.isfile(dest_path):
            os.mkdir(dest_path)
        contents = os.listdir(log_source)
        for filename in contents:
            if log_name in filename:
                shutil.copy(log_source + filename, dest_path + filename)

    def if_linux(self, guid_path, dest_path, log_source, log_name, test_engine_ip, test_engine_username,
                 test_engine_pw):
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(test_engine_ip, username=test_engine_username, password=test_engine_pw)
        sftp_client = ssh.open_sftp()
        ssh.exec_command('sudo chmod -R 777 ' + guid_path)
        time.sleep(1)
        try:
            sftp_client.mkdir(dest_path)
            ssh.exec_command('sudo chmod -R 777 ' + dest_path)
        except IOError:
            pass
        print("CONNECTED.... OPEN SFTP\n")

        contents = os.listdir(log_source)
        for filename in contents:
            if log_name in filename:
                print("Uploading File: " + log_source + filename + "\n")
                print("TO: " + dest_path + filename + "\n")
                source = os.path.join(log_source, filename)
                dest = os.path.join(dest_path, filename)
                sftp_client.put(source, dest)
        sftp_client.close()
        ssh.close()


start = CopyLog()
start.copy_xmc_log(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
