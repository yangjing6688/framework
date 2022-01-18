"""
All webauth supported commands
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.webauth.base.webauthbase import WebauthBase


class Webauth(DeviceApi, WebauthBase):
    def __init__(self, device_input):
        super(Webauth, self).__init__(device_input)

    def enable_global(self, arg_dictionary, **kwargs):
        uuid = "8605577b-fe15-4664-baa7-6e84ac4421c1"
        cmd = "enable netlogin web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_global(self, arg_dictionary, **kwargs):
        uuid = "58c01afb-4532-4b08-bbe8-f44f0e54bda6"
        cmd = "disable netlogin web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_control_port(self, arg_dictionary, **kwargs):
        uuid = "475f2a85-c938-46de-b2b1-da36b8114e43"
        cmd = "enable netlogin ports {0} web-based".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_control_port(self, arg_dictionary, **kwargs):
        uuid = "93383c86-d287-4126-b217-16b639fa2b52"
        cmd = "disable netlogin ports {0} web-based".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_redirect_page(self, arg_dictionary, **kwargs):
        uuid = "ee9523ba-ceb5-433c-b27b-932152cb4fdb"
        cmd = "enable netlogin redirect-page"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_redirect_page(self, arg_dictionary, **kwargs):
        uuid = "f82a024e-faaf-483a-81eb-aa56eebaa87f"
        cmd = "disable netlogin redirect-page"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_logout_page(self, arg_dictionary, **kwargs):
        uuid = "0157c81a-3fdf-4044-86b1-bbfb86d4ab48"
        cmd = "enable netlogin logout-privilege"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_logout_page(self, arg_dictionary, **kwargs):
        uuid = "c5a90167-b800-4730-9599-8eedbb64671d"
        cmd = "disable netlogin logout-privilege"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "eb5e5732-eb51-4387-8349-5b520c99af74"
        cmd = "enable netlogin session-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "17fcbd87-7b7b-4027-992b-072260cf8179"
        cmd = "disable netlogin session-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def enable_reauthentication_on_refresh(self, arg_dictionary, **kwargs):
        uuid = "4d2f44e4-954c-4e88-be77-9c232aaa442e"
        cmd = "enable netlogin reauthenticate-on-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def disable_reauthentication_on_refresh(self, arg_dictionary, **kwargs):
        uuid = "276c579b-ed6c-43eb-8fbd-c03b4306afd9"
        cmd = "disable netlogin reauthenticate-on-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_hostname(self, arg_dictionary, **kwargs):
        uuid = "d8f21304-c087-4894-ab2f-8b00b90f21a6"
        cmd = "configure netlogin base-url {0}".format(arg_dictionary['url_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_init_mac_port(self, arg_dictionary, **kwargs):
        uuid = "19ce2e26-de9c-4974-af06-726750d8daaf"
        cmd = "clear netlogin state mac-address {0} port {1}".format(arg_dictionary['mac'],
                                                                     arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_init_port(self, arg_dictionary, **kwargs):
        uuid = "9155b2cb-6093-4f7d-b82b-32858ddf63b5"
        cmd = "clear netlogin state agent web-based port {0}".format(arg_dictionary['port'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_init_mac(self, arg_dictionary, **kwargs):
        uuid = "12cbca5e-67a7-4b96-8834-6fc0790a0fb5"
        cmd = "clear netlogin state agent web-based mac-address {0}".format(arg_dictionary['mac'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_init_all(self, arg_dictionary, **kwargs):
        uuid = "909e163d-aa1c-4e10-b95d-c69fc92fae88"
        cmd = "clear netlogin state agent web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_redirect_page(self, arg_dictionary, **kwargs):
        uuid = "ee1a4441-587d-48da-aa1e-edb66bc1dd88"
        cmd = "configure netlogin redirect-page {0}".format(arg_dictionary['redirect_page'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "3919fec3-b919-40ee-9266-3ffff001771d"
        cmd = "configure netlogin session-timeout web-based {0}".format(arg_dictionary['session_timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "1a0f1eb2-33a4-431f-818f-8ae0b4c748e5"
        cmd = "configure netlogin idle-timeout web-based {0}".format(arg_dictionary['idle_timeout'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_lease_time(self, arg_dictionary, **kwargs):
        uuid = "d8f32a89-1e25-4f90-8cd9-c504da005213"
        cmd = "configure vlan {0} netlogin-lease-timer {1}".format(arg_dictionary['vlan_name'],
                                                                   arg_dictionary['lease_time'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "73c3d442-1863-446e-ad0f-a6bb6639b7d2"
        cmd = "configure netlogin session-refresh {0}".format(arg_dictionary['session_refresh'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_allowed_refresh_failures(self, arg_dictionary, **kwargs):
        uuid = "aa8fac1c-6e03-4357-ae88-11d5f22f7d8b"
        cmd = "configure netlogin allowed-refresh-failures {0}".format(arg_dictionary['num_failures'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_protocol_order(self, arg_dictionary, **kwargs):
        uuid = "85cc0d41-59fc-4685-aaaa-759bac2dae56"
        cmd = "configure netlogin authentication protocol-order {0}".format(arg_dictionary['order'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_protocol_order_web_dot1x_mac(self, arg_dictionary, **kwargs):
        uuid = "5fed7b5a-4fc1-4dab-bcc8-7a65461e6192"
        cmd = "configure netlogin authentication protocol-order web-based dot1x mac"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_protocol_order_web_mac_dot1x(self, arg_dictionary, **kwargs):
        uuid = "884b221f-c28a-4e50-acbe-c0b5fdd0f739"
        cmd = "configure netlogin authentication protocol-order web-based mac dot1x"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_db_order_local(self, arg_dictionary, **kwargs):
        uuid = "73697d07-91d5-4fe4-a6d5-4a870269eed7"
        cmd = "configure netlogin web-based authentication database-order local"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_db_order_local_radius(self, arg_dictionary, **kwargs):
        uuid = "15afc978-0a35-408e-945c-648561a2db2c"
        cmd = "configure netlogin web-based authentication database-order local radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_db_order_radius(self, arg_dictionary, **kwargs):
        uuid = "a766710f-c829-4315-bf44-a3851e3d4e89"
        cmd = "configure netlogin web-based authentication database-order radius"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def set_db_order_radius_local(self, arg_dictionary, **kwargs):
        uuid = "beaebe2c-ab03-460b-bb97-8021cec0db01"
        cmd = "configure netlogin web-based authentication database-order radius local"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_hostname(self, arg_dictionary, **kwargs):
        uuid = "dba32dfa-85b2-4888-b3b4-ef9e48548c64"
        cmd = "configure netlogin base-url network-access.com"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_redirect_page(self, arg_dictionary, **kwargs):
        uuid = "671068c9-e516-4210-a488-8a63011c75d5"
        cmd = "configure netlogin redirect-page http://www.extremenetworks.com"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_session_timeout(self, arg_dictionary, **kwargs):
        uuid = "8b536a06-86f6-4753-b7ed-7ba1f265128d"
        cmd = "unconfigure netlogin session-timeout web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_idle_timeout(self, arg_dictionary, **kwargs):
        uuid = "b2827e2d-a25a-4580-8442-d1dd78585451"
        cmd = "unconfigure netlogin idle-timeout web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_lease_time(self, arg_dictionary, **kwargs):
        uuid = "49537bd8-9618-4d7d-918f-b0bbbafacc40"
        cmd = "configure vlan {0} netlogin-lease-timer 10".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_session_refresh(self, arg_dictionary, **kwargs):
        uuid = "5317e740-0148-4c5d-882c-154533d14dd6"
        cmd = "unconfigure netlogin session-refresh"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_allowed_refresh_failures(self, arg_dictionary, **kwargs):
        uuid = "3d21c5c4-0cc0-4504-8eae-d8f1c75b4809"
        cmd = "unconfigure netlogin allowed-refresh-failures"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_protocol_order(self, arg_dictionary, **kwargs):
        uuid = "af54254b-7d49-4107-91c9-2b8df0ad5b39"
        cmd = "configure netlogin authentication protocol-order dot1x mac web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def clear_db_order(self, arg_dictionary, **kwargs):
        uuid = "4aaa8f88-5d2c-47cc-9f8f-df2a90073548"
        cmd = "unconfigure netlogin web-based authentication database-order"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_summary_snapshot(self, arg_dictionary, **kwargs):
        uuid = "8db45701-652b-4f75-98ca-7b54283fe547"
        cmd = "show netlogin web-based"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_port(self, arg_dictionary, **kwargs):
        uuid = "3766b43d-58cc-40f6-9aaf-047508966934"
        cmd = "show config netlogin"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_timeout_values(self, arg_dictionary, **kwargs):
        uuid = "a7f16361-3c51-4921-b455-e968cf552be5"
        cmd = "show netlogin timeout"
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)

    def show_vlan_dhcp_netlogin_lease_time(self, arg_dictionary, **kwargs):
        uuid = "fb1e7e20-6f69-41ff-b98d-cc42809314f8"
        cmd = "show vlan {0} dhcp-config".format(arg_dictionary['vlan_name'])
        prompt = "userPrompt"

        return self.create_cmd_obj(uuid, cmd, prompt=prompt)
