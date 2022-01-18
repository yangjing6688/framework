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
        self.CHECK_CPU_5_MINUTE_TOTAL_UTILIZATION = {"constant": "check_cpu_5_minute_total_utilization",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_cpu_5_minute_total_utilization}
        self.CHECK_CPU_5_MINUTE_UTILIZATION = {"constant": "check_cpu_5_minute_utilization",
                                               "tags": ["PARSE_SNMP"],
                                               "link": self.link.check_cpu_5_minute_utilization}
        self.CHECK_CPU_CURRENT_TOTAL_UTILIZATION = {"constant": "check_cpu_current_total_utilization",
                                                    "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                    "link": self.link.check_cpu_current_total_utilization}
        self.CHECK_CPU_HIGHEST_5_MINUTE_TOTAL_UTILIZATION = {"constant": "check_cpu_highest_5_minute_total_utilization",
                                                             "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                             "link": self.link.check_cpu_highest_5_minute_total_utilization}
        self.CHECK_CPU_MAX_UTILIZATION = {"constant": "check_cpu_max_utilization",
                                          "tags": ["PARSE_SNMP"],
                                          "link": self.link.check_cpu_max_utilization}
        self.CHECK_CPU_MONITOR_INTERVAL = {"constant": "check_cpu_monitor_interval",
                                           "tags": ["PARSE_SNMP"],
                                           "link": self.link.check_cpu_monitor_interval}
        self.CHECK_CPU_PROCESS_5_MINUTE_UTILIZATION = {"constant": "check_cpu_process_5_minute_utilization",
                                                       "tags": ["PARSE_SNMP"],
                                                       "link": self.link.check_cpu_process_5_minute_utilization}
        self.CHECK_CPU_PROCESS_APPLICATION_TIME = {"constant": "check_cpu_process_application_time",
                                                   "tags": ["PARSE_SNMP"],
                                                   "link": self.link.check_cpu_process_application_time}
        self.CHECK_CPU_PROCESS_KERNEL_TIME = {"constant": "check_cpu_process_kernel_time",
                                              "tags": ["PARSE_SNMP"],
                                              "link": self.link.check_cpu_process_kernel_time}
        self.CHECK_CPU_PROCESS_MAX_UTILIZATION = {"constant": "check_cpu_process_max_utilization",
                                                  "tags": ["PARSE_SNMP"],
                                                  "link": self.link.check_cpu_process_max_utilization}
        self.CHECK_CPU_PROCESS_STATE = {"constant": "check_cpu_process_state",
                                        "tags": ["PARSE_SNMP"],
                                        "link": self.link.check_cpu_process_state}
        self.CHECK_CPU_THRESHOLD = {"constant": "check_cpu_threshold",
                                    "tags": ["PARSE_SNMP"],
                                    "link": self.link.check_cpu_threshold}
        self.CHECK_CPU_TOTAL_UTILIZATION = {"constant": "check_cpu_total_utilization",
                                            "tags": ["PARSE_SNMP"],
                                            "link": self.link.check_cpu_total_utilization}
        self.CHECK_CURRENT_QUEUE_ENTRIES_CONSUMED = {"constant": "check_current_queue_entries_consumed",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_current_queue_entries_consumed}
        self.CHECK_EXHAUSTED_FBUFS = {"constant": "check_exhausted_fbufs",
                                      "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                      "link": self.link.check_exhausted_fbufs}
        self.CHECK_FREE_FBUF = {"constant": "check_free_fbuf",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.check_free_fbuf}
        self.CHECK_FREE_MEMORY = {"constant": "check_free_memory",
                                  "tags": ["PARSE_SNMP"],
                                  "link": self.link.check_free_memory}
        self.CHECK_FREE_QUEUE_ENTRIES = {"constant": "check_free_queue_entries",
                                         "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                         "link": self.link.check_free_queue_entries}
        self.CHECK_FREE_TOTAL_MEMORY = {"constant": "check_free_total_memory",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_free_total_memory}
        self.CHECK_HIGHEST_QUEUE_ENTRIES_CONSUMED = {"constant": "check_highest_queue_entries_consumed",
                                                     "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                     "link": self.link.check_highest_queue_entries_consumed}
        self.CHECK_MEMORY_5_MINUTE_TOTAL_UTILIZATION = {"constant": "check_memory_5_minute_total_utilization",
                                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                        "link": self.link.check_memory_5_minute_total_utilization}
        self.CHECK_MEMORY_HIGHEST_5_MINUTE_TOTAL_UTILIZATION = {"constant": "check_memory_highest_5_minute_total_utilization",
                                                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                                "link": self.link.check_memory_highest_5_minute_total_utilization}
        self.CHECK_MEMORY_TOTAL_UTILIZATION = {"constant": "check_memory_total_utilization",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_memory_total_utilization}
        self.CHECK_NET_STACK_DATA_FREE_MBUF = {"constant": "check_net_stack_data_free_mbuf",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_net_stack_data_free_mbuf}
        self.CHECK_NET_STACK_DATA_USED_MBUF = {"constant": "check_net_stack_data_used_mbuf",
                                               "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                               "link": self.link.check_net_stack_data_used_mbuf}
        self.CHECK_NET_STACK_SYSTEM_FREE_MBUF = {"constant": "check_net_stack_system_free_mbuf",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_net_stack_system_free_mbuf}
        self.CHECK_NET_STACK_SYSTEM_SOCKET_MBUF = {"constant": "check_net_stack_system_socket_mbuf",
                                                   "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                   "link": self.link.check_net_stack_system_socket_mbuf}
        self.CHECK_NET_STACK_SYSTEM_USED_MBUF = {"constant": "check_net_stack_system_used_mbuf",
                                                 "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                                 "link": self.link.check_net_stack_system_used_mbuf}
        self.CHECK_SLOT_OPERATIONAL = {"constant": "check_slot_operational",
                                       "tags": ["PARSE_CLI"],
                                       "link": self.link.check_slot_operational}
        self.CHECK_TOTAL_MEMORY = {"constant": "check_total_memory",
                                   "tags": ["PARSE_SNMP"],
                                   "link": self.link.check_total_memory}
        self.CHECK_USED_FBUF = {"constant": "check_used_fbuf",
                                "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                "link": self.link.check_used_fbuf}
        self.CHECK_USED_MEMORY_FOR_PROCESS = {"constant": "check_used_memory_for_process",
                                              "tags": ["PARSE_SNMP"],
                                              "link": self.link.check_used_memory_for_process}
        self.CHECK_USED_SYSTEM_SERVICE_MEMORY = {"constant": "check_used_system_service_memory",
                                                 "tags": ["PARSE_SNMP"],
                                                 "link": self.link.check_used_system_service_memory}
        self.CHECK_USED_TOTAL_MEMORY = {"constant": "check_used_total_memory",
                                        "tags": ["PARSE_CLI", "PARSE_SNMP"],
                                        "link": self.link.check_used_total_memory}
        self.CHECK_USED_USER_APPLICATION_MEMORY = {"constant": "check_used_user_application_memory",
                                                   "tags": ["PARSE_SNMP"],
                                                   "link": self.link.check_used_user_application_memory}
