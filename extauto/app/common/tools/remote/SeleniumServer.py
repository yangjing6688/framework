import subprocess
import re
from time import sleep
import json


class SeleniumServer(object):
    def __init__(self):
        pass

    def start_hub(self, platform='Windows'):
        """
        Start the selenium grid hub
        :param platform:
        :return:
        """
        if platform == "Windows":
            cmd = 'netstat -ano'
            output = self.execute_cmd(cmd, ":4444")
            if output:
                print("Hub is running on port:{}".format(output))
                return output
            else:
                pr = subprocess.Popen("C:\\remote\\seleniumconfig\\starthub.bat", shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
                status = self.execute_cmd(cmd, ":4444")
                return status

    def start_node(self, host, platform="Windows"):
        """
        Start the selenium grid node
        :param platform:
        :param host
        :return:
        """
        if platform == "Windows":
            cmd = 'netstat -ano'
            output = self.execute_cmd(cmd, ":5556")
            if output:
                print("Node is running on port:{}".format(output))
                return output
            else:
                # Update the hub url in nodeConfig.json file
                self.update_hub_url(host)
                pr = subprocess.Popen("C:\\remote\\seleniumconfig\\startnode.bat", shell=True, stdout=subprocess.PIPE,
                                      stderr=subprocess.PIPE)
                sleep(10)
                status = self.execute_cmd(cmd, ":5556")
                return status

    @staticmethod
    def update_hub_url(ip):
        """
        Update the selenium hub url in nodeConfig.json file
        :param ip:
        :return:
        """
        with open("C:\\remote\\seleniumconfig\\nodeConfig.json", 'r') as f:
            data = json.load(f)
            if data['hub'] == 'http://' + ip + ':4444':
                return 1
            else:
                data['hub'] = 'http://' + ip + ':4444'

        with open("C:\\remote\\seleniumconfig\\nodeConfig.json", 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def execute_cmd(cmd, search_string):
        """
        Execute the command and check the search string in the command output
        :param cmd: cmd to be executed
        :param search_string:
        :return:
        """
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = None
        for line in process.stdout:
            if re.search(search_string, line.decode()):
                out = line
                break
        return out


if __name__ == "__main__":
    obj = SeleniumServer()
    obj.start_node("10.234.106.226")
