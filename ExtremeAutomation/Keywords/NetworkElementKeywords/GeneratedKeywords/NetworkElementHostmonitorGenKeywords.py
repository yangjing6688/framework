"""
Keyword class for all hostmonitor cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.HostmonitorConstants import \
    HostmonitorConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.HostmonitorConstants import \
    HostmonitorConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.
from ExtremeAutomation.Keywords.NetworkElementKeywords.Utils.NetworkElementSnmpUtils \
    import NetworkElementSnmpUtils as SnmpUtils
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils


class NetworkElementHostmonitorGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementHostmonitorGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "hostmonitor"

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def hostmonitor_verify_cpu_monitor_interval(self, device_name, interval='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [interval]     - The interval in seconds which is being verified.

        Verifies Cpu monitoring interval in seconds. Can not be smaller than 5 seconds.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"interval": interval}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_INTERVAL,
                                           self.parse_const.CHECK_CPU_MONITOR_INTERVAL, True,
                                           "CPU interval {interval}  is correct.",
                                           "CPU interval {interval}  is NOT correct!",
                                           **kwargs)

    def hostmonitor_verify_cpu_total_utilization(self, device_name, percentage='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [percent]      - The percentage which is being verified.
        [operator]     -  The operator (>, <, or =) to be used along with the interval argument.
        If nothing is specified (=) will be used.

        Verifies Total CPU utilization (percentage) as of last sampling/
        percentage of CPU utilization under current operating conditions.
        Note:  Currently this is both EXOS proprietary specific.
        """
        args = {"percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_CPU_TOTAL_UTILIZATION, True,
                                           "CPU percent current utilization is {operator} {percentage}.",
                                           "CPU percent current utilization is NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_threshold(self, device_name, threshold='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [threshold]    - The threshold in percentage which is being verified.

        Verifies Threshold for CPU Aggregation utilization trap.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"threshold": threshold}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_THRESHOLD,
                                           self.parse_const.CHECK_CPU_THRESHOLD, True,
                                           "CPU threshold {threshold} is correct.",
                                           "CPU threshold {threshold} is NOT correct.",
                                           **kwargs)

    def hostmonitor_verify_cpu_5_minute_system_utilization(self, device_name, slot='', percentage='', operator="=",
                                                           **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies The CPU utilization by set of system resources. This is the utilization of the process
        in the last 5 minutes.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_5_MINUTE_UTILIZATION,
                                           self.parse_const.CHECK_CPU_5_MINUTE_UTILIZATION, True,
                                           "Slot {slot} 5 minute CPU system utilization is"
                                           " {operator} {percentage}.",
                                           "Slot {slot} 5 minute CPU system utilization is"
                                           " NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_max_system_utilization(self, device_name, slot='', percentage='', operator="=",
                                                      **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the maximum CPU utilization of the system since the start of runtime.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_MAX_UTILIZATION,
                                           self.parse_const.CHECK_CPU_MAX_UTILIZATION, True,
                                           "Slot {slot} max CPU system utilization is {operator} {percentage}.",
                                           "Slot {slot} max CPU system utilization is"
                                           " NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_free_system_memory(self, device_name, slot='', k_bytes='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [k_bytes]      -  The value of Kilobytes to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the total amount of free memory in Kbytes in the system.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "k_bytes": k_bytes,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FREE_MEMORY,
                                           self.parse_const.CHECK_FREE_MEMORY, True,
                                           "Slot {slot} free system memory is {operator} {k_bytes}.",
                                           "Slot {slot} free system memory is NOT {operator} {k_bytes}!",
                                           **kwargs)

    def hostmonitor_verify_used_system_service_memory(self, device_name, slot='', k_bytes='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [k_bytes]      -  The value of Kilobytes to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the total amount of memory used by all system services in Kilobytes in the system.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "k_bytes": k_bytes,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USED_SYSTEM_SERVICE_MEMORY,
                                           self.parse_const.CHECK_USED_SYSTEM_SERVICE_MEMORY, True,
                                           "Slot {slot} used system service memory is {operator} {k_bytes}.",
                                           "Slot {slot} used system service memory is NOT {operator} {k_bytes}!",
                                           **kwargs)

    def hostmonitor_verify_used_application_memory(self, device_name, slot='', k_bytes='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [k_bytes]      -  The value of Kilobytes to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.
        Verifies the total amount of memory used by all applications in Kilobytes in the system.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "k_bytes": k_bytes,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USED_USER_APPLICATION_MEMORY,
                                           self.parse_const.CHECK_USED_USER_APPLICATION_MEMORY, True,
                                           "Slot {slot} used user application memory is"
                                           " {operator} {k_bytes}.",
                                           "Slot {slot} used user application memory is"
                                           " NOT {operator} {k_bytes}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_current_total_utilization(self, device_name, slot='', percentage='', operator="=",
                                                         **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the percentage CPU utilization under current operating conditions.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_CURRENT_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_CPU_CURRENT_TOTAL_UTILIZATION, True,
                                           "Current cpu total utilization on slot {slot} is"
                                           " {operator} {percentage}.",
                                           "Current  cpu total utilization on slot {slot} is"
                                           " NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_5_minute_total_utilization(self, device_name, slot='', percentage='', operator="=",
                                                          **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies average percentage CPU utilization over the past 5 minutes.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_5_MINUTE_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_CPU_5_MINUTE_TOTAL_UTILIZATION, True,
                                           "5 minute cpu total utilization on slot {slot} is"
                                           " {operator} {percentage}.",
                                           "5 minute cpu total utilization on slot {slot} is"
                                           " NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_5_minute_highest_total_utilization(self, device_name, slot='', percentage='',
                                                                  operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies Hi watermark for percentage CPU utilization over the past 5 minutes.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_CPU_HIGHEST_5_MINUTE_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_CPU_HIGHEST_5_MINUTE_TOTAL_UTILIZATION, True,
                                           "5 minute highest cpu total utilization on slot {slot}"
                                           " is {operator} {percentage}.",
                                           "5 minute highest cpu total utilization on slot {slot}"
                                           " is NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_free_total_memory(self, device_name, slot='', k_bytes='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [k_bytes]     -  The number of KBytes to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the amount of DRAM memory available in KB.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "k_bytes": k_bytes,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FREE_TOTAL_MEMORY,
                                           self.parse_const.CHECK_FREE_TOTAL_MEMORY, True,
                                           "Free total memory on slot {slot} is {operator} {k_bytes}.",
                                           "Free total memory on slot {slot} is NOT {operator} {k_bytes}!",
                                           **kwargs)

    def hostmonitor_verify_used_total_memory(self, device_name, slot='', k_bytes='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [k_bytes]     -  The number of KBytes to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies The amount of DRAM memory consumed in KB.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "k_bytes": k_bytes,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USED_TOTAL_MEMORY,
                                           self.parse_const.CHECK_USED_TOTAL_MEMORY, True,
                                           "Used total memory on slot {slot} is {operator} {k_bytes}.",
                                           "Used total memory on slot {slot} is NOT {operator} {k_bytes}!",
                                           **kwargs)

    def hostmonitor_verify_memory_current_total_utilization(self, device_name, slot='', percentage='', operator="=",
                                                            **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the current percentage of memory utilization.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_MEMORY_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_MEMORY_TOTAL_UTILIZATION, True,
                                           "Current memory total utilization on slot {slot} is"
                                           " {operator} {percentage}.",
                                           "Current memory total utilization on slot {slot} is"
                                           " NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_memory_5_minute_total_utilization(self, device_name, slot='', percentage='', operator="=",
                                                             **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies average percentage of memory utilization over the past 5 minutes.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_MEMORY_5_MINUTE_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_MEMORY_5_MINUTE_TOTAL_UTILIZATION, True,
                                           "5 minute memory total utilization on slot {slot} is"
                                           " {operator} {percentage}.",
                                           "5 minute memory total utilization on slot {slot} is"
                                           " NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_memory_5_minute_highest_total_utilization(self, device_name, slot='', percentage='',
                                                                     operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [percentage]  -  The percentage utilization value to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies high watermark for percentage memory utilization over the past 5 minutes.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args,
                                           self.cmd_const.SHOW_MEMORY_HIGHEST_5_MINUTE_TOTAL_UTILIZATION,
                                           self.parse_const.CHECK_MEMORY_HIGHEST_5_MINUTE_TOTAL_UTILIZATION, True,
                                           "5 minute highest memory total utilization on slot {slot}"
                                           " is {operator} {percentage}.",
                                           "5 minute highest memory total utilization on slot {slot}"
                                           " is NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_used_fbuffs(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       -  The number of used Fbufs to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the number of Fbuffs in use.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USED_FBUF,
                                           self.parse_const.CHECK_USED_FBUF, True,
                                           "Used FBUFFs on slot {slot} is {operator} {value}.",
                                           "Used FBUFFs on slot {slot} is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_free_fbuffs(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       -  The number of available Fbufs to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the number of available Fbufs.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FREE_FBUF,
                                           self.parse_const.CHECK_FREE_FBUF, True,
                                           "Free FBUFFs on slot {slot} is {operator} {value}.",
                                           "Free FBUFFs on slot {slot} is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_exhausted_fbuffs(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The number of times Fbuffs were exhausted to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the number of times Fbufs were exhausted.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_EXHAUSTED_FBUFS,
                                           self.parse_const.CHECK_EXHAUSTED_FBUFS, True,
                                           "Exhausted FBUFFs on slot {slot} is {operator} {value}.",
                                           "Exhausted FBUFFs on slot {slot} is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_network_stack_system_free_mbuffs(self, device_name, slot='', value='', operator="=",
                                                            **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The number of network stack system Mbuffs available to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the number of network stack system Mbuffs available.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NET_STACK_SYSTEM_FREE_MBUF,
                                           self.parse_const.CHECK_NET_STACK_SYSTEM_FREE_MBUF, True,
                                           "Network stack system free FBUFFs on slot {slot}"
                                           " is {operator} {value}.",
                                           "Network stack system free FBUFFs on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_network_stack_system_used_mbuffs(self, device_name, slot='', value='', operator="=",
                                                            **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The number of network stack system Mbuffs in use to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies number of network stack system Mbuffs in use.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NET_STACK_SYSTEM_USED_MBUF,
                                           self.parse_const.CHECK_NET_STACK_SYSTEM_USED_MBUF, True,
                                           "Network stack system used FBUFFs on slot {slot}"
                                           " is {operator} {value}.",
                                           "Network stack system used FBUFFs on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_network_stack_data_free_mbuffs(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The number of network stack data Mbuffs available to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the number of network stack data Mbuffs available.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NET_STACK_DATA_FREE_MBUF,
                                           self.parse_const.CHECK_NET_STACK_DATA_FREE_MBUF, True,
                                           "Network stack data free FBUFFs on slot {slot}"
                                           " is {operator} {value}.",
                                           "Network stack data free FBUFFs on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_network_stack_data_used_mbuffs(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The number of network stack data Mbuffs in use to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies number of network stack data Mbuffs in use.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NET_STACK_DATA_USED_MBUF,
                                           self.parse_const.CHECK_NET_STACK_DATA_USED_MBUF, True,
                                           "Network stack data used FBUFFs on slot {slot}"
                                           " is {operator} {value}.",
                                           "Network stack data used FBUFFs on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_network_stack_system_socket_mbuffs(self, device_name, slot='', value='', operator="=",
                                                              **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The number of network stack system socket Mbuffs to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the number of network stack system socket Mbuffs available.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_NET_STACK_SYSTEM_SOCKET_MBUF,
                                           self.parse_const.CHECK_NET_STACK_SYSTEM_SOCKET_MBUF, True,
                                           "Network stack system socket FBUFFs on slot {slot}"
                                           " is {operator} {value}.",
                                           "Network stack system socket FBUFFs on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_highest_queue_entries_consumed(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The highest number of queue entries consumed for system messaging to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies The highest number of queue entries consumed for system messaging.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HIGHEST_QUEUE_ENTRIES_CONSUMED,
                                           self.parse_const.CHECK_HIGHEST_QUEUE_ENTRIES_CONSUMED, True,
                                           "The highest queue entries consumed on slot {slot}"
                                           " is {operator} {value}.",
                                           "The highest queue entries consumed on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_current_queue_entries_consumed(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The current number of queue entries consumed for system messaging to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies The current number of queue entries consumed for system messaging.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CURRENT_QUEUE_ENTRIES_CONSUMED,
                                           self.parse_const.CHECK_CURRENT_QUEUE_ENTRIES_CONSUMED, True,
                                           "The current queue entries consumed on slot {slot}"
                                           " is {operator} {value}.",
                                           "The current queue entries consumed on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_free_queue_entries(self, device_name, slot='', value='', operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will be run against.
        [slot]        - The chassis slot position in the stack.
        [value]       - The current available number of queue entries for system messaging to compare against.
        [operator]    - The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the current available number of queue entries for system messaging.
        Note:  Currently this is VOSS proprietary specific.
        """
        args = {"slot": slot,
                "value": value,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_FREE_QUEUE_ENTRIES,
                                           self.parse_const.CHECK_FREE_QUEUE_ENTRIES, True,
                                           "The current available number of queue entries on slot {slot}"
                                           " is {operator} {value}.",
                                           "The current available number of queue entries on slot {slot}"
                                           " is NOT {operator} {value}!",
                                           **kwargs)

    def hostmonitor_verify_used_process_memory(self, device_name, slot='', process_name='', k_bytes='', operator="=",
                                               **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [slot]         - The chassis slot position in the stack.
        [process_name] - The process name.
        For EXOS: 'aaa','acl','bfd','bgp','brm','cfgmgr','cli','devmgr','dirser','dosprotect'
        'dot1ag','eaps','edp','elrp','elsm','ems','epm','erps','esrp','ethoam','etmon'
        'exacl','exdhcpsnoop','exdos','exfib','exfipSnoop','exnasnoop' ,'exosmc','exosq',
        'expolicy','exsflow','exsnoop','exsshd','exvlan','fcoe','fdb','hal','hclag'
        'idMgr','ipSecurity','ipfix','isis','ismb','lacp','lldp','mcmgr','mpls','mrp'
        'msdp','netLogin','netTools','nettx','nodealias','nodemgr','ntp','openflow'
        'ospf','ospfv3','otm','pim','polMgr','policy','ptpV2','pwmib','rip','ripng'
        'rtmgr','snmpMaster','snmpSubagent','stp','synce','techSupport','telnetd''tftpd'
        'throw','thttpd','twamp','upm','vlan','vmt','vpex','vrrp','vsm','xmlc','xmld'
        [k_bytes]     -  The value of Kilobytes to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies current memory consumption in Kilobytes for the process.
        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "oid_index": SnmpUtils().create_slot_process_string(slot, process_name),
                "process_name": StringUtils.ascii_to_dec(process_name),
                "process_name_string": process_name,
                "k_bytes": k_bytes,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_USED_MEMORY_FOR_PROCESS,
                                           self.parse_const.CHECK_USED_MEMORY_FOR_PROCESS, True,
                                           "Slot {slot} used user application memory for {process_name_string}"
                                           " is {operator} {k_bytes}.",
                                           "Slot {slot} used user application memory for {process_name_string}"
                                           " is NOT {operator} {k_bytes}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_process_state(self, device_name, slot='', process_name='', state='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [slot]         - The chassis slot position in the stack.
        [process_name] - The process name.
        [state]        - The state of the process.  Typically it is "Ready".
        For EXOS: 'aaa','acl','bfd','bgp','brm','cfgmgr','cli','devmgr','dirser','dosprotect'
        'dot1ag','eaps','edp','elrp','elsm','ems','epm','erps','esrp','ethoam','etmon'
        'exacl','exdhcpsnoop','exdos','exfib','exfipSnoop','exnasnoop' ,'exosmc','exosq',
        'expolicy','exsflow','exsnoop','exsshd','exvlan','fcoe','fdb','hal','hclag'
        'idMgr','ipSecurity','ipfix','isis','ismb','lacp','lldp','mcmgr','mpls','mrp'
        'msdp','netLogin','netTools','nettx','nodealias','nodemgr','ntp','openflow'
        'ospf','ospfv3','otm','pim','polMgr','policy','ptpV2','pwmib','rip','ripng'
        'rtmgr','snmpMaster','snmpSubagent','stp','synce','techSupport','telnetd''tftpd'
        'throw','thttpd','twamp','upm','vlan','vmt','vpex','vrrp','vsm','xmlc','xmld'

         Verifies the current state of the process as reported by Extremeware XOS.
         Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "oid_index": SnmpUtils().create_slot_process_string(slot, process_name),
                "process_name": StringUtils.ascii_to_dec(process_name),
                "process_name_string": process_name,
                "state": state}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_PROCESS_STATE,
                                           self.parse_const.CHECK_CPU_PROCESS_STATE, True,
                                           "Slot {slot} CPU process state for {process_name_string} is {state}.",
                                           "Slot {slot} CPU process state for {process_name_string}"
                                           " is NOT {state}!",
                                           **kwargs)

    def hostmonitor_verify_cpu_5_minute_process_utilization(self, device_name, slot='', process_name='', percentage='',
                                                            operator="=", **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will be run against.
        [slot]         - The chassis slot position in the stack.
        [process_name] - The process name.
        For EXOS: 'aaa','acl','bfd','bgp','brm','cfgmgr','cli','devmgr','dirser','dosprotect'
        'dot1ag','eaps','edp','elrp','elsm','ems','epm','erps','esrp','ethoam','etmon'
        'exacl','exdhcpsnoop','exdos','exfib','exfipSnoop','exnasnoop' ,'exosmc','exosq',
        'expolicy','exsflow','exsnoop','exsshd','exvlan','fcoe','fdb','hal','hclag'
        'idMgr','ipSecurity','ipfix','isis','ismb','lacp','lldp','mcmgr','mpls','mrp'
        'msdp','netLogin','netTools','nettx','nodealias','nodemgr','ntp','openflow'
        'ospf','ospfv3','otm','pim','polMgr','policy','ptpV2','pwmib','rip','ripng'
        'rtmgr','snmpMaster','snmpSubagent','stp','synce','techSupport','telnetd''tftpd'
        'throw','thttpd','twamp','upm','vlan','vmt','vpex','vrrp','vsm','xmlc','xmld'
        [percentage]  -  The value of percentage to compare against.
        [operator]    -  The operator (>, <, or =) to be used along with the count argument.
        If nothing is specified (=) will be used.

        Verifies the CPU utilization by this process. This is the utilization of the process in the last 5 minutes.

        Note:  Currently this is EXOS proprietary specific.
        """
        args = {"slot": slot,
                "oid_index": SnmpUtils().create_slot_process_string(slot, process_name),
                "process_name": StringUtils.ascii_to_dec(process_name),
                "process_name_string": process_name,
                "percentage": percentage,
                "operator": operator}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_CPU_PROCESS_5_MINUTE_UTILIZATION,
                                           self.parse_const.CHECK_CPU_PROCESS_5_MINUTE_UTILIZATION, True,
                                           "Slot {slot} CPU 5 minute utilization for {process_name_string}"
                                           " is {operator} {percentage}.",
                                           "Slot {slot} CPU 5 minute utilization for {process_name_string}"
                                           " is NOT {operator} {percentage}!",
                                           **kwargs)

    def hostmonitor_verify_slot_operational(self, device_name, slot='', **kwargs):
        """
        Keyword Arguments:
        [device_names] - The device(s) the keyword should be run against.
        [slot]     - The slot number that should be in Operational state
        Verifies the provided slot's state is Operational.
        Note:  Currently this is EXOS specific.
        """
        args = {"slot": slot}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SLOT,
                                           self.parse_const.CHECK_SLOT_OPERATIONAL, True,
                                           "Slot {slot} state is Operational.",
                                           "Slot {slot} state is NOT Operational!",
                                           **kwargs)
