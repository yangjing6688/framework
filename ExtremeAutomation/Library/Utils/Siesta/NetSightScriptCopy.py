import sys
import ftplib
import os


class NetsightInstall(object):
    def __init__(self):
        pass

    @staticmethod
    def copy_script(server_ip, script_directory, script_name, username, password):
        scripts_dir = r"C:/Program Files/Extreme Networks/NetSight/appdata/scripting/overrides/"
        sys.stdout.write("Copying Netsight Script..." + script_name + '\n')
        sys.stdout.write("To:" + scripts_dir + '\n')
        os.chdir(scripts_dir)
        ftp = ftplib.FTP(server_ip)
        ftp.login(username, password)
        ftp.cwd(script_directory)
        localfile = open(script_name, "wb")
        ftp.retrbinary("RETR " + script_name, localfile.write, 1024)
        sys.stdout.write("FTP Transfer complete..." + '\n')


start = NetsightInstall()
start.copy_script(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
