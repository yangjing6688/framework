from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.CLI.cos.base.CosBaseCustomShowTools import \
    CosBaseCustomShowTools
# All imports above this line will be removed after generation.
# User imports must be added below.


def create_instance(device):
    return CosCustomShowTools(device)


class CosCustomShowTools(CosBaseCustomShowTools):
    def __init__(self, device):
        super(CosCustomShowTools, self).__init__(device)

    def check_qos_profile_exists(self, output, args, **kwargs):
        qos_profile = args["qp"].lower()
        output = output.lower()

        if qos_profile.isdigit():
            qos_profile = "qp" + qos_profile

        returned_profile_id = self.pw.get_value_by_offset(output, "qp", 0)
        qos_list = returned_profile_id.split(" ")

        result = True if qos_profile in qos_list else False
        return result, {"ret_qos_list": qos_list}

    def check_cos_port_resource(self, output, args, **kwargs):
        output = output.lower()

        meter = "ingmeter" + args["cos_index"]

        dev_rate = self.pw.get_value_by_offset(output, meter, 1)
        dev_unit = self.pw.get_value_by_offset(output, meter, 2)

        result = True if dev_rate == args["rate"] and dev_unit == args["unit"] else False
        return result, {"ret_rate": dev_rate,
                        "ret_unit": dev_unit}

    def check_port_group_exists(self, output, args, **kwargs):
        dev_groups = self.pw.get_value_by_offset(output, args["group"], 0)

        dev_groups = dev_groups.split(" ")

        result = True if args["group"] in dev_groups else False
        return result, {"ret_groups": dev_groups}

    def check_port_group_ports(self, output, args, **kwargs):
        ports = self.pw.get_value_by_offset(output, args["group"], 1)

        result = self.it.compare_port_values(ports, args["port"], self.inspect_constants.CONTAINS)
        return result, {"ret_ports": ports}

    def check_qos_scheduler_mode(self, output, args, **kwargs):
        if args["mode"] == 0:
            args["mode"] = "strict-priority"
        elif args["mode"] == 1:
            args["mode"] = "weighted-round-robin"
        elif args["mode"] == 2:
            args["mode"] = "weighted-deficit-round-robin"

        dev_mode = self.pw.get_value_by_offset(output.lower(), "configured scheduler", 3)

        result = True if dev_mode == args["mode"] else False
        return result, {"ret_mode": dev_mode}

    def check_cos_settings(self, output, args, **kwargs):
        output = output.lower()
        output = output.splitlines()

        result = False
        indexes = list()

        if args.get("tos", None) == "*":
            args["tos"] = "--"
        if args.get("txq", None) == "*":
            args["txq"] = "--"
        if args.get("irl", None) == "*":
            args["irl"] = "--"

        if args.get("txq", None) is not None and args["txq"].isdigit():
            args["txq"] = "qp" + str(int(args["txq"]) + 1)

        for i, line in enumerate(output):
            if line.find("-----") != -1:
                i += 1
                while i < len(output) - 1:
                    indexes.append(output[i])
                    i += 1
                else:
                    break

        ret_dict = {"priority": None,
                    "tos": None,
                    "txq": None,
                    "irl": None,
                    "orl": None,
                    "drop_prec": None,
                    "flood_ctrl": None}

        for entry in indexes:
            dev_index = self.pw.get_value_by_offset(entry, "", 0)

            if dev_index == args["cos_index"]:
                ret_dict["txq"] = self.pw.get_value_by_offset(entry, "", 1)
                ret_dict["priority"] = str(int(ret_dict["txq"][2:]) - 1)
                ret_dict["tos"] = self.pw.get_value_by_offset(entry, "", 2)
                ret_dict["irl"] = self.pw.get_value_by_offset(entry, "", 4)

                if ret_dict["irl"] != "--":
                    ret_dict["irl"] = ret_dict["irl"][8:]  # Remove "ingmeter" from dev_irl.

                result = True
                if args.get("tos", None) is not None and result:
                    if ret_dict["tos"] != args["tos"]:
                        result = False
                if args.get("txq", None) is not None and result:
                    if ret_dict["txq"] != args["txq"]:
                        result = False
                if args.get("irl", None) is not None and result:
                    if ret_dict["irl"] != args["irl"]:
                        result = False
                if args.get("priority", None) is not None and result:
                    if ret_dict["priority"] != args["priority"]:
                        result = False
            if result:
                return True, ret_dict
        return result, ret_dict

    def check_txq_weights(self, output, args, **kwargs):
        output = output.lower()
        output = output.splitlines()

        conf_weights = list()
        weights = args["weights"].split(",")

        for line in output:
            if line.find("qp") > 0:
                conf_weights.append(self.pw.get_value_by_offset(line, "", 12))

        for i in range(len(conf_weights)):
            if conf_weights[i] != weights[i]:
                return False, {"ret_weights": conf_weights}

        return True, {"ret_weights": conf_weights}

    def verify_port_priority(self, output, args, **kwargs):
        """
        The following function returns True if the priority value found in the output is equal to the priority
        argument provided.
        """
        configured_priority = self.pw.get_value_by_offset(output, "Ingress 802.1p Priority:", 3)

        result = True if args["priority"] == configured_priority else False
        return result, {"ret_priority": configured_priority}

    def check_port_qos_profile(self, output, args, **kwargs):
        dev_qos_profile = self.pw.get_value_by_offset(output, "QoS Profile:", 2).lower()
        qp = "qp" + args["qp"] if args["qp"].isdigit() else args["qp"]

        result = True if dev_qos_profile == qp.lower() else False
        return result, {"ret_qos_profile": dev_qos_profile}
