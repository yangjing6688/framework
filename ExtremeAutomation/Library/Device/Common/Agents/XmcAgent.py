from ExtremeAutomation.Library.Device.Common.Agents.RestAgent import RestAgent
import requests
import time


class XmcAgent(RestAgent):
    def __init__(self, device):
        super(XmcAgent, self).__init__(device)
        self.type = self.constants.TYPE_XMC_REST

    def send_command_object(self, cmd_obj, **kwargs):
        """
        Main looping function to continuously poll the Rest Server for errors and
        step completed flags, while logging any data updated on the Rest server.
        If the error flag is True, we mark it as a fail and print all the logs and
        then clear them all.
        If the step completed flag is observed to be True. The step properly passed
        We print all the data remaining in the logs and then clear the logs
        """
        error_flag = False
        cmd_obj = super(XmcAgent, self).send_command_object(cmd_obj, **kwargs)
        d = '/robot/v1/'
        uri = [e + d for e in cmd_obj.full_uri.split(d) if e]
        base_uri = uri[0]
        time_end = time.time() + 60 * 60

        while time.time() < time_end and not error_flag:
            error = requests.get(base_uri + 'read_error_log')
            if error.text == "False" or error.text == "log_empty":
                output = requests.get(base_uri + 'read_step_completed_log')
                if output.text == "True":
                    log_output = requests.get(base_uri + 'read_log')
                    while log_output.text != "log_empty":
                        log_output = requests.get(base_uri + 'read_log')
                        if log_output.text != "log_empty":
                            self.log_output_text(log_output)
                    log_output = requests.get(base_uri + 'read_entire_log')
                    if log_output.text != "log_empty":
                        self.print_complete_log_output(log_output)
                    self.clear_logs(base_uri)
                    return cmd_obj
                log_output = requests.get(base_uri + 'read_log')
                if log_output.text != 'log_empty':
                    self.log_output_text(log_output)
                    time.sleep(2)
                else:
                    time.sleep(2)
            else:
                error_flag = True

        cmd_obj.error_state = True
        log_output = requests.get(base_uri + 'read_entire_log')
        cmd_obj.error_text = log_output.text
        self.logger.log_info("log read_entire_log error")
        self.logger.log_info(log_output.text)
        log_output = requests.get(base_uri + 'read_error_log')
        self.logger.log_info("log read_error_log")
        self.logger.log_info(log_output.text)
        log_output = requests.get(base_uri + 'read_step_completed_log')
        self.logger.log_info("log read_step_completed_log")
        self.logger.log_info(log_output.text)
        self.clear_logs(base_uri)
        return cmd_obj

    def log_output_text(self, log_output):
        """
        Logs just the output text of the kw run
        """
        end_char = len(log_output.text) + 10
        equal_length = len(log_output.text) // 2
        equal_string = "=" * equal_length
        equal_end = "=" * end_char
        self.logger.log_info(equal_end)
        self.logger.log_info(equal_string + " Log Output " + equal_string)
        self.logger.log_info(log_output.text)
        self.logger.log_info(equal_end)

    def print_complete_log_output(self, log_output):
        """
        Logs the entire REST log
        """
        new_output = log_output.text.split(',')
        max_output = len(max(new_output, key=len))
        equal_end = "=" * max_output
        equal_length = (max_output - 20) // 2
        equal_string = equal_length * "="
        self.logger.log_info(equal_end)
        self.logger.log_info(equal_string + " Complete Log Output " + equal_string)
        self.logger.log_info(log_output.text)
        self.logger.log_info(equal_end)

    def clear_logs(self, base_uri):
        """
        Clears all REST server logs to start again
        """
        log_output = requests.get(base_uri + 'clear_entire_log')
        if log_output.text != "log_empty":
            self.logger.log_info("=============================")
            self.logger.log_info("    LOGS were not cleared    ")
            self.logger.log_info("=============================")
        else:
            self.logger.log_info("========================")
            self.logger.log_info("    All Logs Cleared    ")
            self.logger.log_info("========================")
