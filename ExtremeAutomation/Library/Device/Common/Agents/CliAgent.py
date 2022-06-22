import re
import abc
import time
from ExtremeAutomation.Library.Device.Common.Agents.LoginManagementAgent import LoginManagementAgent
from ExtremeAutomation.Keywords.Utils.GlobalVariableCache import GlobalVariableCache, GlobalVariableCacheConstants
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants \
    import EndsystemElementConstants


class CliAgent(LoginManagementAgent, metaclass=abc.ABCMeta):
    def __init__(self, device):
        super(CliAgent, self).__init__(device)
        self.prompt_snapshot = ""
        self.variable_cache = GlobalVariableCache()
        self.eol = "\n"

    @abc.abstractmethod
    def login(self):
        """
        This function should log the CLI agent into the given device.
        """
        pass

    @abc.abstractmethod
    def write(self, text):
        """
        This function should write the given text to the CliAgent session.
        """
        pass

    @abc.abstractmethod
    def read_until(self, text):
        """
        This function should read data from the device until the provided text is found.
        """
        pass

    @abc.abstractmethod
    def read_until_list_match(self, _list):
        """
        This function should read data from the device until one of the strings in the list is found.
        """
        pass

    @abc.abstractmethod
    def wait_no_parse(self, ms, retries):
        """
        This function should read for data from the device for <ms> * <retries> milliseconds.
        """
        pass

    @abc.abstractmethod
    def disconnect(self):
        """
        This function attempts to log out of the device before closing the connection.
        """
        if self.connected:
            if self.device.oper_sys == NetworkElementConstants.OS_ALPHA:
                self.write("logout")
                output = self.wait_no_parse(100, 10)
            elif self.device.oper_sys == NetworkElementConstants.OS_VOSS:
                self.write("exit" + self.eol)
                output = self.wait_no_parse(100, 10)
            else:
                self.write("exit")
                output = self.wait_no_parse(100, 10)

            if output is not None:
                if "y/n" in output.lower():
                    self.write("n")
                    self.wait_no_parse(100, 10)

    @abc.abstractmethod
    def logout(self):
        """
        This function should log out of the given device.
        """
        pass

    def write_encode(self, text):
        """
        Function Args:
        [text] - The text that should be encoded before writing to the current agent.

        Writes encoded text to the current agent.
        """
        return self.write(self.cmd_encode(text))

    def write_encode_ln(self, text):
        """
        Function Args:
        [text] - The text that should be sent to the current agent. This text will be encoded before sending.

        Writes the encoded text plus the end of line character to the current agent.
        """
        return self.write(self.cmd_encode(text) + self.eol)

    def send_command_object(self, cmd_obj, **kwargs):
        """
        Function Args:
        [cmd_obj] - An instance of CliCommandObject.

        Sends the information within the command object to the device.
        """
        cmd_obj.clear_error_state()

        retries = 0
        max_retries = 3

        while retries < max_retries:
            retries += 1
            try:
                if not self.connected:
                    self.login()
                cmd_obj.start_time = time.time()
                prompt_success, prompt_error = self.device.prompt_handler.change_prompt(cmd_obj.prompt,
                                                                                        cmd_obj.prompt_args)
                if prompt_success:
                    commands = cmd_obj.command.split("||")
                    output_list = []

                    if cmd_obj.confirmation_args:
                        conf_phrase_list = cmd_obj.confirmation_phrases.split("||")
                        conf_arg_list = cmd_obj.confirmation_args.split("||")

                        if len(conf_arg_list) == len(conf_phrase_list):
                            for command in commands:
                                output, index = self.send_command_wait_for_confirmation(command, conf_phrase_list)
                                self.logger.log_info("Command: " + command)
                                self.logger.log_info(output)
                                output_list.append(output)

                                while index is not None:
                                    confirm_cmd = conf_arg_list[index]
                                    self.logger.log_debug("Confirmation arg is: " + confirm_cmd)

                                    conf_phrase_list.pop(index)
                                    conf_arg_list.pop(index)

                                    if self.device.wait_for_prompt:
                                        reply, index = self.send_command_wait_for_confirmation(confirm_cmd,
                                                                                               conf_phrase_list)
                                    else:
                                        reply, index = \
                                            self.send_command_wait_for_confirmation_or_quiet(confirm_cmd,
                                                                                             conf_phrase_list)

                                    retries = 0
                                    while (not reply or reply.strip() == command) and retries < 3:
                                        reply += self.wait_until_quiet()
                                        retries += 1
                                    output_list.append(reply)
                                    self.logger.log_info(reply)
                        else:
                            raise ValueError("Error: confirmation arg list and confirmation "
                                             "phrase list must be the same length.")
                    else:
                        for command in commands:
                            if self.device.wait_for_prompt:
                                reply = self.send_command_wait_for_prompt(command)
                            else:
                                reply = self.send_command_wait_for_quiet(command)

                            retries = 0
                            while (not reply or reply.strip() == command) and retries < 3:
                                reply += self.wait_until_quiet()
                                retries += 1
                            output_list.append(reply)
                            self.logger.log_info("Command: " + command)
                            self.logger.log_info("Output : " + reply.replace("\r\r", "\r"))

                    cmd_obj.return_text = "||".join(output_list)

                    if self.device.error_checker is not None:
                        errs = self.device.error_checker.check_for_errors(cmd_obj.return_text)
                        if errs is not None:
                            if len(errs) > 0:
                                cmd_obj.set_error_state(errs)
                    cmd_obj.end_time = time.time()
                    return cmd_obj
                else:
                    # An error was encountered while changing prompts.
                    if prompt_error == "":
                        prompt_error = "Error when changing prompt"
                    cmd_obj.set_error_state(prompt_error)
                    return cmd_obj
            except Exception as ex:
                self.logger.log_debug(ex)
                self.logger.log_debug("Error: " + str(ex.args))
                if any(x in str(ex.args) for x in ["closed", "reset", "peer", "pipe"]) or isinstance(ex, EOFError):
                    self.disconnect()
                else:
                    cmd_obj.return_text = str(ex.args)
                    cmd_obj.set_error_state(str(ex.args))
                    return cmd_obj
        cmd_obj.set_error_state("Max connect retries exhausted!")
        return cmd_obj

    def wait_until_quiet(self, timeout=None):
        """
        Function Args:
        [timeout] - The timeout in milliseconds. If no timeout is provided DEFAULT_SLEEP_BETWEEN_COMMANDS_MS
                    will be used.

        Reads from the session for timeout MS.
        """
        start = time.time()
        return_string = ""

        if timeout is None:
            timeout = self.default_sleep_between_commands / 1000.0
        else:
            timeout = timeout / 1000.0

        while (time.time() - start) < timeout:
            reply = self.wait_no_parse(self.wait_for_sleep, self.wait_for_retries)
            if reply:
                return_string += reply
        return return_string

    def wait_for_confirmation_or_prompt(self, command, prompt_list, timeout):
        """
        Function Args:
        [prompt_list] - A list of prompt to search for in the data returned from the CLI.
        [timeout] - The amount of time in MS to wait before stopping the prompt search.

        This function will retrieve data from the device CLI until it finds a prompt match or timeout MS have passed.
        At that point it will return, if no prompt was matches the returned index will be None. Otherwise it will
        be the index of the matching prompt in <prompt_list>.
        """
        start = time.time()
        found = False
        return_string = ""
        index = None
        reply = self.wait_no_parse(self.wait_for_sleep, self.wait_for_retries)
        if reply:
            return_string += self.strip_command_from_output(command, reply)
        while not found and (time.time() - start) < timeout / 1000.0:
            reply = self.wait_no_parse(self.wait_for_sleep, self.wait_for_retries)
            if reply:
                return_string += reply
                start = time.time()

            for i, prompt in enumerate(prompt_list):
                if prompt in return_string.strip():
                    found = True
                    index = i
                    break
        return return_string, index

    def wait_for_regex_prompt_or_quiet(self, prompt_regex, timeout, strip_eol=True):
        """
        Function Args:
        [prompt_regex] - The regex of the prompt to search for.
        [timeout] - How long to search for the prompt before returning.
        [strip_eol] - Boolean that indicating whether or not end of line chars should be removed.

        This will pull output off the buffer until the prompt is found.
        The prompt match is a regular expression
        """
        start = time.time()
        found = False
        comp_re = re.compile(prompt_regex)
        return_string = ""

        while not found and (time.time() - start) < timeout / 1000.0:
            reply = self.wait_no_parse(self.wait_for_sleep, self.wait_for_retries)

            if reply:
                return_string += reply

            if strip_eol:
                found = comp_re.search(return_string.strip())
            else:
                found = comp_re.search(return_string)
        return return_string

    def wait_for_prompt(self):
        """
        This method will will read CLI output until either a prompt regex is matched or the timeout is exceeded.
        Any data read during this time will be returned.
        """
        prompt_list = self.__get_prompt_regex()

        if self.wait_for_retries == 0:
            self.wait_for_retries = 10

        timeout = int(self.variable_cache.get_global_value(GlobalVariableCacheConstants.DEBUG_VALUE_CLI_TIME_OUT,
                                                           60000))

        start = time.time()
        found = False
        return_string = ""

        while not found and (time.time() - start) < timeout / 1000.0:
            reply = self.wait_no_parse(self.constants.WAIT_FOR_SLEEP, self.constants.WAIT_FOR_RETRIES)
            if reply:
                return_string += reply
            for prompt_re in prompt_list:
                found = prompt_re.search(return_string)
                if found:
                    break
        self.read_until("")
        return return_string

    def send_command(self, commands):
        """
        Function Args:
        [commands] - A list of commands to send to the device.

        This function will send each of the commands in <commands> to the device.
        """
        if not isinstance(commands, list):
            commands = [commands]
        self.debug_print("Sending command(s): [" + ", ".join(commands) + "]")

        output = ""

        for command in commands:
            self.write_encode_ln(command)
            return_string = self.read_until(self.device.main_prompt)
            output += self.strip_command_from_output(command, return_string)
            time.sleep(self.default_sleep_between_commands / 1000)
        return output

    def send_command_wait_for_quiet(self, commands):
        """
        Function Args:
        [commands] - A list of commands to send to the device.

        This function will send each of the commands in <commands> to the device. It will wait until no data
        is returned from the device before returning.
        """
        if not isinstance(commands, list):
            commands = [commands]
        self.debug_print("Sending command(s): [" + ", ".join(commands) + "]")

        output = ""

        for command in commands:
            self.write_encode_ln(command)
            return_string = self.wait_until_quiet(self.default_sleep_between_commands)
            output += self.strip_command_from_output(command, return_string)
        return output

    def send_command_wait_for_prompt(self, commands, **kwargs):
        """
        Function Args:
        [commands] - Either a string or list of commands to send to the device.

        This function will send command(s) to the device and wait for the prompt between each sent command.
        """
        return_output = ""

        if kwargs.get("take_snapshot", False):
            self.take_prompt_snapshot()
            self.debug_print("Sending Command (with wait for prompt: " + self.prompt_snapshot + ") [" + commands + "]")

        if not isinstance(commands, list):
            commands = [commands]

        for command in commands:
            self.write_encode_ln(command)
            cmd_len = len(command)

            # Not sure what this is for.
            #
            # Old comment:
            # if you are going from user to debug or debug to user, you need to change the prompt.
            # otherwise the wait for prompt doesn't work.
            if (command.startswith("dbg") and (cmd_len == 3 or cmd_len == 13) or
                    (self.prompt_snapshot == "admin" and command == "exit")):
                self.wait_no_parse(100, 1)
                self.write("\r\n")
                self.take_prompt_snapshot(force_snapshot=True)
            output = self.wait_for_prompt()
            if command not in output:
                output += self.wait_until_quiet(500)
            return_output += self.strip_command_from_output(command, output)
        return return_output

    def send_command_wait_for_confirmation(self, command, conf_phrases):
        """
        Function Args:
        [command] - The command that should be sent to the device.
        [conf_phrases] - A list of confirmation phrases to search for. This can also be a string with a
                         single phrase.

        This function sends a command and then waits for a given confirmation phrase to be seen. It also checks for
        the prompt. If the prompt is seen index=None is returned indicating that the expected confirmation phrase
        was not seen.
        """
        if not isinstance(conf_phrases, list):
            conf_phrases = [conf_phrases]
        else:
            # This is needed so that conf_phrases is a new list. Otherwise the list in this function
            # the caller will be synced.
            conf_phrases = list(conf_phrases)

        if self.prompt_snapshot == "" or self.prompt_snapshot is None:
            self.take_prompt_snapshot()

        conf_phrases.append(self.prompt_snapshot)

        self.debug_print("Sending Command: [" + command + "]")

        self.write_encode_ln(command)
        output, index = self.wait_for_confirmation_or_prompt(command, conf_phrases, 600000)
        if index == len(conf_phrases) - 1:
            index = None

        return output, index

    def send_command_wait_for_confirmation_or_quiet(self, command, conf_phrases):
        """
        Function Args:
        [command] - The command to send to the device.
        [conf_phrase] - A string that should be returned after sending the command to the device.

        This function sends a command and expects a non-prompt response from the device. This function returns
        the output and  the index of the phrase that matched. This index is used to send the correct data
        in response.
        """
        if not isinstance(conf_phrases, list):
            conf_phrases = [conf_phrases]

        self.debug_print("Sending Commnad: [" + ", ".join(command) + "]")

        if self.device.oper_sys == NetworkElementConstants.OS_ALPHA:
            self.write_encode(command)
        else:
            self.write_encode_ln(command)
        output, index = self.wait_for_confirmation_or_prompt(command, conf_phrases, self.default_sleep_between_commands)

        return output, index

    def take_prompt_snapshot(self, force_snapshot=False):
        """
        Function Args:
        force_snapshot - Normally this function only takes a snapshot if no snapshot is present. This
                         flag forces the function to take a new snapshot. Defaulted to False.

        This function creates a regex string of the device's current prompt. This is used later to determine
        whether or not the prompt was returned after issuing a command. Regex is used because the prompt can
        change between commands.
        """
        output = self.prompt_snapshot

        if self.prompt_snapshot == "" or self.prompt_snapshot is None or force_snapshot:
            self.debug_print("Taking snapshot of prompt...")

            if self.device.oper_sys in [NetworkElementConstants.OS_LINUX,
                                        NetworkElementConstants.OS_SNAP_ROUTE]:
                prompt_list = ["#", "$"]
            elif self.device.oper_sys == NetworkElementConstants.OS_AHFASTPATH:
                prompt_list = ["#",">"]
            else:
                prompt_list = [self.device.main_prompt]

            self.write_encode_ln("")
            output = self.read_until_list_match(prompt_list).splitlines()[-1]
            output = output.replace("\r", "").replace("\n", "")

            if self.device.oper_sys in [NetworkElementConstants.OS_LINUX,
                                        NetworkElementConstants.OS_SNAP_ROUTE]:
                if ":" in output:
                    output = output.split(":")[0]
                output = self.remove_control_characters(output)

                if "@" in output:
                    output = output.split("@")[1]
                    output = output.replace("$", "").replace("#", "").replace("~", "").replace(" ", "")
            elif self.device.oper_sys in [NetworkElementConstants.OS_EXTR_WIRELESS]:
                output = output.replace(self.device.main_prompt, "").strip()
            elif self.device.oper_sys in [NetworkElementConstants.OS_EXOS]:
                if "." in output:
                    output = output.split(".")[0]
                    output = output.replace("*", "")
            elif self.device.oper_sys in [NetworkElementConstants.OS_EOS,
                                          NetworkElementConstants.OS_EOS_STACKS]:
                output = output.split("(")[0]
            elif self.device.oper_sys in [NetworkElementConstants.OS_VOSS]:
                output = output.split(":")[0]
            elif self.device.oper_sys in [NetworkElementConstants.OS_ALPHA]:
                output = output.split(")")[0] + ")"
            elif self.device.oper_sys in [NetworkElementConstants.OS_BOSS,
                                          NetworkElementConstants.OS_ICX,
                                          NetworkElementConstants.OS_MLX,
                                          NetworkElementConstants.OS_VDX,
                                          NetworkElementConstants.OS_SLX]:
                output = output.split("#")[0]
            self.prompt_snapshot = output.strip()

            self.debug_print("Prompt was set to: " + self.prompt_snapshot)
        return output.strip()

    @staticmethod
    def strip_command_from_output(cmd, output):
        """
        Function Args:
        [cmd] - The command that should be removed.
        [output] - The data to remove the command from.

        This function will check <output> for the <cmd> issued. If it is found it will be removed
        otherwise the output is returned untouched.
        """
        output_split = output.splitlines(True)

        if len(output_split) == 0:
            return output
        elif cmd in output_split[0]:
            output_split[0] = output_split[0].replace(cmd, "")
            return "".join(output_split)
        return output

    def __get_prompt_regex(self):
        """
        This function will return a list of compiled regex strings.

        The regex strings may need different formatting depending on the device's operating system.
        """
        prompt_re = ".*" + self.prompt_snapshot + ".*" + self.device.main_prompt + ".*"
        try:
            prompt_list = \
                [re.compile(prompt_re.replace("[", r"\[").replace("]", r"\]").replace("(", "[(]").replace(")", "[)]"))]
        except Exception as e:
            print("Unable to get default prompt value: " +str(e))

        # OS based exceptions.
        if self.device.oper_sys in [NetworkElementConstants.OS_LINUX,
                                    NetworkElementConstants.OS_SNAP_ROUTE,
                                    EndsystemElementConstants.OS_LINUX_MU]:
            prompt_re1 = ".*" + self.prompt_snapshot + ".*$"
            prompt_re1 = re.compile(prompt_re1.replace("[", r"\[").replace("]", r"\]"))
            prompt_re2 = ".*" + self.prompt_snapshot + ".*#"
            prompt_re2 = re.compile(prompt_re2.replace("[", r"\[").replace("]", r"\]"))
            prompt_list = [prompt_re1, prompt_re2]
        elif self.device.oper_sys in [EndsystemElementConstants.OS_WINDOWS]:
            prompt_re1 = self.prompt_snapshot + ".$"
            prompt_re1 = prompt_re1.replace("\\", "\\\\")
            prompt_list = [re.compile(prompt_re1, re.IGNORECASE)]
        elif self.device.oper_sys in [EndsystemElementConstants.OS_MAC_MU]:
            prompt_re1 = ".#"
            prompt_list = [re.compile(prompt_re1, re.IGNORECASE)]
        elif self.device.oper_sys in [EndsystemElementConstants.OS_WINDOWS_MU]:
            prompt_re1 = ".>"
            prompt_list = [re.compile(prompt_re1, re.IGNORECASE)]
        elif self.device.oper_sys in [EndsystemElementConstants.OS_A3]:
            prompt_re1 = ".$"
            prompt_list = [re.compile(prompt_re1, re.IGNORECASE)]
        elif self.device.oper_sys in [NetworkElementConstants.OS_AHAP,
                                      NetworkElementConstants.OS_AHFASTPATH,
                                      NetworkElementConstants.OS_WING]:
            prompt_re1 = ".*" + self.prompt_snapshot + ".*"
            prompt_list = [re.compile(prompt_re1, re.IGNORECASE)]

        return prompt_list

    @staticmethod
    def cmd_encode(text):
        """
        Function Args:
        [text] - The text to encode.

        Checks the string for control characters and replace them as needed.
        """
        # http://nemesis.lonestar.org/reference/telecom/codes/ascii.html
        if text and "^" in text:
            text = text.replace("^DEL", chr(0x7F))
            text = text.replace("^A", chr(0x01))
            text = text.replace("^B", chr(0x02))
            text = text.replace("^C", chr(0x03))
            text = text.replace("^D", chr(0x04))
            text = text.replace("^E", chr(0x05))
            text = text.replace("^F", chr(0x06))
            text = text.replace("^G", chr(0x07))
            text = text.replace("^H", chr(0x08))
            text = text.replace("^I", chr(0x09))
            text = text.replace("^J", chr(0x0A))
            text = text.replace("^K", chr(0x0B))
            text = text.replace("^L", chr(0x0C))
            text = text.replace("^M", chr(0x0D))
            text = text.replace("^N", chr(0x0E))
            text = text.replace("^O", chr(0x0F))
            text = text.replace("^P", chr(0x10))
            text = text.replace("^Q", chr(0x11))
            text = text.replace("^R", chr(0x12))
            text = text.replace("^S", chr(0x13))
            text = text.replace("^T", chr(0x14))
            text = text.replace("^U", chr(0x15))
            text = text.replace("^V", chr(0x16))
            text = text.replace("^W", chr(0x17))
            text = text.replace("^X", chr(0x18))
            text = text.replace("^Y", chr(0x19))
            text = text.replace("^Z", chr(0x1A))
            text = text.replace("^[", chr(0x1B))
            text = text.replace("^\\", chr(0x1C))
            text = text.replace("^]", chr(0x1D))
            text = text.replace("^^", chr(0x1E))
            text = text.replace("^_", chr(0x1F))
        return text

    @staticmethod
    def remove_control_characters(output):
        """
        Function Args:
        [output] - The output that control chars should be removed from.

        Removes all control characters from the provided output.
        """
        c = ["[m", "[1m", "\133", "\135", " \176", "\176"]
        for i in c:
            output = output.replace(i, "")
        output = re.sub(r'[^a-zA-Z0-9@-]', r'', output)
        output = output.replace(' ', '')
        return output
