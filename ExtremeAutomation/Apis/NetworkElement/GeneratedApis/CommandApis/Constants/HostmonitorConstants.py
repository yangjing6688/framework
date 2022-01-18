"""
This class outlines all the constants for the hostmonitor API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(HostmonitorConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class HostmonitorConstants(ApiConstants):
    def __init__(self):
        super(HostmonitorConstants, self).__init__()
        self.SHOW_CPU_10_SECOND_UTILIZATION = {"constant": "show_cpu_10_second_utilization",
                                               "tags": ["COMMAND_SNMP"],
                                               "link": self.link.show_cpu_10_second_utilization}
        self.SHOW_CPU_1_HOUR_UTILIZATION = {"constant": "show_cpu_1_hour_utilization",
                                            "tags": ["COMMAND_SNMP"],
                                            "link": self.link.show_cpu_1_hour_utilization}
        self.SHOW_CPU_1_MINUTE_UTILIZATION = {"constant": "show_cpu_1_minute_utilization",
                                              "tags": ["COMMAND_SNMP"],
                                              "link": self.link.show_cpu_1_minute_utilization}
        self.SHOW_CPU_30_MINUTE_UTILIZATION = {"constant": "show_cpu_30_minute_utilization",
                                               "tags": ["COMMAND_SNMP"],
                                               "link": self.link.show_cpu_30_minute_utilization}
        self.SHOW_CPU_30_SECOND_UTILIZATION = {"constant": "show_cpu_30_second_utilization",
                                               "tags": ["COMMAND_SNMP"],
                                               "link": self.link.show_cpu_30_second_utilization}
        self.SHOW_CPU_5_MINUTE_HI_TIME_TOTAL_UTILIZATION = {"constant": "show_cpu_5_minute_hi_time_total_utilization",
                                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                            "link": self.link.show_cpu_5_minute_hi_time_total_utilization}
        self.SHOW_CPU_5_MINUTE_TOTAL_UTILIZATION = {"constant": "show_cpu_5_minute_total_utilization",
                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                    "link": self.link.show_cpu_5_minute_total_utilization}
        self.SHOW_CPU_5_MINUTE_UTILIZATION = {"constant": "show_cpu_5_minute_utilization",
                                              "tags": ["COMMAND_SNMP"],
                                              "link": self.link.show_cpu_5_minute_utilization}
        self.SHOW_CPU_5_SECOND_UTILIZATION = {"constant": "show_cpu_5_second_utilization",
                                              "tags": ["COMMAND_SNMP"],
                                              "link": self.link.show_cpu_5_second_utilization}
        self.SHOW_CPU_CURRENT_TOTAL_UTILIZATION = {"constant": "show_cpu_current_total_utilization",
                                                   "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                   "link": self.link.show_cpu_current_total_utilization}
        self.SHOW_CPU_HIGHEST_5_MINUTE_TOTAL_UTILIZATION = {"constant": "show_cpu_highest_5_minute_total_utilization",
                                                            "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                            "link": self.link.show_cpu_highest_5_minute_total_utilization}
        self.SHOW_CPU_INTERVAL = {"constant": "show_cpu_interval",
                                  "tags": ["COMMAND_SNMP"],
                                  "link": self.link.show_cpu_interval}
        self.SHOW_CPU_MAX_UTILIZATION = {"constant": "show_cpu_max_utilization",
                                         "tags": ["COMMAND_SNMP"],
                                         "link": self.link.show_cpu_max_utilization}
        self.SHOW_CPU_PROCESS_10_SECOND_UTILIZATION = {"constant": "show_cpu_process_10_second_utilization",
                                                       "tags": ["COMMAND_SNMP"],
                                                       "link": self.link.show_cpu_process_10_second_utilization}
        self.SHOW_CPU_PROCESS_1_HOUR_UTILIZATION = {"constant": "show_cpu_process_1_hour_utilization",
                                                    "tags": ["COMMAND_SNMP"],
                                                    "link": self.link.show_cpu_process_1_hour_utilization}
        self.SHOW_CPU_PROCESS_1_MINUTE_UTILIZATION = {"constant": "show_cpu_process_1_minute_utilization",
                                                      "tags": ["COMMAND_SNMP"],
                                                      "link": self.link.show_cpu_process_1_minute_utilization}
        self.SHOW_CPU_PROCESS_30_MINUTE_UTILIZATION = {"constant": "show_cpu_process_30_minute_utilization",
                                                       "tags": ["COMMAND_SNMP"],
                                                       "link": self.link.show_cpu_process_30_minute_utilization}
        self.SHOW_CPU_PROCESS_30_SECOND_UTILIZATION = {"constant": "show_cpu_process_30_second_utilization",
                                                       "tags": ["COMMAND_SNMP"],
                                                       "link": self.link.show_cpu_process_30_second_utilization}
        self.SHOW_CPU_PROCESS_5_MINUTE_UTILIZATION = {"constant": "show_cpu_process_5_minute_utilization",
                                                      "tags": ["COMMAND_SNMP"],
                                                      "link": self.link.show_cpu_process_5_minute_utilization}
        self.SHOW_CPU_PROCESS_5_SECOND_UTILIZATION = {"constant": "show_cpu_process_5_second_utilization",
                                                      "tags": ["COMMAND_SNMP"],
                                                      "link": self.link.show_cpu_process_5_second_utilization}
        self.SHOW_CPU_PROCESS_APPLICATION_TIME = {"constant": "show_cpu_process_application_time",
                                                  "tags": ["COMMAND_SNMP"],
                                                  "link": self.link.show_cpu_process_application_time}
        self.SHOW_CPU_PROCESS_KERNEL_TIME = {"constant": "show_cpu_process_kernel_time",
                                             "tags": ["COMMAND_SNMP"],
                                             "link": self.link.show_cpu_process_kernel_time}
        self.SHOW_CPU_PROCESS_MAX_UTILIZATION = {"constant": "show_cpu_process_max_utilization",
                                                 "tags": ["COMMAND_SNMP"],
                                                 "link": self.link.show_cpu_process_max_utilization}
        self.SHOW_CPU_PROCESS_STATE = {"constant": "show_cpu_process_state",
                                       "tags": ["COMMAND_SNMP"],
                                       "link": self.link.show_cpu_process_state}
        self.SHOW_CPU_THRESHOLD = {"constant": "show_cpu_threshold",
                                   "tags": ["COMMAND_SNMP"],
                                   "link": self.link.show_cpu_threshold}
        self.SHOW_CPU_TOTAL_UTILIZATION = {"constant": "show_cpu_total_utilization",
                                           "tags": ["COMMAND_SNMP"],
                                           "link": self.link.show_cpu_total_utilization}
        self.SHOW_CURRENT_QUEUE_ENTRIES_CONSUMED = {"constant": "show_current_queue_entries_consumed",
                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                    "link": self.link.show_current_queue_entries_consumed}
        self.SHOW_EXHAUSTED_FBUFS = {"constant": "show_exhausted_fbufs",
                                     "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                     "link": self.link.show_exhausted_fbufs}
        self.SHOW_FREE_FBUF = {"constant": "show_free_fbuf",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.show_free_fbuf}
        self.SHOW_FREE_MEMORY = {"constant": "show_free_memory",
                                 "tags": ["COMMAND_SNMP"],
                                 "link": self.link.show_free_memory}
        self.SHOW_FREE_QUEUE_ENTRIES = {"constant": "show_free_queue_entries",
                                        "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                        "link": self.link.show_free_queue_entries}
        self.SHOW_FREE_TOTAL_MEMORY = {"constant": "show_free_total_memory",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_free_total_memory}
        self.SHOW_HIGHEST_QUEUE_ENTRIES_CONSUMED = {"constant": "show_highest_queue_entries_consumed",
                                                    "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                    "link": self.link.show_highest_queue_entries_consumed}
        self.SHOW_MEMORY_5_MINUTE_HI_TIME_TOTAL_UTILIZATION = {"constant": "show_memory_5_minute_hi_time_total_utilization",
                                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                               "link": self.link.show_memory_5_minute_hi_time_total_utilization}
        self.SHOW_MEMORY_5_MINUTE_TOTAL_UTILIZATION = {"constant": "show_memory_5_minute_total_utilization",
                                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                       "link": self.link.show_memory_5_minute_total_utilization}
        self.SHOW_MEMORY_HIGHEST_5_MINUTE_TOTAL_UTILIZATION = {"constant": "show_memory_highest_5_minute_total_utilization",
                                                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                               "link": self.link.show_memory_highest_5_minute_total_utilization}
        self.SHOW_MEMORY_TOTAL_UTILIZATION = {"constant": "show_memory_total_utilization",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.show_memory_total_utilization}
        self.SHOW_NET_STACK_DATA_FREE_MBUF = {"constant": "show_net_stack_data_free_mbuf",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.show_net_stack_data_free_mbuf}
        self.SHOW_NET_STACK_DATA_USED_MBUF = {"constant": "show_net_stack_data_used_mbuf",
                                              "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                              "link": self.link.show_net_stack_data_used_mbuf}
        self.SHOW_NET_STACK_SYSTEM_FREE_MBUF = {"constant": "show_net_stack_system_free_mbuf",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.show_net_stack_system_free_mbuf}
        self.SHOW_NET_STACK_SYSTEM_SOCKET_MBUF = {"constant": "show_net_stack_system_socket_mbuf",
                                                  "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                  "link": self.link.show_net_stack_system_socket_mbuf}
        self.SHOW_NET_STACK_SYSTEM_USED_MBUF = {"constant": "show_net_stack_system_used_mbuf",
                                                "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                                "link": self.link.show_net_stack_system_used_mbuf}
        self.SHOW_SLOT = {"constant": "show_slot",
                          "tags": ["COMMAND_CLI"],
                          "link": self.link.show_slot}
        self.SHOW_TOTAL_MEMORY = {"constant": "show_total_memory",
                                  "tags": ["COMMAND_SNMP"],
                                  "link": self.link.show_total_memory}
        self.SHOW_USED_FBUF = {"constant": "show_used_fbuf",
                               "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                               "link": self.link.show_used_fbuf}
        self.SHOW_USED_MEMORY_FOR_PROCESS = {"constant": "show_used_memory_for_process",
                                             "tags": ["COMMAND_SNMP"],
                                             "link": self.link.show_used_memory_for_process}
        self.SHOW_USED_SYSTEM_SERVICE_MEMORY = {"constant": "show_used_system_service_memory",
                                                "tags": ["COMMAND_SNMP"],
                                                "link": self.link.show_used_system_service_memory}
        self.SHOW_USED_TOTAL_MEMORY = {"constant": "show_used_total_memory",
                                       "tags": ["COMMAND_CLI", "COMMAND_SNMP"],
                                       "link": self.link.show_used_total_memory}
        self.SHOW_USED_USER_APPLICATION_MEMORY = {"constant": "show_used_user_application_memory",
                                                  "tags": ["COMMAND_SNMP"],
                                                  "link": self.link.show_used_user_application_memory}
