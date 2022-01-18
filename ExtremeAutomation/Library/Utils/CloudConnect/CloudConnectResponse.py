import ExtremeAutomation.Library.Utils.CloudConnect.CloudConnectEncryption as CloudConnectEncryption
import logging


class CcConnectResponse(object):
    def __init__(self):
        self._action = ""
        self._standby_timeout = 0
        self._redirect_type = ""

        self.action = "RESET"
        self.standby_timeout = 5
        self.login = "admin"
        self.password = "extreme"
        self.redirect_uri = None
        self.redirect_type = None

    @property
    def action(self):
        """Variable property for 'action' setter."""
        return self._action

    @action.setter
    def action(self, action):
        valid_actions = ["ACCEPT", "PENDING", "REDIRECT", "RESET"]
        if action.upper() in valid_actions:
            self._action = str(action).upper()
        else:
            raise ValueError("Provided action value is not valid.\nValid actions are " + str(valid_actions))

    @property
    def standby_timeout(self):
        """Variable property for 'standby_timeout' setter."""
        return self._standby_timeout

    @standby_timeout.setter
    def standby_timeout(self, standby_timeout):
        if 5 <= int(standby_timeout) <= 3600:
            self._standby_timeout = int(standby_timeout)
        else:
            raise ValueError("Provided Standby-Timeout is not between 5 and 3600.")

    @property
    def redirect_type(self):
        """Variable property for 'redirect_type' setter."""
        return self._redirect_type

    @redirect_type.setter
    def redirect_type(self, redirect_type):
        if redirect_type is not None:
            valid_types = ["IPSEC", "HTTPS"]
            if redirect_type.upper() in valid_types:
                self._redirect_type = str(redirect_type).upper()
            else:
                raise ValueError("Provided Redirect-Type is not valid.\nValid types are " + str(valid_types))

    def send(self):
        """Returns the Connect reply dictionary."""
        arg_dict = {"action": self.action,
                    "standbyTimeout": self.standby_timeout,
                    "credentials":
                        {"login": CloudConnectEncryption.des3_encrypt(self.login),
                         "password": CloudConnectEncryption.des3_encrypt(self.password)}
                    }
        if self.redirect_type is not None and self.redirect_uri is not None:
            arg_dict["redirect"] = {"type": self.redirect_type,
                                    "uri": self.redirect_uri}
        return arg_dict


class CcUpgradeResponse(object):

    def __init__(self, upgrade, uri, timeout, asset_name, asset_version, asset_type, asset_size):
        self._upgrade = False
        self._timeout = 0
        self._asset_type = ""
        self._asset_size = 0

        self.upgrade = upgrade
        self.uri = uri
        self.timeout = timeout
        self.asset_name = asset_name
        self.asset_version = asset_version
        self.asset_type = asset_type
        self.asset_size = asset_size

    @property
    def upgrade(self):
        """Variable property for 'upgrade' setter."""
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        if isinstance(upgrade, bool):
            self._upgrade = upgrade
        else:
            raise ValueError("Provided upgrade value is not valid.\nValue must be a boolean.")

    @property
    def timeout(self):
        """Variable property for 'timeout' setter."""
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        if 5 <= int(timeout) <= 3600:
            self._timeout = timeout
        else:
            raise ValueError("Provided timeout is not between 5 and 3600.")

    @property
    def asset_type(self):
        """Variable property for 'asset_type' setter."""
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        valid_types = ["SCRIPT", "FIRMWARE", "XMOD", "LIBRARY", "XML", "OTHER"]
        if asset_type.upper() in valid_types:
            self._asset_type = asset_type.upper()
        else:
            raise ValueError("Provided assetType value is not valid.\nValid types are " + str(valid_types))

    @property
    def asset_size(self):
        """Variable property for 'asset_size' setter."""
        return self._asset_size

    @asset_size.setter
    def asset_size(self, asset_size):
        if isinstance(asset_size, int):
            self._asset_size = asset_size
        else:
            self._asset_size = int(asset_size)

    def create(self):
        """Returns the Upgrade reply dictionary."""
        arg_dict = {"upgrade": self.upgrade,
                    "uri": self.uri,
                    "timeout": self.timeout,
                    "assetName": self.asset_name,
                    "assetVersion": self.asset_version,
                    "assetType": self.asset_type}

        if self.asset_size != 0:
            arg_dict["assetSize"] = self.asset_size
        return arg_dict


class CcConfigResponse(object):
    def __init__(self, config_orig, config_new):
        self.config_orig = {}
        self.config_new = {}

        self.config_orig = config_orig
        self.config_new = config_new

    @property
    def config_orig(self):
        """Variable property for 'config_orig' setter."""
        return self._config_orig

    @config_orig.setter
    def config_orig(self, config_orig):
        if isinstance(config_orig, dict):
            self._config_orig = config_orig
        else:
            raise ValueError("Provided Original config is not valid.\nValue must be a dictionary.")

    @property
    def config_new(self):
        """Variable property for 'config_new' setter."""
        return self._config_new

    @config_new.setter
    def config_new(self, config_new):
        if isinstance(config_new, dict):
            self._config_new = config_new
        else:
            raise ValueError("Provided New config is not valid.\nValue must be a dictionary.")

    def merge_config_blocks(self, orig, new):
        """Attempts to merge the new ConfigBlocks with the Original from the DUT."""
        for block in new:
            if block not in orig:
                orig[block] = new[block]
            elif isinstance(new[block], list) and len(new[block]) > 0 and isinstance(new[block][0], dict):
                if block == "vlanConfig":
                    merged = {}
                    for vlan in orig[block] + new[block]:
                        if "vlanId" in vlan:
                            if vlan["vlanId"] in merged:
                                merged[vlan["vlanId"]].update(vlan)
                            else:
                                merged[vlan["vlanId"]] = vlan
                        else:
                            if vlan["role"] in merged:
                                merged[vlan["role"]].update(vlan)
                            else:
                                merged[vlan["role"]] = vlan
                    orig[block] = [val for (_, val) in merged.items()]
                elif block == "ports":
                    merged = {}
                    for port in orig[block] + new[block]:
                        if port["portName"] in merged:
                            merged[port["portName"]].update(port)
                        else:
                            merged[port["portName"]] = port
                    orig[block] = [val for (_, val) in merged.items()]
                    for port_dict in orig[block]:
                        port_dict["pvid"] = int(port_dict["pvid"])
                else:
                    for new_item, orig_item in zip(new[block], orig[block]):
                        self.merge_config_blocks(orig_item, new_item)
            elif isinstance(new[block], dict):
                self.merge_config_blocks(orig[block], new[block])
            else:
                orig[block] = new[block]
        if "vpex" in orig:
            if not orig["vpex"]["enabled"]:
                orig.pop("vpex")

    def remove_null_blocks(self, config_blocks):
        """Attempts to remove empty configBlocks from the dictionary."""
        for block in config_blocks.keys():
            block_val = config_blocks[block]
            if isinstance(block_val, list) and len(block_val) > 0 and isinstance(block_val[0], dict):
                for item in block_val:
                    self.remove_null_blocks(item)
            elif isinstance(block_val, dict):
                self.remove_null_blocks(block_val)
            elif isinstance(block_val, str):
                if block_val == "null" or block_val == "":
                    config_blocks.pop(block)

    def send(self, merge=False):
        """Returns the Configuration reply dictionary."""
        merge = False if not merge else True
        if merge:
            logging.info("Attempting to merge Switch config and User config.")
            final_config = self.config_orig.copy()
            try:
                self.merge_config_blocks(final_config, self.config_new)
            except Exception as e:
                logging.info("Exception received while merging configs: " + str(e))

            # Attempt to remove empty configBlocks.
            # self.remove_null_blocks(final_config)
            return final_config
        else:
            return self.config_new


class CcStatsResponse(object):
    def __init__(self, stats_dict):
        self._action = ""
        self.action = stats_dict["action"]

        self.stats_dict = stats_dict

    @property
    def action(self):
        """Variable property for 'action' setter."""
        return self._action

    @action.setter
    def action(self, action):
        valid_actions = ["REBOOT", "RESET", "IMAGE_UPGRADE", "CONFIGURATION", "TRACES", "STATS", "NONE"]
        if action.upper() in valid_actions:
            self._action = str(action).upper()
        else:
            raise ValueError("Provided action value is not valid.\nValid value are: " + str(valid_actions))

    def send(self):
        """Returns the Stats reply dictionary."""
        arg_dict = {"action": self.action}

        if self.action == "TRACES":
            arg_dict["tracesBlock"] = {"uri": self.stats_dict["uri"],
                                       "delete": "true" if self.stats_dict["delete"] else "false"}
        if self.action == "STATS":
            arg_dict["statsBlock"] = {"type": self.stats_dict["type"]}

        if self.action == "CONFIGURATION":
            arg_dict["configBlock"] = self.stats_dict["config"]["configBlock"]

        if self.action == "IMAGE_UPGRADE":
            arg_dict["imageUpgradeBlock"] = self.stats_dict["upgrade"]["imageUpgradeBlock"]

        if "checkin_timer" in self.stats_dict:
            arg_dict["statsTimer"] = int(self.stats_dict["checkin_timer"])

        if "stats_interval" in self.stats_dict:
            arg_dict["statsInterval"] = int(self.stats_dict["stats_interval"])

        return arg_dict
