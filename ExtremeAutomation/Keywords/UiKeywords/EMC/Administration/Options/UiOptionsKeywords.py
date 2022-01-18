from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.OptionsConstants import OptionsConstants


class UiOptionsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiOptionsKeywords, self).__init__()
        self.api_const = self.constants.API_OPTIONS
        self.cmd = OptionsConstants()

    def options_expand_option(self, element_name, option_name, **kwargs):
        """Returns the result of options_expand_option."""
        args = {"option_name": option_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_EXPAND_OPTION, **kwargs)

    def options_collapse_option(self, element_name, option_name, **kwargs):
        """Returns the result of options_collapse_option."""
        args = {"option_name": option_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_COLLAPSE_OPTION, **kwargs)

    def options_select_option(self, element_name, option_name, **kwargs):
        """Returns the result of options_select_option."""
        args = {"option_name": option_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SELECT_OPTION, **kwargs)

    def options_restore_defaults(self, element_name, **kwargs):
        """Returns the result of options_restore_."""
        return self.execute_keyword(element_name, {}, self.cmd.OPTIONS_RESTORE_DEFAULTS, **kwargs)

    def options_reset(self, element_name, **kwargs):
        """Returns the result of options_reset."""
        return self.execute_keyword(element_name, {}, self.cmd.OPTIONS_RESET, **kwargs)

    def options_save(self, element_name, **kwargs):
        """Returns the result of options_save."""
        return self.execute_keyword(element_name, {}, self.cmd.OPTIONS_SAVE, **kwargs)

    def options_set_extreme_networks_updates_credentials(self, element_name, user_name, pwd, **kwargs):
        """Returns the result of options_set_extreme_networks_updates_credentials."""
        args = {"pwd": pwd,
                "user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_EXTREME_NETWORKS_UPDATES_CREDENTIALS,
                                    **kwargs)

    def options_set_db_backup_file_path(self, element_name, option_value, **kwargs):
        """Returns the result of options_set_db_backup_file_path."""
        args = {"option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DB_BACKUP_FILE_PATH, **kwargs)

    def options_set_db_backup_include_additional_data(self, element_name, option_value, **kwargs):
        """Returns the result of options_set_db_backup_include_additional_data."""
        args = {"option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DB_BACKUP_INCLUDE_ADDITIONAL_DATA,
                                    **kwargs)

    def options_set_db_backup_schedule_file_format(self, element_name, option_value, **kwargs):
        """Returns the result of options_set_db_backup_schedule_file_format."""
        args = {"option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DB_BACKUP_SCHEDULE_FILE_FORMAT, **kwargs)

    def options_set_db_backup_schedule_occurrence(self, element_name, on_day, at_time, **kwargs):
        """Returns the result of options_set_db_backup_schedule_occurrence."""
        args = {"at_time": at_time,
                "on_day": on_day}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DB_BACKUP_SCHEDULE_OCCURRENCE, **kwargs)

    def options_set_db_backup_schedule_limit_backups(self, element_name, limit_files, max_files, **kwargs):
        """Returns the result of options_set_db_backup_schedule_limit_backups."""
        args = {"limit_files": limit_files,
                "max_files": max_files}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DB_BACKUP_SCHEDULE_LIMIT_BACKUPS, **kwargs)

    def options_set_ftp_file_transfer(self, element_name, anonymous_user, user_name, pwd, fw_dir, root_dir, use_emc_ip,
                                      server_ip, server_port, **kwargs):
        """Returns the result of options_set_ftp_file_transfer."""
        args = {"root_dir": root_dir,
                "use_emc_ip": use_emc_ip,
                "fw_dir": fw_dir,
                "anonymous_user": anonymous_user,
                "server_port": server_port,
                "pwd": pwd,
                "server_ip": server_ip,
                "user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_FTP_FILE_TRANSFER, **kwargs)

    def options_set_scp_file_transfer(self, element_name, anonymous_user, user_name, pwd, fw_dir, root_dir, use_emc_ip,
                                      server_ip, server_port, **kwargs):
        """Returns the result of options_set_scp_file_transfer."""
        args = {"root_dir": root_dir,
                "use_emc_ip": use_emc_ip,
                "fw_dir": fw_dir,
                "anonymous_user": anonymous_user,
                "server_port": server_port,
                "pwd": pwd,
                "server_ip": server_ip,
                "user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_SCP_FILE_TRANSFER, **kwargs)

    def options_set_sftp_file_transfer(self, element_name, anonymous_user, user_name, pwd, fw_dir, root_dir, use_emc_ip,
                                       server_ip, server_port, **kwargs):
        """Returns the result of options_set_sftp_file_transfer."""
        args = {"root_dir": root_dir,
                "use_emc_ip": use_emc_ip,
                "fw_dir": fw_dir,
                "anonymous_user": anonymous_user,
                "server_port": server_port,
                "pwd": pwd,
                "server_ip": server_ip,
                "user_name": user_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_SFTP_FILE_TRANSFER, **kwargs)

    def options_set_tftp_file_transfer(self, element_name, fw_dir, root_dir, server_ip, **kwargs):
        """Returns the result of options_set_tftp_file_transfer."""
        args = {"fw_dir": fw_dir,
                "root_dir": root_dir,
                "server_ip": server_ip}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_TFTP_FILE_TRANSFER, **kwargs)

    def options_set_device_tree_name_format(self, element_name, option_value, **kwargs):
        """Returns the result of options_set_device_tree_name_format."""
        args = {"option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DEVICE_TREE_NAME_FORMAT, **kwargs)

    def options_set_access_control_collection_poll_rate(self, element_name, option_value, option_units, **kwargs):
        """Returns the result of options_set_access_control_collection_poll_rate."""
        args = {"option_units": option_units,
                "option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_ACCESS_CONTROL_COLLECTION_POLL_RATE,
                                    **kwargs)

    def options_set_device_collection_poll_rate(self, element_name, option_value, option_units, **kwargs):
        """Returns the result of options_set_device_collection_poll_rate."""
        args = {"option_units": option_units,
                "option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_DEVICE_COLLECTION_POLL_RATE, **kwargs)

    def options_set_interface_collection_poll_rate(self, element_name, option_value, option_units, **kwargs):
        """Returns the result of options_set_interface_collection_poll_rate."""
        args = {"option_units": option_units,
                "option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_INTERFACE_COLLECTION_POLL_RATE, **kwargs)

    def options_set_wireless_collection_access_point_poll_rate(self, element_name, option_value, option_units,
                                                               **kwargs):
        """Returns the result of options_set_wireless_collection_access_point_poll_rate."""
        args = {"option_units": option_units,
                "option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_WIRELESS_COLLECTION_ACCESS_POINT_POLL_RATE,
                                    **kwargs)

    def options_set_wireless_collection_controller_poll_rate(self, element_name, option_value, option_units, **kwargs):
        """Returns the result of options_set_wireless_collection_controller_poll_rate."""
        args = {"option_units": option_units,
                "option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_WIRELESS_COLLECTION_CONTROLLER_POLL_RATE,
                                    **kwargs)

    def options_set_status_polling_default_group(self, element_name, option_value, **kwargs):
        """Returns the result of options_set_status_polling_."""
        args = {"option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_STATUS_POLLING_DEFAULT_GROUP, **kwargs)

    def options_set_status_polling_poll_group_1(self, element_name, group_name, interval_val, interval_units, **kwargs):
        """Returns the result of options_set_status_polling_poll_group_1."""
        args = {"interval_units": interval_units,
                "interval_val": interval_val,
                "group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_STATUS_POLLING_POLL_GROUP_1, **kwargs)

    def options_set_status_polling_poll_group_2(self, element_name, group_name, interval_val, interval_units, **kwargs):
        """Returns the result of options_set_status_polling_poll_group_2."""
        args = {"interval_units": interval_units,
                "interval_val": interval_val,
                "group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_STATUS_POLLING_POLL_GROUP_2, **kwargs)

    def options_set_status_polling_poll_group_3(self, element_name, group_name, interval_val, interval_units, **kwargs):
        """Returns the result of options_set_status_polling_poll_group_3."""
        args = {"interval_units": interval_units,
                "interval_val": interval_val,
                "group_name": group_name}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_STATUS_POLLING_POLL_GROUP_3, **kwargs)

    def options_set_trap_snmpv1_credential_name(self, element_name, the_value, **kwargs):
        """Returns the result of options_set_trap_snmpv1_credential_name."""
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_TRAP_SNMPV1_CREDENTIAL_NAME, **kwargs)

    def options_set_trap_snmpv2_credential_name(self, element_name, the_value, **kwargs):
        """Returns the result of options_set_trap_snmpv2_credential_name."""
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_TRAP_SNMPV2_CREDENTIAL_NAME, **kwargs)

    def options_set_trap_snmpv3_credential_name(self, element_name, the_value, **kwargs):
        """Returns the result of options_set_trap_snmpv3_credential_name."""
        args = {"the_value": the_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_TRAP_SNMPV3_CREDENTIAL_NAME, **kwargs)

    def options_set_web_server_timeout(self, element_name, option_value, option_units, **kwargs):
        """Returns the result of options_set_web_server_timeout."""
        args = {"option_units": option_units,
                "option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_WEB_SERVER_TIMEOUT, **kwargs)

    def options_set_site_show_vlan_untagged(self, element_name, option_value, **kwargs):
        """Returns the result of options_set_site_show_vlan_untagged."""
        args = {"option_value": option_value}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_SITE_SHOW_VLAN_UNTAGGED, **kwargs)

    def options_set_trap_engine_delay_start(self, element_name, delay_time, **kwargs):
        """Returns the result of options_set_trap_engine_delay_start."""
        args = {"delay_time": delay_time}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_TRAP_ENGINE_DELAY_START, **kwargs)

    def options_set_syslog_engine_delay_start(self, element_name, delay_time, **kwargs):
        """Returns the result of options_set_syslog_engine_delay_start."""
        args = {"delay_time": delay_time}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SET_SYSLOG_ENGINE_DELAY_START, **kwargs)

    def options_site_set_length_of_snmp_timeout(self, element_name, snmp_timeout, **kwargs):
        """Sets the length of snmp timeout."""
        args = {"snmp_timeout": snmp_timeout}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SITE_SET_LENGTH_OF_SNMP_TIMEOUT, **kwargs)

    def options_site_set_number_of_snmp_retries(self, element_name, snmp_retries, **kwargs):
        """Sets the number of SNMP retries."""
        args = {"snmp_retries": snmp_retries}

        return self.execute_keyword(element_name, args, self.cmd.OPTIONS_SITE_SET_NUMBER_OF_SNMP_RETRIES, **kwargs)
