"""
Keyword class for all cos cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.CosConstants import \
    CosConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.CosConstants import \
    CosConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementCosGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementCosGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "cos"

    def cos_create_qos_profile(self, device_name, name='', **kwargs):
        """
        Description: Creates the given QOS profiles on the given device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_QOS_PROFILE,
                                    **kwargs)

    def cos_delete_qos_profile(self, device_name, name='', **kwargs):
        """
        Description: Removes a QOS profile from a given device.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_QOS_PROFILE,
                                    **kwargs)

    def cos_create_port_group(self, device_name, group='', cos_type='', **kwargs):
        """
        Description: Creates an port group of the given type.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_type": cos_type,
            "group": group
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CREATE_PORT_GROUP,
                                    **kwargs)

    def cos_delete_port_group(self, device_name, group='', cos_type='', **kwargs):
        """
        Description: Deletes an port group of the given type.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_type": cos_type,
            "group": group
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DELETE_PORT_GROUP,
                                    **kwargs)

    def cos_set_port_group_port(self, device_name, group='', port='', cos_type='', **kwargs):
        """
        Description: Adds a port to an existing port group.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_type": cos_type,
            "group": group,
            "port": port
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_GROUP_PORT,
                                    **kwargs)

    def cos_set_txq_settings(self, device_name, cos_index='', txq_index='', qos_profile='', **kwargs):
        """
        Description: Configures a TXQ reference to a given COS value.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "qos_profile": qos_profile,
            "txq_index": txq_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TXQ_SETTINGS,
                                    **kwargs)

    def cos_set_txq_settings_cos_under_seven(self, device_name, cos_index='', txq_index='', qos_profile='', **kwargs):
        """
        Description: Configures a TXQ reference to a given COS value. For COS values below 7.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "qos_profile": qos_profile,
            "txq_index": txq_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TXQ_SETTINGS_COS_UNDER_SEVEN,
                                    **kwargs)

    def cos_set_irl_settings(self, device_name, cos_index='', irl_index='', priority='', qos_profile='', **kwargs):
        """
        Description: Configures an IRL reference to a given COS value.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "irl_index": irl_index,
            "priority": priority,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IRL_SETTINGS,
                                    **kwargs)

    def cos_set_irl_settings_cos_under_seven(self, device_name, cos_index='', irl_index='', qos_profile='', **kwargs):
        """
        Description: Configures an IRL reference to a given COS value. For COS values below 7.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "irl_index": irl_index,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IRL_SETTINGS_COS_UNDER_SEVEN,
                                    **kwargs)

    def cos_set_port_resource_irl(self, device_name, group='', irl_index='', rate='', unit='', **kwargs):
        """
        Description: Creates and inbound rate limiter.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "group": group,
            "irl_index": irl_index,
            "rate": rate,
            "unit": unit
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_RESOURCE_IRL,
                                    **kwargs)

    def cos_set_orl_settings(self, device_name, cos_index='', orl_index='', priority='', qos_profile='', **kwargs):
        """
        Description: Configures an ORL reference to a given COS value.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "orl_index": orl_index,
            "priority": priority,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ORL_SETTINGS,
                                    **kwargs)

    def cos_set_orl_settings_cos_under_seven(self, device_name, cos_index='', orl_index='', qos_profile='', **kwargs):
        """
        Description: Configures an ORL reference to a given COS value. For COS values below 7.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "orl_index": orl_index,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ORL_SETTINGS_COS_UNDER_SEVEN,
                                    **kwargs)

    def cos_set_dot1p_type(self, device_name, cos_index='', qos_profile='', **kwargs):
        """
        Description: Configures a QOS profiles to a given dot1p type.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cos_index": cos_index,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DOT1P_TYPE,
                                    **kwargs)

    def cos_set_dot1p_type_only(self, device_name, cos_index='', qos_profile='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "cos_index": cos_index,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DOT1P_TYPE_ONLY,
                                    **kwargs)

    def cos_set_dot1p_port_type(self, device_name, port='', qos_profile='', **kwargs):
        """
        Description: Applies a given QOS profiles to a port.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DOT1P_PORT_TYPE,
                                    **kwargs)

    def cos_set_qos_scheduler(self, device_name, mode='', group='', **kwargs):
        """
        Description: Sets the QOS scheduler to a given mode.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "group": group,
            "mode": mode
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_QOS_SCHEDULER,
                                    **kwargs)

    def cos_set_txq_weights(self, device_name, group='', txq='', weight='', weights='', **kwargs):
        """
        Description: Configures the weight for each TXQ on a given device.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "group": group,
            "txq": txq,
            "weight": weight,
            "weights": weights
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TXQ_WEIGHTS,
                                    **kwargs)

    def cos_set_tos_settings(self, device_name, cos_index='', tos='', **kwargs):
        """
        Description: Applies a TOS value to a given COS index.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "tos": tos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TOS_SETTINGS,
                                    **kwargs)

    def cos_set_tos_settings_cos_under_seven(self, device_name, tos='', cos_index='', qos_profile='', **kwargs):
        """
        Description: Applies a TOS value to a given COS index. For COS values below 7.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "qos_profile": qos_profile,
            "tos": tos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TOS_SETTINGS_COS_UNDER_SEVEN,
                                    **kwargs)

    def cos_set_priority_settings(self, device_name, cos_index='', priority='', qos_profile='', **kwargs):
        """
        Description: Configures a COS index with the given priority.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "priority": priority,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PRIORITY_SETTINGS,
                                    **kwargs)

    def cos_set_priority_settings_cos_under_seven(self, device_name, cos_index='', priority='', qos_profile='',
                                                  **kwargs):
        """
        Description: Configures a COS index with the given priority. For COS values below 7.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index,
            "priority": priority,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PRIORITY_SETTINGS_COS_UNDER_SEVEN,
                                    **kwargs)

    def cos_set_diff_serve_replacement(self, device_name, qos_profile='', tos='', **kwargs):
        """
        Description: Not provided in CSV.

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "qos_profile": qos_profile,
            "tos": tos
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_DIFF_SERVE_REPLACEMENT,
                                    **kwargs)

    def cos_clear_index(self, device_name, cos_index='', **kwargs):
        """
        Description: Removes the given COS index from the device's configuration.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "cos_index": cos_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_INDEX,
                                    **kwargs)

    def cos_clear_irl(self, device_name, group='', irl_index='', **kwargs):
        """
        Description: Removes the given IRL from the configuration.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "group": group,
            "irl_index": irl_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IRL,
                                    **kwargs)

    def cos_set_txq_shaping(self, device_name, group='', rate='', unit='', qos_profile='', txq='', **kwargs):
        """
        Description: Applies rate shaping to a given transmit queue.

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "group": group,
            "qos_profile": qos_profile,
            "rate": rate,
            "txq": txq,
            "unit": unit
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TXQ_SHAPING,
                                    **kwargs)

    def cos_clear_txq_shaping(self, device_name, group='', txq='', **kwargs):
        """
        Description: Removes rate shaping from a TXQ. Note: on EXOS it removes rate shaping from all TXQs..

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "group": group,
            "txq": txq
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TXQ_SHAPING,
                                    **kwargs)

    def cos_set_port_priority(self, device_name, port='', pri='', **kwargs):
        """
        Description: Applies the given priority to the port(s).

        Supported Agents and OS:
            CLI: EXOS, EOS
        """
        args = {
            "port": port,
            "pri": pri
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_PRIORITY,
                                    **kwargs)

    def cos_set_port_qos_profile(self, device_name, port='', qos_profile='', **kwargs):
        """
        Description: Applies the given qos profile to the port(s).

        Supported Agents and OS:
            CLI: EXOS
        """
        args = {
            "port": port,
            "qos_profile": qos_profile
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_QOS_PROFILE,
                                    **kwargs)

    def cos_enable_state(self, device_name, **kwargs):
        """
        Description: Enables COS on a given device.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.ENABLE_STATE,
                                    **kwargs)

    def cos_disable_state(self, device_name, **kwargs):
        """
        Description: Disables COS on a given device.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.DISABLE_STATE,
                                    **kwargs)

    def cos_set_txq_reference(self, device_name, group='', reference='', queue='', **kwargs):
        """
        Description: Applies a TXQ to a given reference number.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "group": group,
            "queue": queue,
            "reference": reference
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_TXQ_REFERENCE,
                                    **kwargs)

    def cos_clear_txq_settings(self, device_name, cos_index='', **kwargs):
        """
        Description: Removes the txq reference for a given COS index.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos_index": cos_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TXQ_SETTINGS,
                                    **kwargs)

    def cos_set_irl_reference(self, device_name, group='', reference='', number='', **kwargs):
        """
        Description: Applies an IRL to a given reference number.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "group": group,
            "number": number,
            "reference": reference
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_IRL_REFERENCE,
                                    **kwargs)

    def cos_clear_irl_settings(self, device_name, cos_index='', **kwargs):
        """
        Description: Removes the IRL reference for a given COS index.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos_index": cos_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_IRL_SETTINGS,
                                    **kwargs)

    def cos_set_orl_reference(self, device_name, group='', reference='', number='', **kwargs):
        """
        Description: Applies an ORL to a given reference number.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "group": group,
            "number": number,
            "reference": reference
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_ORL_REFERENCE,
                                    **kwargs)

    def cos_set_port_resource_orl(self, device_name, group='', orl_index='', rate='', unit='', **kwargs):
        """
        Description: Creates and outbound rate limiter.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "group": group,
            "orl_index": orl_index,
            "rate": rate,
            "unit": unit
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PORT_RESOURCE_ORL,
                                    **kwargs)

    def cos_clear_orl_settings(self, device_name, cos_index='', **kwargs):
        """
        Description: Removes the ORL reference for a given COS index.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos_index": cos_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ORL_SETTINGS,
                                    **kwargs)

    def cos_clear_tos_settings(self, device_name, cos_index='', **kwargs):
        """
        Description: Removes the TOS value for a given COS index.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos_index": cos_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_TOS_SETTINGS,
                                    **kwargs)

    def cos_clear_flood_ctrl_settings(self, device_name, cos_index='', **kwargs):
        """
        Description: Removes the Flood Control reference for a given COS index.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {
            "cos_index": cos_index
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_FLOOD_CTRL_SETTINGS,
                                    **kwargs)

    def cos_clear_all_config(self, device_name, **kwargs):
        """
        Description: Removes all COS configuration on a given device.

        Supported Agents and OS:
            CLI: EOS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_ALL_CONFIG,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def cos_verify_qos_profile_exists(self, device_name, qos_profiles='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [qos_profiles] - The QOS profiles that should exist on the device.

        Verifies a QOS profile exists on a give device.
        """
        args = {"qp": qos_profiles}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_QOS_PROFILE,
                                           self.parse_const.CHECK_QOS_PROFILE_EXISTS, True,
                                           "QoS Profile: {qp} exists on {device_name}.",
                                           "QoS Profile: {qp} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def cos_verify_qos_profile_does_not_exist(self, device_name, qos_profiles='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [qos_profiles] - The QOS profile(s) that should not exist on the device.

        Verifies that a QOS profile does not exist on a given device.
        """
        args = {"qp": qos_profiles}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_QOS_PROFILE,
                                           self.parse_const.CHECK_QOS_PROFILE_EXISTS, False,
                                           "QoS Profile: {qp} does not exist on {device_name}.",
                                           "QoS Profile: {qp} EXISTS on {device_name}.",
                                           **kwargs)

    def cos_verify_enabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.

        Verifies that COS is enabled on a given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_COS_STATE, True,
                                           "COS state was enabled on {device_name}.",
                                           "COS state was DISABLED on {device_name}.",
                                           **kwargs)

    def cos_verify_disabled(self, device_name, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.

        Verifies that COS is disabled on a given device.
        """
        args = {}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_STATE,
                                           self.parse_const.CHECK_COS_STATE, False,
                                           "COS state was disabled on {device_name}.",
                                           "COS state was ENABLED on {device_name}.",
                                           **kwargs)

    def cos_verify_irl_port_group_exists(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The IRL port group to inspect.
                  EOS group format should be #.# for group number and port type.
        [port_type] - The port type for ports in the group.

        Verifies that an IRL port group exists on a given device.
        """
        args = {"group": group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_GROUP,
                                           self.parse_const.CHECK_PORT_GROUP_EXISTS, True,
                                           "IRL port group {group} exists on {device_name}.",
                                           "IRL port group {group} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def cos_verify_irl_port_group_does_not_exist(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The IRL port group to inspect.
                  EOS group format should be #.# for group number and port type.
        [port_type] - The port type for ports in the group.

        Verifies that an IRL port group does not exist on a given device.
        """
        args = {"group": group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_GROUP,
                                           self.parse_const.CHECK_PORT_GROUP_EXISTS, True,
                                           "IRL port group {group} does not exist on {device_name}.",
                                           "IRL port group {group} EXISTS on {device_name}.",
                                           **kwargs)

    def cos_verify_txq_port_group_exists(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The TXQ port group to inspect.
                  EOS group format should be #.# for group number and port type.
        [port_type] - The port type for ports in the group.

        Verifies that an TXQ port group exists on a given device.
        """
        args = {"group": group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_PORT_GROUP,
                                           self.parse_const.CHECK_PORT_GROUP_EXISTS, True,
                                           "IRL port group {group} exists on {device_name}.",
                                           "IRL port group {group} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def cos_verify_txq_port_group_does_not_exist(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The TXQ port group to inspect.
                  EOS group format should be #.# for group number and port type.
        [port_type] - The port type for ports in the group.

        Verifies that an TXQ port group does not exist on a given device.
        """
        args = {"group": group}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_PORT_GROUP,
                                           self.parse_const.CHECK_PORT_GROUP_EXISTS, False,
                                           "IRL port group {group} does not exist on {device_name}.",
                                           "IRL port group {group} EXISTS on {device_name}.",
                                           **kwargs)

    def cos_verify_irl_configured(self, device_name, group='', cos_index='', rate='', unit="pps", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [group] - The IRL port group to be inspected.
                  EOS group format should be #.# for group number and port type.
        [cos_index] - The IRL index to inspect.
        [rate] - The rate that the IRL should be configured with.
        [unit] - The unit that the IRL should be configured with.

        Verifies an IRL was configured as expected.
        """
        args = {"group": group,
                "cos_index": cos_index,
                "unit": unit,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_RESOURCE_SPECIFIC,
                                           self.parse_const.CHECK_COS_PORT_RESOURCE, True,
                                           "IRL index {index} was set to {rate} {unit} on {device_name}.",
                                           "IRL index {index} was NOT set to {rate} {unit} on {device_name}.",
                                           **kwargs)

    def cos_verify_irl_not_configured(self, device_name, group='', cos_index='', rate='', unit="pps", **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [group] - The IRL port group to be inspected.
                  EOS group format should be #.# for group number and port type.
        [cos_index] - The IRL index to inspect.

        Verifies an IRL was not configured.
        """
        args = {"group": group,
                "cos_index": cos_index,
                "unit": unit,
                "rate": rate,
                "configured": False}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_RESOURCE_SPECIFIC,
                                           self.parse_const.CHECK_COS_PORT_RESOURCE, False,
                                           "IRL index {index} was not configured on {device_name}.",
                                           "IRL index {index} WAS configured on {device_name}.",
                                           **kwargs)

    def cos_verify_txq_wfq_weights(self, device_name, group='', weights='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group_number] - The group number whose queues should be checked.
        [port_type] - The port type for the ports in the group.
        [queue] - The TXQ to inspect.
        [weight] - The weight or slice assigned to the queue.

        Verifies a queues weight/slice on a given device.
        """
        args = {"group": group,
                "weights": weights}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_WFQ_WEIGHTS,
                                           self.parse_const.CHECK_TXQ_WEIGHTS, True,
                                           "The " + str(len(weights.split(","))) + " queues were set to "
                                           "{weights} on {device_name}.",
                                           "The " + str(len(weights.split(","))) + " queues were NOT set to "
                                           "{weights} on {device_name}.",
                                           **kwargs)

    def cos_verify_irl_reference(self, device_name, group='', reference='', rate_limiter='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The IRL port group to be inspected.
        [port_type] - The port type for the ports in the group.
        [reference] - Which reference should be verified.
        [rate_limiter] - The rate limiter that should be configured to the specified reference.

        Verifies the correct IRL is configured to a specific reference.
        """
        args = {"group": group,
                "reference": reference,
                "rate_limiter": rate_limiter}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_REFERENCE,
                                           self.parse_const.CHECK_COS_REFERENCE, True,
                                           "IRL reference {reference} was configured with IRL {rate_limiter} "
                                           "on device {device_name}.",
                                           "IRL reference {reference} was NOT configured with IRL {rate_limiter} "
                                           "on device {device_name}.",
                                           **kwargs)

    def cos_verify_orl_reference(self, device_name, group='', reference='', rate_limiter='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group_number] - The group number of the reference to check.
        [port_type] - The port type for the ports in the group.
        [reference] - Which reference should be verified.
        [rate_limiter] - The rate limiter that should be configured to the specified reference.

        Verifies the correct ORL is configured to a specific reference.
        """
        args = {"group": group,
                "reference": reference,
                "rate_limiter": rate_limiter}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ORL_REFERENCE,
                                           self.parse_const.CHECK_COS_REFERENCE, True,
                                           "ORL reference {reference} was configured with ORL {rate_limiter} "
                                           "on device {device_name}.",
                                           "ORL reference {reference} was NOT configured with ORL {rate_limiter} "
                                           "on device {device_name}.",
                                           **kwargs)

    def cos_verify_txq_reference(self, device_name, group='', reference='', queue='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group_number] - The group number of the reference to check.
        [port_type] - The port type for the ports in the group.
        [reference] - Which reference should be verified.
        [queue] - The queue that should be configured to the specified reference.

        Verifies the correct TXQ is configured to a specific reference.
        """
        args = {"group": group,
                "reference": reference,
                "queue": queue}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_REFERENCE,
                                           self.parse_const.CHECK_COS_REFERENCE, True,
                                           "TXQ reference {reference} was configured with queue {queue} "
                                           "on device {device_name}.",
                                           "TXQ reference {reference} was NOT configured with queue {queue} "
                                           "on device {device_name}.",
                                           **kwargs)

    def cos_verify_irl_port_resource(self, device_name, group='', cos_index='', unit='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group_number] - The group number of the resource to check.
        [port_type] - The port type for the ports in the group.
        [cos_index] - The IRL resource index to inspect.
        [unit] - The unit that should be configured to the given resource. Valid options are "percentage", "pps",
                 "kbps", "mbps", and "gbps".
        [rate] - The rate that should be configured to the given resource.

        Verifies that a given IRL port resource is configured.
        """
        args = {"group": group,
                "cos_index": cos_index,
                "unit": unit,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_RESOURCE,
                                           self.parse_const.CHECK_COS_PORT_RESOURCE, True,
                                           "IRL resource {index} rate limiter was equal to {rate} {unit}"
                                           " on {device_name}.",
                                           "IRL resource {index} rate limiter was NOT equal to {rate} {unit}"
                                           " on {device_name}.",
                                           **kwargs)

    def cos_verify_orl_port_resource(self, device_name, group='', cos_index='', unit='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group_number] - The group number of the resource to check.
        [port_type] - The port type for the ports in the group.
        [cos_index] - The ORL resource index to inspect.
        [unit] - The unit that should be configured to the given resource. Valid options are "percentage", "pps",
                 "kbps", "mbps", and "gbps".
        [rate] - The rate that should be configured to the given resource.

        Verifies that a given ORL port resource is configured.
        """
        args = {"group": group,
                "cos_index": cos_index,
                "unit": unit,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ORL_PORT_RESOURCE,
                                           self.parse_const.CHECK_COS_PORT_RESOURCE, True,
                                           "ORL resource {index} rate limiter was equal to {rate} {unit}"
                                           " on {device_name}.",
                                           "ORL resource {index} rate limiter was NOT equal to {rate} {unit}"
                                           " on {device_name}.",
                                           **kwargs)

    def cos_verify_txq_port_resource(self, device_name, group='', cos_index='', unit='', rate='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group_number] - The group number of the resource to check.
        [port_type] - The port type for the ports in the group.
        [cos_index] - The TXQ resource index to inspect.
        [unit] - The unit that should be configured to the given resource. Valid options are "percentage", "pps",
                 "kbps", "mbps", and "gbps".
        [rate] - The rate that should be configured to the given resource.

        Verifies that a given TXQ port resource is configured.
        """
        args = {"group": group,
                "cos_index": cos_index,
                "unit": unit,
                "rate": rate}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_PORT_RESOURCE,
                                           self.parse_const.CHECK_COS_PORT_RESOURCE, True,
                                           "TXQ resource {index} rate limiter was equal to {rate} {unit} on "
                                           "{device_name}.",
                                           "TXQ resource {index} rate limiter was NOT equal to {rate} {unit} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_index_exists(self, device_name, cos_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [cos_indexes] - The COS index(es) that should exist on the device.

        Verifies that a COS index exists on a given device.
        """
        args = {"cos_index": cos_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, False,
                                           "COS index {index} exists on {device_name}.",
                                           "COS index {index} DOES NOT exist on {device_name}.",
                                           **kwargs)

    def cos_verify_index_does_not_exist(self, device_name, cos_index='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [cos_indexes] - The COS index(es) that should exist on the device.

        Verifies that a COS index exists on a given device.
        """
        args = {"cos_index": cos_index}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, False,
                                           "COS index {index} does not exist on {device_name}.",
                                           "COS index {index} EXISTS on {device_name}.",
                                           **kwargs)

    def cos_verify_index_priority(self, device_name, cos_index='', priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [priority] - The priority that should be applied to the COS index.

        Verifies that the correct priority is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with priority {priority} on "
                                           "{device_name}.",
                                           "COS index {index} was NOT configured with priority {priority} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_index_tos(self, device_name, cos_index='', tos='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [tos] - The TOS value that should be applied to the COS index.

        Verifies that the correct priority is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "tos": tos}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with TOS {tos} on {device_name}.",
                                           "COS index {index} was NOT configured with TOS {tos} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_index_txq(self, device_name, cos_index='', txq='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [txq] - The TXQ that should be applied to the COS index.

        Verifies that the correct txq is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "txq": txq}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with TXQ {txq} on {device_name}.",
                                           "COS index {index} was NOT configured with TXQ {txq} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_index_irl(self, device_name, cos_index='', irl='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [irl] - The IRL that should be applied to the COS index.

        Verifies that the correct irl is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "irl": irl}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with IRL {irl} on {device_name}.",
                                           "COS index {index} was NOT configured with IRL {irl} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_index_orl(self, device_name, cos_index='', orl='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [orl] - The ORL that should be applied to the COS index.

        Verifies that the correct orl is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "orl": orl}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with ORL {orl} on {device_name}.",
                                           "COS index {index} was NOT configured with ORL {orl} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_index_drop_precedence(self, device_name, cos_index='', drop_precedence='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [drop_precedence] - The drop_precedence that should be applied to the COS index.

        Verifies that the correct drop_precedence is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "drop_prec": drop_precedence}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with drop precedence {drop_prec}"
                                           " on {device_name}.",
                                           "COS index {index} was NOT configured with drop precedence {drop_prec}"
                                           " on {device_name}.",
                                           **kwargs)

    def cos_verify_index_flood_control(self, device_name, cos_index='', flood_ctrl='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [cos_indexes] - The cos index(es) to inspect.
        [flood_ctrl] - The flood_ctrl that should be applied to the COS index.

        Verifies that the correct flood_ctrl is configured to a given COS index.
        """
        args = {"cos_index": cos_index,
                "flood_ctrl": flood_ctrl}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SETTINGS,
                                           self.parse_const.CHECK_COS_SETTINGS, True,
                                           "COS index {index} was configured with flood control {flood_ctrl}"
                                           " on {device_name}.",
                                           "COS index {index} was NOT configured with flood control {flood_ctrl}"
                                           " on {device_name}.",
                                           **kwargs)

    def cos_verify_port_in_irl_port_group(self, device_name, group='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group]       - The port group that ports should belong to.
        [port]        - The port(s) that should be within the port group.

        Verifies that a port group contains a given port.
        """
        args = {"group": group,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_GROUP_SPECIFIC,
                                           self.parse_const.CHECK_PORT_GROUP_PORTS, True,
                                           "IRL port group {group} contains port {port} on {device_name}.",
                                           "IRL port group {group} DOES NOT contain port {port} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_port_not_in_irl_port_group(self, device_name, group='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group]       - The port group that ports should belong to.
        [port]        - The port(s) that should be within the port group.

        Verifies that a port group contains a given port.
        """
        args = {"group": group,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_IRL_PORT_GROUP_SPECIFIC,
                                           self.parse_const.CHECK_PORT_GROUP_PORTS, False,
                                           "IRL port group {group} does not contain port {port} on "
                                           "{device_name}.",
                                           "IRL port group {group} CONTAINS port {port} on {device_name}.",
                                           **kwargs)

    def cos_verify_port_in_txq_port_group(self, device_name, group='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group]       - The port group that ports should belong to.
        [port]        - The port(s) that should be within the port group.

        Verifies that a port group contains a given port.
        """
        args = {"group": group,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_PORT_GROUP_SPECIFIC,
                                           self.parse_const.CHECK_PORT_GROUP_PORTS, True,
                                           "TXQ port group {group} contains port {port} on {device_name}.",
                                           "TXQ port group {group} DOES NOT contain port {port} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_port_not_in_txq_port_group(self, device_name, group='', port='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group]       - The port group that ports should belong to.
        [port]        - The port(s) that should be within the port group.

        Verifies that a port group contains a given port.
        """
        args = {"group": group,
                "port": port}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_TXQ_PORT_GROUP_SPECIFIC,
                                           self.parse_const.CHECK_PORT_GROUP_PORTS, False,
                                           "TXQ port group {group} does not contain port {port} on "
                                           "{device_name}.",
                                           "TXQ port group {group} contains port {port} on {device_name}.",
                                           **kwargs)

    def cos_verify_qos_scheduler_strict_priority(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The group to inspect.

        Verifies that a give port groups QOS scheduler is set to strict priority.
        """
        args = {"group": group,
                "mode": 0}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_QOS_SCHEDULER,
                                           self.parse_const.CHECK_QOS_SCHEDULER_MODE, True,
                                           "QOS scheduler was set to strict priority for group {group} on "
                                           "{device_name}.",
                                           "QOS scheduler was NOT set to strict priority for group {group} on "
                                           "{device_name}.",
                                           **kwargs)

    def cos_verify_qos_scheduler_weighted_round_robin(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The group to inspect.

        Verifies that a give port groups QOS scheduler is set to weighted round robin.
        """
        args = {"group": group,
                "mode": 1}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_QOS_SCHEDULER,
                                           self.parse_const.CHECK_QOS_SCHEDULER_MODE, True,
                                           "QOS scheduler was set to weighted round robin for group {group} on "
                                           "{device_name}.",
                                           "QOS scheduler was NOT set to weighted round robin for group {group} "
                                           "on {device_name}.",
                                           **kwargs)

    def cos_verify_qos_scheduler_weighted_deficit_round_robin(self, device_name, group='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [group] - The group to inspect.

        Verifies that a give port groups QOS scheduler is set to weighted deficit round robin.
        """
        args = {"group": group,
                "mode": 2}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_QOS_SCHEDULER,
                                           self.parse_const.CHECK_QOS_SCHEDULER_MODE, True,
                                           "QOS scheduler was set to weighted deficit round robin for group "
                                           "{group} on {device_name}.",
                                           "QOS scheduler was NOT set to weighted deficit round robin for group "
                                           "{group} on {device_name}.",
                                           **kwargs)

    def cos_verify_port_priority(self, device_name, port='', priority='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should be run against.
        [port]        - The port(s) to inspect.
        [priority]    - The priority value that should be applied to the port.

        Verifies the priority applied to a given port.
        """
        args = {"port": port,
                "priority": priority}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_PRIORITY,
                                           self.parse_const.VERIFY_PORT_PRIORITY, True,
                                           "Priority was {priority} on port {port}.",
                                           "Priority was NOT {priority} on port {port}.",
                                           **kwargs)

    def cos_verify_port_qos_profile(self, device_name, port='', qos_profile='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [port]        - The ports whose qos profile should be inspected.
        [qos_profile] - The qos profile that the port should be configured with.

        Verifies the given qos profile is applied to the specified port.
        """
        args = {"port": port,
                "qp": qos_profile}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_PORT_QOS_PROFILE,
                                           self.parse_const.CHECK_PORT_QOS_PROFILE, True,
                                           "Port {port} was configured with QOS profile {qp}.",
                                           "Port {port} was NOT configured with QOS profile {qp}.",
                                           **kwargs)
