import re
from time import sleep
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.common.AutoActions import AutoActions
from extauto.xiq.flows.common.Navigator import Navigator
from extauto.xiq.elements.DeviceCliAccessElements import DeviceCliAccessElements


class DeviceCliAccess(DeviceCliAccessElements):
    def __init__(self):
        super().__init__()
        self.utils = Utils()
        self.navigator = Navigator()
        self.screen = Screen()
        self.auto_actions = AutoActions()

    def send_cmd_on_device_advanced_cli(self, device_serial="", cmd="show version"):
        """
        - This keyword is used to execute the command on device advanced cli window
        - It will Return the executed command output in str format
        - Flow:
         - Navigate to Manage --> Device --> Select Device --> Actions --> Advanced --> CLi Access
        -  Keyword Usage:
         - ``Send Cmd On Device Advanced Cli   ${DEVICE1_SERIAL}   cmd=${CMD}``

        :param device_serial: device serial number
        :param cmd: cmd to execute on the device advanced cli
        :return:
        - if command is valid return the str format of the command output
        - if command is invalid return -1
        """

        self.utils.print_info("Navigate to the device advanced cli window")
        if self.navigator.navigate_to_device_cli_access(device_serial) == -1:
            self.utils.print_info("Navigation to advanced cli window failed")
            return -1

        self.utils.print_info(f"Send command {cmd} to cli input field")
        self.auto_actions.send_keys(self.get_cli_cmd_input_field(), cmd)

        self.utils.print_info("Click on the cli input apply button")
        self.auto_actions.click_reference(self.get_cli_cmd_input_apply_button)

        if self.get_cli_command_output_error_tool_tip():
            self.utils.print_info(f"check the command:{cmd} it seems invalid command")
            self.utils.print_info(self.get_cli_command_output_error_tool_tip().text)
            self.utils.print_info("closing the cli dialog window")
            self.auto_actions.click_reference(self.get_cli_dialog_window_close_button)
            return -1

        cli_output = self.get_cli_cmd_output_field().text
        self.utils.print_info(f"~~~~~~~~~~~~~~~~~cmd:{cmd}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.utils.print_info(f"{cli_output}")

        self.utils.print_info("closing the cli dialog window")
        self.auto_actions.click_reference(self.get_cli_dialog_window_close_button)
        return cli_output

    def check_cli_output_of_previous_ap_in_current_ap_cli_output(self, device_host_names='', cmd='show hw-info'):
        """
        - This keyword is used to validate the CFD-4322
        - To check The CLI Access output for the previous AP is displayed for the current AP if the Apply button is clicked too quickly
        - Keyword Usage:
         - Check Clo Output Of Previous Ap In Current Ap Cli Output   device_serials=${AP1_SERIAL},${AP2_SERIAL}``

        :param device_host_names: comma separated host names of the devices to select device rows
        :param cmd: cmd to execute
        :return: returns 1 if successful
        """
        self.utils.print_info("Navigate to the device advanced cli window")
        self.navigator.navigate_to_device_cli_access(device_host_names)

        self.utils.print_info("Select the first device")
        self.auto_actions.select_drop_down_options(self.get_cli_device_access_list(), device_host_names.split(',')[0])

        self.utils.print_info(f"Send command {cmd} to cli input field")
        self.auto_actions.send_keys(self.get_cli_cmd_input_field(), cmd)

        self.utils.print_info("Click on the cli input apply button")
        self.auto_actions.click_reference(self.get_cli_cmd_input_apply_button)

        self.utils.print_info("Select the second  device")
        self.auto_actions.select_drop_down_options(self.get_cli_device_access_list(), device_host_names.split(',')[1])

        self.utils.print_info("Check the output on second device cli output field")
        if self.get_cli_cmd_output_field():
            self.utils.print_info(f"second device output field:")
            self.utils.print_info(self.get_cli_cmd_output_field().text)
            self.utils.print_info("first device output appearing on second device output field")
            return -1

        self.utils.print_info("Select the first device")
        self.auto_actions.select_drop_down_options(self.get_cli_device_access_list(), device_host_names.split(',')[0])

        self.utils.print_info("Check the output on first device cli output field")
        first_dev_cli_output = self.get_cli_cmd_output_field().text

        if first_dev_cli_output:
            self.utils.print_info(f"first device cli output:{first_dev_cli_output}")
            self.utils.print_info("closing the cli dialog window")
            self.auto_actions.click_reference(self.get_cli_dialog_window_close_button)
            return 1
        return -1

    def verify_command(self, ui_output="default", cli_output="default", cmd="default"):
        """
             - This keyword  verifies whether UI output and CLI output match.
             - Keyword Usage:
              - ``${RESULT}=        Verify UI Command         ${UI_OUTPUT}      ${CLI_OUTPUT}       ${CMD}  ``
             :param ui_output: output of command in UI
             :param cli_output: output of command in cli
             :param cmd: command that is executed
             :return: returns 1 if successful
             """
        try:
            if ui_output != "default" and cli_output != "default":
                ui_output = ui_output.strip()
                ui_output = re.sub("Uptime.*", "", ui_output)
                ui_output = re.sub("\nRx packets.*", "", ui_output)
                ui_output = re.sub("\nTx packets.*", "", ui_output)
                ui_output = re.sub("\nRx bytes.*", "", ui_output)
                ui_output = re.sub("\nRx airtime.*", "", ui_output)
                ui_output = re.sub("\nTx range.*", "", ui_output)
                ui_output = re.sub("--+", "", ui_output)
                ui_output = re.sub("  *", "", ui_output)
                ui_output = ui_output.strip()
                ui_output = ui_output.splitlines()
                if len(ui_output) > 5:
                    ui_output = ui_output[0:5]
                self.utils.print_info("UI Output List of command ", cmd, " : ", ui_output)

                cli_output = str(cli_output)
                cli_output = cli_output.strip()
                cli_output = re.sub("Uptime.*", "", cli_output)
                cli_output = re.sub("\nRx packets.*", "", cli_output)
                cli_output = re.sub("\nTx packets.*", "", cli_output)
                cli_output = re.sub("\nRx bytes.*", "", cli_output)
                cli_output = re.sub("\nRx airtime.*", "", cli_output)
                cli_output = re.sub("--+", "", cli_output)
                cli_output = re.sub("  *", "", cli_output)
                self.utils.print_info("CLI output:  ", cli_output)
                for ui_op in ui_output:
                    if ui_op not in cli_output:
                        self.utils.print_info("UI and CLI output does not match")
                        return -1
                self.utils.print_info("UI and CLI output match")
                return 1
        except Exception as e:
            self.utils.print_info("Unable to verify ", cmd, " exception: ", e)
            return -1

    def ap_operating_channel(self, cli_op):
        """
            - Verifing the Ap Operating channel
            - Keyword Usage:
                =>  ${channel}=     Ap Operating Channel     ${cli_output}

        Note : before executing this method, we have to get the AP interface details like below
                =>  ${cli_output}=		Send		${SPAWN}    sho interface | in Wifi1.1

            :param cli_op: get the channel information from send command
            :return: will return the current operating channel if AP is UP,
                        else return -1 """

        if cli_op.find(" U ") != -1:
            self.utils.print_info("AP is up now, checking the operation channel")
            channel = str(cli_op.split("(")[0].split()[-1])
            self.utils.print_info("Ap Operating channel is ::  ", channel)
            return channel
        self.utils.print_info("AP is not UP, please check the AP status ")
        return -1
