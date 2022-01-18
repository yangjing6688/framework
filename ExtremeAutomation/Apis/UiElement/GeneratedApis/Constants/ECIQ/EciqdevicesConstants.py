"""
This class outlines all the constants for the eciqdevices API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(EciqdevicesConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class EciqdevicesConstants(ApiConstants):
    def __init__(self):
        super(EciqdevicesConstants, self).__init__()
        self.DEVICES_CHECK_DEVICE_CHECKBOX = {"constant": "devices_check_device_checkbox",
                                              "tags": ["COMMAND_SELENIUM"],
                                              "link": self.link.devices_check_device_checkbox}
        self.DEVICES_CLEAR_DEVICE_SEARCH = {"constant": "devices_clear_device_search",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_clear_device_search}
        self.DEVICES_CLICK_ADD_AND_SELECT_ADVANCED_ONBOARDING = {"constant": "devices_click_add_and_select_advanced_onboarding",
                                                                 "tags": ["COMMAND_SELENIUM"],
                                                                 "link": self.link.devices_click_add_and_select_advanced_onboarding}
        self.DEVICES_CLICK_REFRESH = {"constant": "devices_click_refresh",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.devices_click_refresh}
        self.DEVICES_DELETE_DEVICE = {"constant": "devices_delete_device",
                                      "tags": ["COMMAND_SELENIUM"],
                                      "link": self.link.devices_delete_device}
        self.DEVICES_MONITOR_DIALOG_CLICK_CLOSE = {"constant": "devices_monitor_dialog_click_close",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_monitor_dialog_click_close}
        self.DEVICES_MONITOR_DIALOG_CLICK_REFRESH = {"constant": "devices_monitor_dialog_click_refresh",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_monitor_dialog_click_refresh}
        self.DEVICES_MONITOR_DIALOG_SELECT_PORT = {"constant": "devices_monitor_dialog_select_port",
                                                   "tags": ["COMMAND_SELENIUM"],
                                                   "link": self.link.devices_monitor_dialog_select_port}
        self.DEVICES_SELECT_DEVICE_BY_HOSTNAME_AND_IP = {"constant": "devices_select_device_by_hostname_and_ip",
                                                         "tags": ["COMMAND_SELENIUM"],
                                                         "link": self.link.devices_select_device_by_hostname_and_ip}
        self.DEVICES_SELECT_DEVICE_BY_HOSTNAME_AND_SERIAL_NUMBER = {"constant": "devices_select_device_by_hostname_and_serial_number",
                                                                    "tags": ["COMMAND_SELENIUM"],
                                                                    "link": self.link.devices_select_device_by_hostname_and_serial_number}
        self.DEVICES_SELECT_DEVICE_COUNT_PER_PAGE = {"constant": "devices_select_device_count_per_page",
                                                     "tags": ["COMMAND_SELENIUM"],
                                                     "link": self.link.devices_select_device_count_per_page}
        self.DEVICES_VERIFY_DEVICE_FIRMWARE = {"constant": "devices_verify_device_firmware",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_verify_device_firmware}
        self.DEVICES_VERIFY_DEVICE_IP = {"constant": "devices_verify_device_ip",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_verify_device_ip}
        self.DEVICES_VERIFY_DEVICE_IQ_AGENT_VERSION = {"constant": "devices_verify_device_iq_agent_version",
                                                       "tags": ["COMMAND_SELENIUM"],
                                                       "link": self.link.devices_verify_device_iq_agent_version}
        self.DEVICES_VERIFY_DEVICE_MAC = {"constant": "devices_verify_device_mac",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_verify_device_mac}
        self.DEVICES_VERIFY_DEVICE_MODEL = {"constant": "devices_verify_device_model",
                                            "tags": ["COMMAND_SELENIUM"],
                                            "link": self.link.devices_verify_device_model}
        self.DEVICES_VERIFY_DEVICE_SERIAL_NUMBER = {"constant": "devices_verify_device_serial_number",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_verify_device_serial_number}
        self.DEVICES_VERIFY_DEVICE_VENDOR = {"constant": "devices_verify_device_vendor",
                                             "tags": ["COMMAND_SELENIUM"],
                                             "link": self.link.devices_verify_device_vendor}
        self.DEVICES_VERIFY_PORT_LACP_STATUS = {"constant": "devices_verify_port_lacp_status",
                                                "tags": ["COMMAND_SELENIUM"],
                                                "link": self.link.devices_verify_port_lacp_status}
        self.DEVICES_VERIFY_PORT_MODE = {"constant": "devices_verify_port_mode",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_verify_port_mode}
        self.DEVICES_VERIFY_PORT_NAME = {"constant": "devices_verify_port_name",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_verify_port_name}
        self.DEVICES_VERIFY_PORT_POWER_USED = {"constant": "devices_verify_port_power_used",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_verify_port_power_used}
        self.DEVICES_VERIFY_PORT_SPEED = {"constant": "devices_verify_port_speed",
                                          "tags": ["COMMAND_SELENIUM"],
                                          "link": self.link.devices_verify_port_speed}
        self.DEVICES_VERIFY_PORT_STATUS = {"constant": "devices_verify_port_status",
                                           "tags": ["COMMAND_SELENIUM"],
                                           "link": self.link.devices_verify_port_status}
        self.DEVICES_VERIFY_PORT_TRAFFIC_RX = {"constant": "devices_verify_port_traffic_rx",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_verify_port_traffic_rx}
        self.DEVICES_VERIFY_PORT_TRAFFIC_TX = {"constant": "devices_verify_port_traffic_tx",
                                               "tags": ["COMMAND_SELENIUM"],
                                               "link": self.link.devices_verify_port_traffic_tx}
        self.DEVICES_VERIFY_PORT_TYPE = {"constant": "devices_verify_port_type",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_verify_port_type}
        self.DEVICES_VERIFY_PORT_VLAN = {"constant": "devices_verify_port_vlan",
                                         "tags": ["COMMAND_SELENIUM"],
                                         "link": self.link.devices_verify_port_vlan}
        self.DEVICES_VERIFY_SERIAL_NUMBER_DOES_NOT_EXIST = {"constant": "devices_verify_serial_number_does_not_exist",
                                                            "tags": ["COMMAND_SELENIUM"],
                                                            "link": self.link.devices_verify_serial_number_does_not_exist}
        self.DEVICES_VERIFY_SERIAL_NUMBER_EXISTS = {"constant": "devices_verify_serial_number_exists",
                                                    "tags": ["COMMAND_SELENIUM"],
                                                    "link": self.link.devices_verify_serial_number_exists}
