import random
import re
from time import sleep
from common.AutoActions import AutoActions
from common.Utils import Utils
from xiq.flows.manage.Devices import Devices
from xiq.flows.common.Navigator import Navigator
from xiq.flows.manage.Device360 import Device360
from xiq.elements.Device360WebElements import Device360WebElements
from xiq.elements.DevicesWebElements import DevicesWebElements
from common.Cli import Cli
from common.Screen import Screen

class Overview(Device360WebElements):
    def __init__(self):
        super().__init__()
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.dev = Devices()
        self.navigator = Navigator()
        self.Device360 = Device360()
        self.dev360 = Device360WebElements()
        self.devices_web_elements = DevicesWebElements()
        self.cli = Cli()
        self.screen = Screen()

    def fetch_port_detail_with_left_click(self, port):
        """
        This Keyword verifies port icon table information on device360
        :param spawn: spawn switch
        :param port: port number
        :param port_type: device port type
        :return: 1 if successful else -1
        """
        new_port = port.split("/")
        port_len = len(new_port)
        if port_len == 2:
            port = new_port[1]
        else:
            port = new_port[0]

        self.utils.print_info("**********Right click on port {} *********************".format(port))
        port_info = self.Device360.device360_left_click_on_port_icon(port)

        self.Device360.device360_refresh_page()
        self.utils.print_info("******************  D360 Port Icon Vlan Details for port {} ************************".format(port))
        for key, value in port_info.items():
            self.utils.print_info(f"{key}: {value}")

        return port_info