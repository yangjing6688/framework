
import string
import random
import re

from collections import defaultdict
from extauto.common.Cli import Cli
from extauto.common.AutoActions import AutoActions
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.flows.manage.Device360 import Device360
from extauto.xiq.flows.manage.DeviceConfig import DeviceConfig
from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
from extauto.xiq.flows.configure.CommonObjects import CommonObjects
from extauto.xiq.flows.configure.SwitchTemplate import SwitchTemplate
from extauto.common.CommonValidation import CommonValidation
from extauto.xiq.flows.manage.Tools import Tools


class XiqVerifications:

    def __init__(self):
        self.auto_actions = AutoActions()
        self.utils = Utils()
        self.screen = Screen()
        self.devices = Devices()
        self.navigator = Navigator()
        self.device360 = Device360()
        self.switch_template = SwitchTemplate()
        self.device_config = DeviceConfig()
        self.deviceCommon = DeviceCommon()
        self.common_validation = CommonValidation()
        self.common_objects = CommonObjects()
        self.tools = Tools()
        self.cli = Cli()

    def verify_path_cost_at_template_level(
        self, onboarded_switch, path_cost, template_switch,
        network_policy, default_path_cost="", revert_mode="revert_template",
        port_type="access", verify_delta_cli=False, stp_mode="mstp",
        revert_configuration=True, port_order_in_asic=None, ports=None, slot=None):
        """This method is used to set the path cost in XIQ on an already onboarded switch.
        Also it will verify the configuration on the switch once it is configured.

        Args:
            onboarded_switch (dict): the switch - e.g. tb.dut1
            path_cost (int): the path cost value
            template_switch (str): the name of the switch template
            network_policy (str): the name of the network policy
            default_path_cost (int, optional): the default path cost. Defaults to "".
            revert_mode (str, optional): the revert mode. Defaults to "revert_template".
            port_type (str, optional): the port type. Defaults to "access".
            verify_delta_cli (bool, optional): enable of disable the delta cli verification. Defaults to False.
            stp_mode (str, optional): the stp mode. Defaults to "mstp".
            revert_configuration (bool, optional): revert or not the configuration. Defaults to True.
            port_order_in_asic (int, optional): the order in asic of the port we want to verify. Defaults to None.
            ports (List[str], optional): a list of ports to be verified. Defaults to None.
            slot (str, optional): the slot of the stack to be verified. Defaults to None.

        Returns: None; The function will raise an error if the verification failed.

        """
        if not default_path_cost:
            default_path_cost = "200000000" if onboarded_switch.cli_type.upper() == "VOSS" else "20000"

        if not ports:
            ports = self.device360.get_one_port_from_each_asic_flow(
                dut=onboarded_switch, order=port_order_in_asic, slot=slot)

        port_config = defaultdict(lambda: {})
        for port in ports:
            port_config[port]["port_type_name"] = f"port_type_{''.join(random.sample(list(string.ascii_letters) + list(string.digits), k=6))}"
            port_config[port]["path_cost"] = str(random.choice(range(1, 200000000)))\
                if path_cost == "random" else path_cost
            self.utils.wait_till(timeout=0.7)
        self.utils.print_info(f"Port Type Configuration: {port_config}")

        self.utils.print_info(
            f"Go to the port configuration of '{template_switch}' template")
        self.switch_template.select_sw_template(
            network_policy, template_switch)
        self.switch_template.set_stp(enable=True)
        self.switch_template.choose_stp_mode(mode=stp_mode)
        self.switch_template.go_to_port_configuration()

        if slot:
            required_slot = template_switch + "-" + slot
            self.switch_template.navigate_to_slot_template(required_slot)

        self.switch_template.click_on_port_details_tab()

        try:
            try:
                for port, port_type_config in port_config.items():
                    self.utils.print_info(
                        f"Configuring port '{port}' with {port_type_config}")

                    try:
                        self.device360.open_new_port_type_editor(port=port)
                        self.device360.configure_port_name_usage_tab(
                            port_type_name=port_type_config["port_type_name"],
                            port_type=port_type
                        )
                        self.device360.go_to_stp_settings_tab_in_honeycomb()
                        self.device360.verify_path_cost_field_is_editable()
                        self.device360.configure_stp_settings_tab_in_honeycomb(
                            stp_enabled=True,
                            edge_port=True,
                            bpdu_protection="Disabled",
                            path_cost=port_type_config["path_cost"]
                        )
                        self.device360.go_to_last_page()

                        expected_summary = {
                            'STP': 'Enabled',
                            'Edge Port': 'Enabled',
                            'BPDU Protection': 'Disabled',
                            'Path Cost': str(port_type_config["path_cost"])
                            }
                        self.utils.print_info(
                            f"Expected summary: {expected_summary}")

                        summary = self.device360.get_stp_settings_summary()
                        self.utils.print_info(f"Found summary: {summary}")

                        self.utils.print_info(
                            "Verify that the configured fields"
                            " appear correctly in the summary tab"
                        )

                        assert all(expected_summary[k] == summary[k] for k in expected_summary), \
                            "Not all the values of the summary are the expected ones. " \
                            f"Expected summary: {expected_summary}\nFound summary: {summary}"
                        self.utils.print_info("Successfully verified the summary")

                    finally:
                        self.device360.save_port_type_config()

            finally:

                self.utils.wait_till(timeout=5)
                self.switch_template.switch_template_save()
                self.utils.wait_till(timeout=10)

            for port, port_type_config in port_config.items():
                self.utils.print_info(
                    f"Verifying STP tab for port {port}: {port_type_config}")
                self.switch_template.verify_path_cost_in_port_configuration_stp_tab(
                    template_switch, network_policy, port,
                    port_type_config["path_cost"], slot=slot
                )

            if verify_delta_cli:
                commands = []
                if onboarded_switch.cli_type.upper() == "EXOS":

                    for port, port_type_config in port_config.items():
                        commands.append(
                            f"configure stpd s0 ports cost {port_type_config['path_cost']} {port}")

                elif onboarded_switch.cli_type.upper() == "VOSS":
                    commands.extend(
                        [
                            "enable",
                            "configure terminal"
                        ]
                    )

                    for port, port_type_config in port_config.items():
                        commands.extend(
                            [
                                f"interface gigabitEthernet {port}",
                                f"spanning-tree {stp_mode} cost {port_type_config['path_cost']}"
                            ]
                        )

                elif onboarded_switch.cli_type.upper() == "AH-FASTPATH":
                    commands.extend(
                        [
                            "enable",
                            "configure"
                        ]
                    )
                    for port, port_type_config in port_config.items():
                        commands.extend(
                            [
                                f"interface {port}",
                                f"spanning-tree cost {port_type_config['path_cost']}"
                            ]
                        )

                self.device_config.verify_delta_cli_commands(
                    onboarded_switch, commands=commands)

            self.devices.update_and_wait_device(
                policy_name=network_policy, dut=onboarded_switch)

            for port, port_type_config in port_config.items():
                self.utils.print_info(
                    f"Verifying path cost for port {port} on dut:"
                    f" {port_type_config}"
                )
                self.cli.verify_path_cost_on_device(
                    onboarded_switch,
                    expected_path_cost=port_type_config["path_cost"],
                    port=port,
                    mode=stp_mode
                )

        finally:

            if revert_configuration:
                try:
                    self.utils.print_info(
                        "Go to the port configuration of"
                        f" '{template_switch} 'template"
                    )
                    self.switch_template.select_sw_template(
                        network_policy, template_switch)
                    self.switch_template.go_to_port_configuration()

                    if slot:
                        required_slot = template_switch + "-" + slot
                        self.switch_template.navigate_to_slot_template(required_slot)

                    self.switch_template.click_on_port_details_tab()

                    if revert_mode == "revert_template":
                        self.switch_template.revert_port_configuration_template_level(
                            "Auto-sense Port" if onboarded_switch.cli_type.upper() == "VOSS" else "Access Port")
                    elif revert_mode == "edit_honeycomb_with_empty_path_cost":

                        for port, port_type_config in port_config.items():
                            _, summary = self.device360.edit_stp_settings_in_honeycomb_port_editor(
                                port,
                                port_type_name=port_type_config["port_type_name"],
                                path_cost=""
                            )

                            assert summary["Path Cost"] == "", "Failed to edit the Path Cost"
                            self.utils.print_info("Successfully edited the Path Cost")

                finally:

                    self.utils.wait_till(timeout=5)
                    self.switch_template.switch_template_save()
                    self.utils.wait_till(timeout=10)

                    self.utils.print_info(
                        "Saved the port type configuration, "
                        "now push the changes to the dut")

                    self.devices.update_and_wait_device(
                        policy_name=network_policy,
                        dut=onboarded_switch
                    )

                    for port in port_config:
                        self.cli.verify_path_cost_on_device(
                            onboarded_switch,
                            expected_path_cost=default_path_cost,
                            port=port,
                            mode=stp_mode
                        )

                    for port_info in port_config.values():
                        port_type_name = port_info['port_type_name']
                        try:
                            self.utils.print_info(f"Delete port type profile: {port_type_name}")
                            self.common_objects.delete_port_type_profile(
                                port_type_name)
                        except Exception as exc:
                            self.utils.print_info(repr(exc))

    def check_event(self, event, mac, configuration_event=False, **kwargs):
        """ Method that goes to Device360 -> Events and looks for a given event.
        
        Args:
            event (str): the name of the event
            mac (str): the mac of the device
            configuration_event (bool): the method will click on the Configuration Events tab if this arg is True
        
        Returns: 1 if successful else -1
        """
        self.navigator.navigate_to_device360_page_with_mac(device_mac=mac)
        self.device360.device360_select_events_view()

        try:
            def _check_event():
                self.device360.device360_refresh_page()
                return self.device360.device360_search_event_and_confirm_event_description_contains(
                    event_str=event, configuration_event=configuration_event)
            self.utils.wait_till(_check_event, timeout=30, delay=1)

            kwargs["pass_msg"] = "Successfully found the expected event."
            self.common_validation.passed(**kwargs)
            return 1

        except Exception as e:
            kwargs["fail_msg"] = f"No '{event}' found in Events Tab"
            self.common_validation.failed(**kwargs)
            return -1

        finally:
            close_dialog = self.device360.get_close_dialog()
            self.auto_actions.click(close_dialog)

    def wait_for_logs_after_scli_configuration_update(self, os, spawn, mac, **kwargs):
        """ Method that waits for status logs after a SCLI configuration push in XIQ.
        Also it waits for the status of the configuration update in XIQ.

        Currently this method supports only OS EXOS/VOSS.

        Args:
            event (str): the OS of the device
            spawn (pxssh): the spawn object
            mac (str): the mac of the device
            configuration_event (bool): the method will click on the Configuration Events tab if this arg is True

        Returns: 1 if successful else -1

        Author: Dragos Sofiea, Devi Ranganathan, Raluca Cionca
        """

        if os.lower() not in ["exos", "voss"]:
            kwarg["fail_msg"] = "Failed! OS not supported."
            self.common_validation.failed(**kwargs)
            return -1

        percentage_list = []
        percentage_list.append(21)
        retry = 0

        while retry <= 900:
            
            output = self.cli.send_line_and_wait(spawn, "", 15)
            self.utils.print_info(output)
            
            if output:
            
                if os.lower() == "voss":
                    if 'Send 30 second in-progress report for cli command processing' in output:
            
                        output_commands = re.search(r'Send 30 second in-progress report for cli command processing. Processing \d+ out of \d+ commands', output)
                        output_commands_new = output_commands.group(0)
                        digit = [int(d) for d in output_commands_new.split() if d.isdigit()]
                        self.utils.print_info(" ", digit)
            
                        percentage = self.devices.get_device_updated_status_percentage(device_mac=mac)
                        percentage_list.append(percentage)
            
                        if "Device Update Failed" in percentage_list:
                            kwargs["fail_msg"] = "Device Update Failed"
                            self.common_validation.failed(**kwargs)
                            return -1

                        elif (int(percentage_list[-1]) > 21 and int(percentage_list[-1]) < 100) and (
                                int(percentage_list[-1]) > int(percentage_list[-2])):
                            self.utils.print_info(f"Update status is increasing from {percentage_list[-2]}% to {percentage_list[-1]}%")
            
                        elif int(percentage_list[-1]) == 100:
                            self.utils.print_info("Update configuration is done")
                            break
            
                        elif int(percentage_list[-1]) == int(percentage_list[-2]):
                            self.utils.print_info(f"Still updating {percentage_list[-1]}%. No update status increasing")
            
                        else:
                            kwargs["fail_msg"] = "No update configuration info"
                            self.common_validation.fault(**kwargs)
            
                    elif 'SNMP INFO Save config successful' in output:
            
                        percentage = self.devices.get_device_updated_status_percentage(device_mac=mac)
                        percentage_list.append(percentage)
            
                        if int(percentage_list[-1]) == 100:
                            self.utils.print_info("Update configuration is done")
                            break
                        else:
                            kwargs["fail_msg"] = "No Update configuration is done"
                            self.common_validation.failed(**kwargs)
                            return -1
            
                    elif retry == 500:
            
                        percentage = self.devices.get_device_updated_status_percentage(device_mac=mac)
                        percentage_list.append(percentage)
            
                        if "Device Update Failed" in percentage_list:
                            kwargs["fail_msg"] = "Device Update Failed"
                            self.common_validation.failed(**kwargs)
                            return -1
            
                        elif (int(percentage_list[-1]) > 21 and int(percentage_list[-1]) < 100) and (
                                int(percentage_list[-1]) > int(percentage_list[-2])):
                            self.utils.print_info(f"Update status is increasing from {percentage_list[-2]}% to {percentage_list[-1]}%")
            
                        elif int(percentage_list[-1]) == 100:
                            self.utils.print_info("Update configuration is done")
                            break
            
                        elif int(percentage_list[-1]) == int(percentage_list[-2]):
                            self.utils.print_info(f"Still updating {percentage_list[-1]}%. No update status increasing")
            
                        else:
                            kwargs["fail_msg"] = "No update configuration info"
                            self.common_validation.failed(**kwargs)
                            return -1
            
                    else:
                        self.utils.print_info("No 'Send 30 second in-progress report'")
                        retry += 10

                elif os.lower() == "exos":

                    if '"commandsExec"' in output:

                        output_commands_exec = re.search(r'"commandsExec":\s\d+', output)
                        self.utils.print_info(output_commands_exec)
                        output_commands_exec_new = output_commands_exec.group(0)
                        digit_exec = [int(d) for d in output_commands_exec_new.split() if d.isdigit()]
                        self.utils.print_info(" ", digit_exec)

                        percentage = self.devices.get_device_updated_status_percentage(device_mac=mac)
                        percentage_list.append(percentage)

                        if "Device Update Failed" in percentage_list:
                            kwargs["fail_msg"] = "Device Update Failed"
                            self.common_validation.failed(**kwargs)
                            return -1

                        elif (int(percentage_list[-1]) > 21 and int(percentage_list[-1]) < 100) and (
                                int(percentage_list[-1]) > int(percentage_list[-2])):
                            self.utils.print_info(f"Update status is increasing from {percentage_list[-2]}% to {percentage_list[-1]}%")

                        elif int(percentage_list[-1]) == 100:
                            self.utils.print_info("Update configuration is done")
                            break

                        elif int(percentage_list[-1]) == int(percentage_list[-2]):
                            self.utils.print_info(f"Still updating {percentage_list[-1]}%. No update status increasing")

                        else:
                            kwargs["fail_msg"] = "No update configuration info"
                            self.common_validation.failed(**kwargs)
                            return -1

                    elif retry == 500:

                        percentage = self.devices.get_device_updated_status_percentage(device_mac=mac)
                        percentage_list.append(percentage)

                        if "Device Update Failed" in percentage_list:
                            kwargs["fail_msg"] = "Device Update Failed"
                            self.common_validation.failed(**kwargs)
                            return -1

                        elif (int(percentage_list[-1]) > 21 and int(percentage_list[-1]) < 100) and (
                                int(percentage_list[-1]) > int(percentage_list[-2])):
                            self.utils.print_info(f"Update status is increasing from {percentage_list[-2]}% to {percentage_list[-1]}%")

                        elif int(percentage_list[-1]) == 100:
                            self.utils.print_info("Update configuration is done")
                            break

                        elif int(percentage_list[-1]) == int(percentage_list[-2]):
                            self.utils.print_info(f"Still updating {percentage_list[-1]}%. No update status increasing")

                        else:
                            kwargs["fail_msg"] = "No update configuration info"
                            self.common_validation.failed(**kwargs)
                            return -1

                    elif 'running config saved as startup config' in output:

                        percentage = self.devices.get_device_updated_status_percentage(device_mac=mac)
                        percentage_list.append(percentage)

                        if int(percentage_list[-1]) == 100:
                            self.utils.print_info("Update configuration is done")
                            break
                        else:
                            kwargs["fail_msg"] = "No Update configuration is done"
                            self.common_validation.failed(**kwargs)
                            return -1
                    else:
                        self.utils.print_info("No 'Send 30 second in-progress report'")
                        retry += 10
        
            elif retry == 900:
                kwargs["fail_msg"] = "Timeout exceeded"
                self.common_validation.failed(**kwargs)
                return -1
        
            else:
                self.utils.print_info("No 'Send 30 second in-progress report'")

        kwargs["pass_msg"] = "Successfully found the expected log"
        self.common_validation.passed(**kwargs)
        return 1
