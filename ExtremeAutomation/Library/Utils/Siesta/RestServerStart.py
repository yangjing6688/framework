
import os
import urllib
import zipfile
import subprocess

class rest_server_start(object):
    def __init__(self):
        pass

    def wget_rest_server_and_unzip(self):
        try:
            os.mkdir("C:\Automation\RestServer")
        except:
            pass
        try:
            os.mkdir("C:\\Automation\\NetSightUtilities")
        except:
            pass

        os.chdir('C:\\Automation\\NetSightUtilities')
        urllib.urlretrieve('http://10.52.15.200/files/DEV/NetSightUtilities.zip', 'NetSightUtilities.zip')

        ns_zip_file = zipfile.ZipFile('NetSightUtilities.zip', 'r')
        ns_zip_file.extractall()
        ns_zip_file.close()
        os.chdir('..')
        os.chdir('C:\\Automation\\RestServer')

        urllib.urlretrieve('http://10.52.15.200/files/DEV/RestServer.zip', 'RestServer.zip')
        zip_file = zipfile.ZipFile('RestServer.zip', 'r')
        zip_file.extractall()
        zip_file.close()

create = rest_server_start()
create.wget_rest_server_and_unzip()