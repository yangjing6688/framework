from ExtremeAutomation.Library.Net.Packet.PacketObject import PacketConstants


class TrafficGenerationUtils(object):

    # since smart bits does port handles different, I had to move the port stuff to the TrafficGenerating Device
    # @staticmethod
    # def convert_port_to_port_handle(port_string):
    #     if isinstance(port_string, list):
    #         index = 0
    #         for port in port_string:
    #             port_string[index] = TrafficGenerationUtils.convert_port_to_port_handle(port)
    #             index += 1
    #     else:
    #         # change [0-9]+.[0-9]+.[0-9]+ to 1/1/1
    #         # change [0-9]+ [0-9]+ [0-9]+ to 1/1/1
    #         port_string = port_string.replace(".", "/")
    #         port_string = port_string.replace(" ", "/")
    #         if not len(port_string.split("/")) is 3:
    #             port_string = "1/"+port_string
    #     if isinstance(port_string, list):
    #         return " ".join(port_string)
    #     else:
    #         return port_string

    @staticmethod
    def convert_port_string_to_file_string(port_string):
        # change [0-9]+.[0-9]+.[0-9]+ to 1/1/1
        # change [0-9]+ [0-9]+ [0-9]+ to 1/1/1
        port_string = port_string.replace(" ", ".")
        port_string = port_string.replace("/", ".")
        if not len(port_string.split(".")) == 3:
            port_string = "1." + port_string
        port_string = port_string.replace(".", "")
        return "-1-" + port_string

    #
    # @staticmethod
    # def convert_port_handle_to_port_string(port_string):
    #     if (devicetype == None):
    #         if isinstance(port_string, list):
    #             index = 0
    #             for port in port_string:
    #                 port_string[index] = self.convert_port_handle_to_port_string(port)
    #                 index += 1
    #         else:
    #             port_string = self.convert_port_handle_to_port_string(port_string)
    #             #  1/1/1 to 1/1
    #             spl = port_string.split("/")
    #             if not len(spl) is 2:
    #                 port_string = spl[len(spl)-2] + "/" + spl[len(spl)-1]
    #         if isinstance(port_string, list):
    #             return " ".join(port_string)
    #         else:
    #             return port_string

    # @staticmethod
    # def convert_port_string_to_ixtclhal_port(port_string):
    #     port_string = TrafficGenerationUtils.convert_port_to_port_handle(port_string)
    #     #  1/1/1 to 1 1 1
    #     return port_string.replace("/", " ")

    @staticmethod
    def convert_port_string_to_ixtclhal_port(port_string):
        port_string = port_string.replace(".", " ").replace("/", " ")
        port_string = port_string.split(" ")
        if len(port_string) == 2:
            port_string.insert(0, "1")
        port_string = " ".join(port_string)
        #  1/1/1 to 1 1 1
        return port_string.replace("/", " ")

    @staticmethod
    def convert_port_string_to_port_handle(port_string):
        port_string = port_string.replace(".", " ").replace("/", " ")
        port_string = port_string.split(" ")
        if len(port_string) == 2:
            port_string.insert(0, "1")
        port_string = "/".join(port_string)
        #  1/1/1 to 1 1 1
        return port_string

    @staticmethod
    def merge_arrays(a1, a2):
        temp = a1.copy()
        if a2:
            temp.update(a2)
        return temp

    @staticmethod
    def insert_ixtcl_command(dummy_dict, val, cmd, _type):
        if isinstance(val, int):
            val = str(val)
        if val and val.find('Not Set') == -1 and val.replace(" ", "").find('NotSet') == -1:
            if _type == PacketConstants.HEX_STRING:
                dummy_dict.append(cmd + " \"" + val + "\"")
            else:
                dummy_dict.append(cmd + " \"" + val + "\"")

    # @staticmethod
    # def compare_only_set_fields(expected_packet, received_packet, ignore_list=None, show_all=True,
    #                             show_failures=True):
    #     AbstractPacket.compare_packet_fields(expected_packet, received_packet, ignore_list=None, show_all=True,
    #                                          show_failures=True)
    #     # assert isinstance(expected_packet, PacketObject)
    #     # composites = expected_packet.get_all_packet_fields()
    #     # for composite in composites:
    #     #     components = composites[composite]
    #     #     for component in components:
    #     #         eval = expected_packet.get_packet_component(composite, component)
    #     #         rval = received_packet.get_packet_component(composite, component)
    #     #         print composite + " " + component + " " + str(eval) + " = " + str(rval)
