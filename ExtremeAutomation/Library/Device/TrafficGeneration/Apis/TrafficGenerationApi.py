from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.TrafficGeneration.TrafficGeneratingCommandObject import \
    TrafficGeneratingCommandObject
from ExtremeAutomation.Library.Utils.Time import current_milli_time
import inspect
from collections import deque


class TrafficGenerationApi(DeviceApi):
    def __init__(self, dev):
        super(TrafficGenerationApi, self).__init__(dev)
        self._nameSpace = dev.get_name_space()

    def send_command(self, cmd):
        """sends the command to the Traffic Generator"""
        cmd_obj = TrafficGeneratingCommandObject()
        cmd_obj.command = cmd
        cmd_obj.start_time = current_milli_time()
        cmd_obj.return_text = TrafficGenerationApi.parse_output(self.get_device().send_command(cmd).strip())
        cmd_obj.end_time = current_milli_time()
        return cmd_obj

    def send_command_no_parse(self, cmd):
        """sends the command to the Traffic Generator"""
        cmd_obj = TrafficGeneratingCommandObject()
        cmd_obj.command = cmd
        cmd_obj.start_time = current_milli_time()
        cmd_obj.return_text = self.get_device().send_command(cmd).strip()
        cmd_obj.end_time = current_milli_time()
        return cmd_obj

    def send_command_wrapped(self, cmd):
        return self.send_command(self.wrap_command_in_return(cmd))

    def send_command_args(self, cmd, arg_list):
        cmd_string = "" + cmd + " \\\n"  # send command to the telnetlib
        cmd_string += self.arglist_to_command(arg_list)
        return self.send_command_wrapped(cmd_string)

    def get_device(self):
        return self.device

    def process_supported_hltapi_commands(self, argdictionary, supported=None, outside_supported=None):
        if supported is None:
            return
        if outside_supported is None:
            outside_supported = []
        prerequisites = []
        keys = dict.fromkeys(argdictionary)
        for key in keys:
            val = argdictionary[key]
            if key not in supported:
                if key not in outside_supported:  # if outside api support isn't done, print it to the logs.
                    msg = "Not supported command: " + str(key) + ":" + str(val) + " << removed"
                    self.logger.log_info(msg)
                else:
                    msg = "not supported command: " + str(key) + ":" + str(val) + " << removed, but done another way"
                    self.logger.log_info(msg)

                del argdictionary[key]
            else:
                prerequisites.append(key)
        # this is for versioned information
        # prerequisites = ListUtils.uniquevalues(prerequisites)
        # missing_prerequisites = []
        # for val in prerequisites:
        #     key, version = val.split(":")
        #     current_version = self._device.get_version(key)
        #     if version > current_version:
        #         missing_prerequisites = key + " is version " + current_version + " but requires version " + version

    @staticmethod
    def wrap_command_in_return(cmd):

        ret_name = "returnValue"
        curframe = inspect.stack()
        # formatted_lines = []
        # bStartedLogging = False
        try:
            for s in curframe:
                path_name = str(s[1]).lower()
                method_name = str(s[3])
                current_frame = s[0]
                args, _, _, values = inspect.getargvalues(current_frame)
                if "hlt" in str(path_name).lower():
                    if "/" in path_name:
                        api_name = path_name.split("/")
                    else:
                        api_name = path_name.split("\\")
                    api_name = api_name[-1]
                    api_name = api_name.replace(".py", "")
                    ret_name = api_name + "_" + method_name
                    break
            # index = 1
            # ret_string = ""
        except:
            pass

        return "set " + ret_name + " [" + cmd + "]"

    # def getPortReferene(self, port):
    #     """
    #     gets a named Port Refence to use in the scripting
    #     """
    #     self.usePort(self.normalizePortToHandle(port), port)
    #     print "set "+self.normalizePortToHandle(port)+" [keylget connect_info port_handle.$ixia(device)."+port+"]"
    #
    #
    # def normalizePortToHandle(self, port):
    #     return "$"+port.replace(".", "_").replace(" ", "_")
    #
    # def usePort(self, portName, port):
    #     self.send_command(portName + " = " + port)

    @staticmethod
    def arglist_to_command(arg_list):
        ret_string = ""
        for key in arg_list:
            value = arg_list[key]
            ret_string += "-" + key + " " + str(value) + " \\\n"
        return ret_string

    @staticmethod
    def parse_output(string):
        ret_dict = []
        lines = string.split("\n")
        for line in lines:
            ret_dict.append(TrafficGenerationApi.parse_output_lines(line))
        return ret_dict

    @staticmethod
    def parse_output_lines(string):
        name = ""
        if '{' not in string or string.count('{') != string.count('}'):
            if ' ' in string:
                parts = string.split(" ", 1)
                return [parts[0], " ".join(parts[1:])]
            else:
                return string
        if not string.startswith("{"):  # this means it looks like "name  {more list}"
            parts = string.split(" ", 1)
            string = parts[1]
            name = parts[0]
            ret_dict = dict()
        else:
            ret_dict = []
        start_index = -1
        depth = 0
        content_string = ""
        for i in range(0, len(string)):
            if string[i] == '{':
                if start_index < 0:
                    start_index = i
                else:
                    content_string += string[i]
                depth += 1
            elif string[i] == '}':
                depth -= 1
                if depth != 0:
                    content_string += string[i]
            else:
                content_string += string[i]
            if depth == 0 and len(content_string.strip()) > 0:
                if isinstance(ret_dict, dict):
                    ret_dict[name] = TrafficGenerationApi.parse_output_lines(content_string.strip())
                else:
                    ret_dict.append(TrafficGenerationApi.parse_output_lines(content_string.strip()))
                content_string = ""
                start_index = -1
        return ret_dict

    @staticmethod
    def get_flattened_value(values, port_handle, key):
        if isinstance(values, TrafficGeneratingCommandObject):
            values = values.return_text
        for lista in values:
            if isinstance(lista, list):
                for deq in lista:
                    if isinstance(deq, dict) and port_handle in deq:
                        port_info = deq[port_handle]
                        for elm in port_info:
                            if isinstance(elm, list):
                                if elm[0] == key:
                                    return " ".join(elm[1:])
                    if isinstance(deq, list):
                        if deq[0] == key:
                            return " ".join(deq[1:])
        return False

    def send_commands(self, commands_list):
        ret_string = deque()
        for cmd in commands_list:
            # ret_string.update(
            ret_string.append(self.send_command(cmd))
        return ret_string

    def strip_return(self, mess):
        if isinstance(mess, TrafficGeneratingCommandObject):
            if len(mess.return_text) > 0:
                ret_string = str(mess.return_text[0])
            else:
                ret_string = ""
        else:
            ret_string = str(mess)
        ret_string = ret_string.replace('%', '')
        return ret_string.strip()


# ret_dict = TrafficGenerationApi.parse_output("{port_handle {{10 {{52 {{2 {{189 {{1/1 1/1/1} {1/2 1/1/2}}}}}}}}}}}
#            {status 1}")
# ret_dict = TrafficGenerationApi.parse_output("{1 1 1} {1 1 2}")
# ret_dict = TrafficGenerationApi.parse_output("{1/1/1 {{aggregate {{rx {{uds2_count 0} {qos2_rate
#            {Stat qualityOfService2 not supported}} {pkt_byte_count 0} {qos0_count
#            {Stat qualityOfService0 not supported}} {vlan_pkts_rate {Stat vlanTaggedFramesRx not supported}}
#            {sequence_errors_count 0} {qos4_count {Stat qualityOfService4 not supported}} {crc_errors_count 0}
#            {qos7_rate {Stat qualityOfService7 not supported}} {uds1_count 0} {raw_pkt_count 0} {data_int_errors_count
#            {Stat dataIntegrityErrors not supported}} {uds2_rate 0} {qos4_rate {Stat qualityOfService4 not supported}}
#            {vlan_pkts_count {Stat vlanTaggedFramesRx not supported}} {data_int_errors_rate
#            {Stat dataIntegrityErrors not supported}} {raw_pkt_rate 0} {pkt_bit_count 0} {qos3_count
#            {Stat qualityOfService3 not supported}} {qos1_rate {Stat qualityOfService1 not supported}}
#            {fragments_count 0} {collisions_count 0} {qos7_count {Stat qualityOfService7 not supported}}
#            {sequence_frames_count 0} {sequence_errors_rate 0} {collisions_rate 0} {fragments_rate 0}
#            {data_int_frames_rate {Stat dataIntegrityFrames not supported}}
#            {qos6_rate{Stat qualityOfService6 not supported}} {qos2_count {Stat qualityOfService2 not supported}}
#            {pkt_count 0} {dribble_errors_count 0} {uds1_rate 0} {qos3_rate {Stat qualityOfService3 not supported}}
#            {qos6_count {Stat qualityOfService6 not supported}} {data_int_frames_count
#            {Stat dataIntegrityFrames not supported}} {dribble_errors_rate 0} {qos0_rate
#            {Stat qualityOfService0 not supported}} {crc_errors_rate 0} {oversize_count 0} {pkt_bit_rate 0}
#            {sequence_frames_rate 0} {pkt_rate 0} {undersize_rate 0} {qos1_count
#            {Stat qualityOfService1 not supported}} {pkt_byte_rate 0} {protocol_pkt_count 0} {qos5_count
#            {Stat qualityOfService5 not supported}} {undersize_count 0} {oversize_rate 0} {qos5_rate
#            {Stat qualityOfService5 not supported}} {protocol_pkt_rate {Stat protocolServerRx not supported}}}}
#            {tx {{raw_pkt_count 2308} {pkt_byte_count 147712} {total_pkt_rate 0} {pkt_bit_count 1181696}
#            {pkt_bit_rate 10235} {pkt_rate 20} {pkt_count 2308} {total_pkt_bytes 0} {total_pkts_bytes 0}
#            {elapsed_time 115.30} {pkt_byte_rate 1279} {protocol_pkt_rate {Stat protocolServerTx not supported}}
#            {total_pkts 0} {raw_pkt_rate 20} {protocol_pkt_count 0}}}}} {elapsed_time
#            {Stat transmitDuration not supported}}}} {seconds 1450291078} {clicks 881755059} {status 1}")


class TrafficGenerationConstants:
    TELNET = "telnet"
    SSH = "ssh"
    INTERFACE_CONFIG_API = "TRAFFIC_GENERATION_INTERFACE_CONFIG_API"
    CONNECT_API = "TRAFFIC_GENERATION_CONNECT_API"
    # this is for ostinato and other 3rd party
    NUMBER_OF_PACKETS_CMD = "NUMBER_OF_PACKETS_CMD"

    def __setattr__(self, *_):
        pass


TrafficGenerationConstants = TrafficGenerationConstants()
