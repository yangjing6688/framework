import time
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Library.Utils.CloudConnect.CloudConnectResponse import CcConnectResponse, CcUpgradeResponse, \
    CcStatsResponse, CcConfigResponse


class CloudConnectRoutes(object):
    def __init__(self):
        self.connect_dict = {}
        self.upgrade_dict = {"current": {}}
        self.config_dict = {"merge": {},
                            "originals": {}}
        self.stats_reply = {"serials": {}}
        self.allow_timeout = {"connect_timeout": [],
                              "upgrade_timeout": [],
                              "config_timeout": []}
        self.device_states = {}
        self.logger = Logger()

########################################################################################################################
#   Server Route Functions   ###########################################################################################
########################################################################################################################
    def connect(self, serial):
        """
        Checks for a Connect entry for the device serial.

        Returns the Connect reply if found.
        """
        # If the serial has an entry in connect_dict, append to the device_states list. Otherwise overwrite it.
        if serial in self.device_states and serial in self.connect_dict:
            if len(self.device_states[serial]) >= 10:
                self.device_states[serial] = self.device_states[serial][1:]
            self.device_states[serial].append("CONNECT")
        else:
            self.device_states[serial] = ["CONNECT"]
        self.logger.log_info("Device " + serial + " states - " + str(self.device_states[serial]))

        # Check the allow_timeout for <serial> and wait for timeout if present.
        if serial in self.allow_timeout["connect_timeout"]:
            self.logger.log_info("Waiting for Connect to timeout.")
            self.allow_timeout["connect_timeout"].remove(serial)
            time.sleep(35)

        try:
            reply = self.connect_dict[serial]
            self.logger.log_info("Sending connect response to client with action: " +
                                 str(reply.action))
            return reply.send()
        except KeyError:
            self.logger.log_info("Device serial was not found in connect_dict.")
            return False
        except TypeError:
            self.logger.log_info("CcConnectResponse object was not callable!")
            return False

    def image_upgrade(self, serial, upgrade_dict):
        """
        Checks for an Upgrade entry for the device serial.

        Returns the Upgrade reply if found.
        """
        self.upgrade_dict["current"][serial] = upgrade_dict

        # If the serial has an entry in connect_dict, append to the device_states list. Otherwise overwrite it.
        if serial in self.device_states and serial in self.connect_dict:
            if len(self.device_states[serial]) >= 10:
                self.device_states[serial] = self.device_states[serial][1:]
            self.device_states[serial].append("UPGRADE")
        else:
            self.device_states[serial] = ["UPGRADE"]
        self.logger.log_info("Device " + serial + " states - " + str(self.device_states[serial]))

        # Check the allow_timeout for <serial> and wait for timeout if present.
        if serial in self.allow_timeout["upgrade_timeout"]:
            self.logger.log_info("Waiting for Upgrade to timeout.")
            self.allow_timeout["upgrade_timeout"].remove(serial)
            time.sleep(35)

        try:
            reply = {"imageUpgradeBlock": self.upgrade_dict[serial]}
            self.logger.log_info("Sending: " + str(reply))
            return reply
        except KeyError:
            self.logger.log_info("Device " + serial + " not found in upgrade_dict!")
            return False

    def configuration(self, serial, sw_config):
        """
        Checks for a Configuration entry for the device serial.

        Returns the Config reply if found.
        """
        # If the serial has an entry in connect_dict, append to the device_states list. Otherwise overwrite it.
        self.logger.log_debug(str(sw_config))
        if serial in self.device_states and serial in self.connect_dict:
            if len(self.device_states[serial]) >= 10:
                self.device_states[serial] = self.device_states[serial][1:]
            self.device_states[serial].append("CONFIG")
        else:
            self.device_states[serial] = ["CONFIG"]
        self.logger.log_info("Device " + serial + " states - " + str(self.device_states[serial]))

        # Check the allow_timeout for <serial> and wait for timeout if present.
        if serial in self.allow_timeout["config_timeout"]:
            self.logger.log_info("Waiting for Configuration to timeout.")
            self.allow_timeout["config_timeout"].remove(serial)
            time.sleep(35)

        if serial in self.config_dict:
            config_orig = {"configBlock": sw_config["configBlock"]}
            self.config_dict["originals"][serial] = config_orig
            config_new = self.config_dict[serial]

            reply = CcConfigResponse(config_orig, config_new).send(self.config_dict["merge"][serial])

            self.logger.log_info("Sending: " + str(reply))
            return reply
        return False

    def event_notify(self, serial, event_dict):
        """Logs the events found in the Event dictionary."""
        self.logger.log_info("Received EVENT from " + str(serial))
        if "configAck" in event_dict:
            if event_dict["configAck"]["status"] == "ok":
                self.logger.log_info("Received EVENT - Configuration OK!")

        self.logger.log_info([event for event in event_dict])
        if "event" in event_dict:
            self.logger.log_info(event_dict["event"])
            # self.check_for_failed_download(serial, event_dict["event"])
        return True

    def stats_notify(self, serial, stats_dict):
        """
        Checks for a Stats entry for the device serial.

        Returns the Stats reply if found.
        """
        # If the serial has an entry in connect_dict, append to the device_states list. Otherwise overwrite it.
        if serial in self.device_states and serial in self.connect_dict:
            if self.device_states[serial][-1] != "RUNNING":
                if len(self.device_states[serial]) >= 10:
                    self.device_states[serial] = self.device_states[serial][1:]
                self.device_states[serial].append("RUNNING")
        else:
            self.device_states[serial] = ["RUNNING"]
        self.logger.log_info("Device " + serial + " states - " + str(self.device_states[serial]))

        # self.logger.log_info([stat for stat in stats_dict])
        if serial in self.stats_reply["serials"]:
            action = self.stats_reply["serials"][serial].get("action", "NONE")
            if action == "IMAGE_UPGRADE":
                self.stats_reply["serials"][serial]["upgrade"] = {"imageUpgradeBlock": self.upgrade_dict[serial]}

            if action == "CONFIGURATION":
                try:
                    config_orig = {"configBlock": self.config_dict["originals"][serial]["configBlock"]}
                except KeyError:
                    config_orig = {"configBlock": {}}
                config_new = self.config_dict[serial]
                self.stats_reply["serials"][serial]["config"] = \
                    CcConfigResponse(config_orig, config_new).send(self.config_dict["merge"][serial])

            reply = CcStatsResponse(self.stats_reply["serials"][serial]).send()
            self.logger.log_info("Sending: " + str(reply))
            # self.stats_reply["serials"].pop(serial)
            # self.logger.log_info("Sending: " + str(reply))
            return reply
        return False

########################################################################################################################
#   Configuration Routes   #############################################################################################
########################################################################################################################
    def configure_timeout(self, json_dict):
        """Configures the CCS to ignore requests from the given device serial."""
        if "allow_timeout" in json_dict:
            for serial in json_dict["allow_timeout"]:
                for timeout in serial:
                    try:
                        self.allow_timeout[timeout].append(serial)
                        self.logger.log_info("Setting allow_timeout for " + str(timeout) + " state.")
                    except KeyError:
                        self.logger.log_info("ERROR - Received invalid timeout type: " + str(timeout) + "!")
                        return False
        return True

    def configure_connect(self, json_dict):
        """Configures the Connect entry for the given device serial."""
        if "serial" in json_dict:
            connect_response_obj = CcConnectResponse()
            try:
                connect_response_obj.action = json_dict["action"]
                connect_response_obj.standby_timeout = json_dict["standby_timeout"]
                connect_response_obj.login = str(json_dict["login"])
                connect_response_obj.password = str(json_dict["password"])
            except KeyError as e:
                self.logger.log_info("Required connect attribute is missing:\n" + repr(e))
                return False
            try:
                connect_response_obj.redirect_type = json_dict["redirect_type"]
                connect_response_obj.redirect_uri = json_dict["redirect_uri"]
            except KeyError:
                connect_response_obj.redirect_type = None
                connect_response_obj.redirect_uri = None

            self.logger.log_info("Adding entry to connect_dict:")
            self.logger.log_info(str(json_dict))

            self.connect_dict[json_dict["serial"]] = connect_response_obj
            return True

        if "remove" in json_dict:
            try:
                self.connect_dict.pop(json_dict["remove"])
                self.logger.log_info("Device serial " + json_dict["remove"] + " was removed from connect_dict.")
                return True
            except KeyError:
                self.logger.log_info("Device serial " + json_dict["remove"] +
                                     " was NOT in connect_dict! Ignoring remove.")
                return True
        return False

    def configure_upgrade(self, json_dict):
        """Configures the Upgrade entry for the given device serial."""
        if "remove" in json_dict:
            try:
                self.upgrade_dict.pop(json_dict["remove"])
                self.logger.log_info("Device serial " + json_dict["remove"] + " was removed from upgrade_dict.")
                return True
            except KeyError:
                self.logger.log_info("Device serial " + json_dict["remove"] +
                                     " was NOT in upgrade_dict! Ignoring remove.")
                return True

        if "serial" in json_dict:
            serial = json_dict["serial"]
            upgrade_response_object = CcUpgradeResponse(json_dict["upgrade"], json_dict["uri"], json_dict["timeout"],
                                                        json_dict["asset_name"], json_dict["asset_version"],
                                                        json_dict["asset_type"], json_dict["asset_size"])

            upgrade_response = upgrade_response_object.create()
            self.logger.log_info("Adding entry to upgrade_dict:")
            self.logger.log_info(str(json_dict))
            self.upgrade_dict.setdefault(serial, []).append(upgrade_response)
            return True
        return False

    def configure_config(self, json_dict):
        """Configures the Configuration entry for the given device serial."""
        if "remove" in json_dict:
            try:
                self.config_dict.pop(json_dict["remove"])
                self.logger.log_info("Device serial " + json_dict["remove"] + " was removed from config_dict.")
                return True
            except KeyError:
                self.logger.log_info("Device serial " + json_dict["remove"] +
                                     " was NOT in config_dict! Ignoring remove.")
                return False

        if "serial" in json_dict:
            serial = json_dict["serial"]
            self.config_dict[serial] = json_dict[serial]
            self.logger.log_info("Adding entry to config_dict:")
            self.logger.log_info(str(json_dict))

            self.config_dict["merge"][serial] = json_dict["merge"]

            return True
        return False

    def configure_stats(self, json_dict):
        """Configures the Stats entry for the given device serial."""
        serials = ListUtils.convert_to_list(json_dict["serials"])
        for serial in serials:
            if "action" in json_dict:
                self.logger.log_info("Adding ACTION to stats_reply serial " + str(serial) + ": " + json_dict["action"])
                self.stats_reply["serials"].setdefault(serial, {})["action"] = json_dict["action"]
                if json_dict["action"] == "TRACES":
                    self.stats_reply["serials"][serial]["uri"] = json_dict["uri"]
                    self.stats_reply["serials"][serial]["delete"] = json_dict["delete"]
                if json_dict["action"] == "STATS":
                    self.stats_reply["serials"][serial]["type"] = json_dict["type"]

            if "checkin_timer" in json_dict:
                self.logger.log_info("Adding checkinTimer to stats_reply serial " + str(serial) + ": " +
                                     json_dict["checkin_timer"])
                self.stats_reply["serials"].setdefault(serial, {})["checkin_timer"] = json_dict["checkin_timer"]

            if "stats_interval" in json_dict:
                self.logger.log_info("Adding statsInterval to stats_reply serial " + str(serial) + ": " +
                                     json_dict["stats_interval"])
                self.stats_reply["serials"].setdefault(serial, {})["stats_interval"] = json_dict["stats_interval"]

            if "remove" in json_dict:
                if serial in self.stats_reply["serials"]:
                    self.logger.log_info("Removing stats_reply entry for serial: " + str(serial))
                    self.stats_reply["serials"].pop(serial)

        self.logger.log_info("Configuring stats_reply:")
        self.logger.log_info(str(json_dict))

        return True

    def get_device_states(self, json_dict):
        """
        Takes a dictionary, in the JSON:
        {"serial": "Device serial number",
         "states": [A list of FSM states, one or more],
         "wait_time": The wait_for duration for the desired FSM state(s)<int>
        }
        """
        serial = json_dict["serial"]

        if "states" in json_dict:
            inspect_states = json_dict["states"].split(",")
            wait_time = json_dict["wait_time"] if "wait_time" in json_dict else 30
            reply = {"result": False,
                     "state_list": "NONE"}
            t = 0
            while t != wait_time:
                try:
                    reply["state_list"] = ",".join(self.device_states[serial])
                    if self.compare_states(inspect_states, self.device_states[serial]):
                        self.logger.log_info("States matched for " + serial + "!")
                        reply["result"] = True
                        break
                except KeyError:
                    # Device serial was not present yet. Keep waiting.
                    pass
                time.sleep(1)
                t += 1
            return reply

        elif serial in self.device_states:
            reply = {serial: self.device_states[serial]}
            return reply
        else:
            reply = {serial: None}
            return reply

    def clear_fsm_states(self, json_dict):
        """Clears the FSM state list for the given device serial."""
        if "serial" in json_dict:
            serial = json_dict["serial"]
            try:
                self.device_states.pop(serial)
                self.logger.log_info("Device serial " + serial + " was removed from the FSM list.")
            except KeyError:
                self.logger.log_info("Device serial " + serial + " was NOT present in the FSM list!")
        return True

    def inspect_connect(self, json_dict):
        """Returns the current Connect entry for the given device serial."""
        if "serial" in self.connect_dict:
            serial = json_dict["serial"]
            if serial in self.connect_dict:
                reply = self.connect_dict[serial]
                return reply.send()
        return False

    def inspect_upgrade(self, json_dict):
        """Returns the current Upgrade entry for the given device serial."""
        if "serial" in self.upgrade_dict:
            serial = json_dict["serial"]
            if serial in self.upgrade_dict:
                reply = self.upgrade_dict[serial]
                return reply.send()
        return False

    @staticmethod
    def get_mgmt_ip(json_dict, dev_ips):
        """
        Takes a dictionary, in the JSON:
        {"serial": "Device serial number",
         "var_name": "String var name for storing the mgmt_ip",
        }
        """
        serial = json_dict["serial"]
        if serial in dev_ips:
            return {"mgmt_ip": dev_ips[serial]}
        else:
            return False

    def get_device_assests(self, json_dict):
        """Returns the current Upgrade entry for the given device serial."""
        serial = json_dict["serial"]
        if serial in self.upgrade_dict["current"]:
            if serial in self.upgrade_dict:
                reply = self.upgrade_dict["current"][serial]
                return reply
        return False

########################################################################################################################
#   Helper Functions    ################################################################################################
########################################################################################################################
    @staticmethod
    def compare_states(expect_states, current_states):
        """
        Compare FSM state lists.

        Returns True if a match is found.
        """
        num_states = len(expect_states)
        if num_states > len(current_states):
            return False
        if num_states > 1:
            for i, state in enumerate(current_states):
                if state == expect_states[0]:
                    match = True
                    for x in range(num_states):
                        try:
                            if expect_states[x] != current_states[i + x]:
                                match = False
                            if x + 1 == num_states and match:
                                return True
                        except IndexError:
                            # Reached the end of the current_states.
                            return False
        else:
            if expect_states[0] == current_states[-1]:
                return True
        return False

    def check_for_failed_download(self, serial, event_dict):
        """Checks the event for a failed upgrade and attempts to remove the associated self.upgrade_dict entry."""
        for event in event_dict:
            if "description" in event:
                desc = event["description"]
                if "Failed to download" in desc:
                    self.logger.log_info("Image download failed. Attempting to remove unsuccessful upgradeBlock.")
                    for upgrade_block in self.upgrade_dict[serial]:
                        if upgrade_block["uri"] in desc:
                            self.upgrade_dict[serial].remove(upgrade_block)
