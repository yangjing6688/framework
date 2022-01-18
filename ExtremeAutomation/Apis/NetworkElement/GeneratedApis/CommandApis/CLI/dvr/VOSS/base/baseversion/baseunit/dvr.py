"""
All dvr supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.dvr.base.dvrbase import DvrBase


class Dvr(DeviceApi, DvrBase):
    def __init__(self, device_input):
        super(Dvr, self).__init__(device_input)

    def set_domain_controller(self, arg_dictionary, **kwargs):
        uuid = "a9354712-f304-477b-ad23-6e9e42e13dfa"
        cmd = "dvr controller {0}".format(arg_dictionary['domain_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_domain_controller(self, arg_dictionary, **kwargs):
        uuid = "0b080271-8fba-4eff-90ba-7c75c884eecc"
        cmd = "no dvr controller"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_domain_controller_inject_default_route_all(self, arg_dictionary, **kwargs):
        uuid = "a6241fde-5aad-4228-92b7-f58aefb50a1f"
        cmd = "dvr controller inject-default-route-disable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_domain_controller_inject_default_route(self, arg_dictionary, **kwargs):
        uuid = "5ad92c0d-527e-43b4-8ef2-7397d22d44f1"
        cmd = "dvr controller {0} inject-default-route-disable".format(arg_dictionary['domain_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_leaf_id(self, arg_dictionary, **kwargs):
        uuid = "912359c5-35e4-47f8-8493-60f314775716"
        cmd = "dvr leaf {0}".format(arg_dictionary['domain_id'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_leaf_virtual_ist(self, arg_dictionary, **kwargs):
        uuid = "3ec2c0ab-0858-49cc-904b-dad9c3b31b94"
        cmd = "dvr leaf virtual-ist {0} {1} peer-ip {2} cluster-id {3}".format(arg_dictionary['local_ip'],
                                                                               arg_dictionary['mask'],
                                                                               arg_dictionary['peer_ip'],
                                                                               arg_dictionary['cluster_id'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_leaf_virtual_ist(self, arg_dictionary, **kwargs):
        uuid = "04166cee-a168-4d87-be9a-a7066f89dd3d"
        cmd = "no dvr leaf virtual-ist"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_interface_gateway_ipv4(self, arg_dictionary, **kwargs):
        uuid = "7b57b57b-b8da-4b65-beb6-d6378e002fa3"
        cmd = "dvr gw-ipv4 {0}".format(arg_dictionary['ip'])
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def clear_interface_gateway_ipv4(self, arg_dictionary, **kwargs):
        uuid = "0f24691c-49cf-4a99-9286-f6a55ade9a3a"
        cmd = "no dvr gw-ipv4"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def enable_interface(self, arg_dictionary, **kwargs):
        uuid = "5ca6c2e3-261f-4af1-9e7b-f1a7fcd6928e"
        cmd = "enable dvr"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def disable_interface(self, arg_dictionary, **kwargs):
        uuid = "675309c2-4098-4849-bf6b-35112f847d19"
        cmd = "no enable dvr"
        prompt = "intfPrompt"
        prompt_args = "vlan {0}".format(arg_dictionary['interface'])

        return self.create_cmd_obj(uuid, cmd, prompt=prompt, prompt_args=prompt_args)

    def set_redistribute(self, arg_dictionary, **kwargs):
        uuid = "e276fd26-c1b6-4ff6-8f6a-de90d7d18a19"
        cmd = "dvr apply redistribute"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "8218d215-1b64-4859-83aa-9c6a24e5b500"
        cmd = "dvr apply redistribute direct"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_direct_metric(self, arg_dictionary, **kwargs):
        uuid = "ee3ffa88-b799-48f3-9d8a-1b0d79133d3a"
        cmd = "dvr redistribute direct metric {0}".format(arg_dictionary['metric'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_vrf(self, arg_dictionary, **kwargs):
        uuid = "772add6c-9ead-4a38-acc5-2e2a022ec026"
        cmd = "dvr apply redistribute vrf {0}".format(arg_dictionary['vrf'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "5fccb62e-e05c-48ec-bd98-52696f881319"
        cmd = "no dvr redistribute direct"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "f65ace22-c6d0-42a6-a806-806faad1a763"
        cmd = "dvr redistribute direct enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_direct(self, arg_dictionary, **kwargs):
        uuid = "97430b8d-49f6-4ea7-8b9d-80b7f3c1f86a"
        cmd = "no dvr redistribute direct enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "8580a1f9-ad78-44a7-b36a-f8dc0f0c8395"
        cmd = "dvr apply redistribute static"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redistribute_static_metric(self, arg_dictionary, **kwargs):
        uuid = "79131e5a-93e3-4e81-944f-041e50b5f6dc"
        cmd = "dvr redistribute static metric {0}".format(arg_dictionary['metric'])
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "649e982c-da7b-42d2-aa4e-611ccfd944f4"
        cmd = "no dvr redistribute static"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "f84d11b1-ad75-435a-baee-686c854b42a6"
        cmd = "dvr redistribute static enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redistribute_static(self, arg_dictionary, **kwargs):
        uuid = "cc74db7b-4152-4fba-a553-b6cc47c83186"
        cmd = "no dvr redistribute static enable"
        prompt = "routerConfigPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_host_entries(self, arg_dictionary, **kwargs):
        uuid = "60738e0e-9974-4a7a-bc90-750dffd6d684"
        cmd = "clear dvr host-entries"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_host_entries_ipv4(self, arg_dictionary, **kwargs):
        uuid = "29bfcbbc-6451-4a34-8e3e-1d6eb7c45191"
        cmd = "clear dvr host-entries {0}".format(arg_dictionary['ip'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_host_entries_ipv4_l3isid(self, arg_dictionary, **kwargs):
        uuid = "f4fc181e-2dd8-47ed-b1ca-bb3669c97cdf"
        cmd = "clear dvr host-entries {0} l3isid {1}".format(arg_dictionary['ip'],
                                                             arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_host_entries_l2isid(self, arg_dictionary, **kwargs):
        uuid = "a89a7127-50d7-482d-8324-6aacf96db0c0"
        cmd = "clear dvr host-entries l2isid {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_host_entries_l3isid(self, arg_dictionary, **kwargs):
        uuid = "c8e41357-3e78-4751-9097-af9c99a8d357"
        cmd = "clear dvr host-entries l3isid {0}".format(arg_dictionary['isid'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_info(self, arg_dictionary, **kwargs):
        uuid = "cbd5c6fa-ee55-4f6e-9636-d71d8ca026fd"
        cmd = "show dvr"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_interfaces(self, arg_dictionary, **kwargs):
        uuid = "f6611778-a98d-4cca-85d3-22808704c34f"
        cmd = "show dvr interfaces"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_members(self, arg_dictionary, **kwargs):
        uuid = "602dc40d-2c84-421c-b5f8-995a75a1ed65"
        cmd = "show dvr members"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_backbone_entries(self, arg_dictionary, **kwargs):
        uuid = "e75b74d4-0f45-48a2-becc-f1686af8d9d9"
        cmd = "show dvr backbone-entries"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_backbone_members(self, arg_dictionary, **kwargs):
        uuid = "8f65a37d-6dc0-40eb-8e3a-29b51dd45bd2"
        cmd = "show dvr backbone-members"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_database(self, arg_dictionary, **kwargs):
        uuid = "8d3c005b-64ed-4c3f-a34c-fc327ae47b1f"
        cmd = "show dvr database"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_host_entries(self, arg_dictionary, **kwargs):
        uuid = "3372483e-f976-446c-ab0c-20502da19b26"
        cmd = "show dvr host-entries"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_l3vsn(self, arg_dictionary, **kwargs):
        uuid = "9bb84fef-65d1-4d69-8de6-f87f8687d0ad"
        cmd = "show dvr l3vsn"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_redistribute(self, arg_dictionary, **kwargs):
        uuid = "a776779c-56d6-4a36-afa0-a3dd2c69a086"
        cmd = "show dvr redistribute"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_routes(self, arg_dictionary, **kwargs):
        uuid = "b4a7f9a1-4412-4eac-a500-ace25fe04b87"
        cmd = "show dvr routes"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
