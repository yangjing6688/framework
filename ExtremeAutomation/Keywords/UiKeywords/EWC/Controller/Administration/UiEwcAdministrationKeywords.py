from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcadministrationConstants \
    import EwcadministrationConstants


class UiEwcAdministrationKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcAdministrationKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_ADMINISTRATION
        self.command_const = EwcadministrationConstants()

    def administration_rename_hostname(self, element_name, host_name, **kwargs):
        """Returns the result of administration_rename_hostname."""
        args = {"host_name": host_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_RENAME_HOSTNAME, **kwargs)

    def administration_hostname_should_exist(self, element_name, host_name, **kwargs):
        """Returns the result of administration_hostname_should_exist."""
        args = {"host_name": host_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_HOSTNAME_SHOULD_EXIST, **kwargs)

    def administration_hostname_should_not_exist(self, element_name, host_name, **kwargs):
        """Returns the result of administration_hostname_should_not_exist."""
        args = {"host_name": host_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_HOSTNAME_SHOULD_NOT_EXIST, **kwargs)

    def administration_rename_domain_name(self, element_name, domain_name, **kwargs):
        """Returns the result of administration_rename_domain_name."""
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_RENAME_DOMAIN_NAME, **kwargs)

    def administration_domain_name_should_exist(self, element_name, domain_name, **kwargs):
        """Returns the result of administration_domain_name_should_exist."""
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_DOMAIN_NAME_SHOULD_EXIST, **kwargs)

    def administration_domain_name_should_not_exist(self, element_name, domain_name, **kwargs):
        """Returns the result of administration_domain_name_should_not_exist."""
        args = {"domain_name": domain_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_DOMAIN_NAME_SHOULD_NOT_EXIST, **kwargs)

    def administration_add_primary_dns_server_on_host(self, element_name, dns_ip, **kwargs):
        """Returns the result of administration_add_primary_dns_server_on_host."""
        args = {"dns_ip": dns_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_ADD_PRIMARY_DNS_SERVER_ON_HOST, **kwargs)

    def administration_delete_primary_dns_server_on_host(self, element_name, dns_ip, **kwargs):
        """Returns the result of administration_delete_primary_dns_server_on_host."""
        args = {"dns_ip": dns_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_DELETE_PRIMARY_DNS_SERVER_ON_HOST, **kwargs)

    def administration_validate_primary_dns_server_ip_on_host(self, element_name, dns_ip, **kwargs):
        """Returns the result of administration_validate_primary_dns_server_ip_on_host."""
        args = {"dns_ip": dns_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.ADMINISTRATION_VALIDATE_PRIMARY_DNS_SERVER_IP_ON_HOST, **kwargs)

    def administration_click_save_button(self, element_name, **kwargs):
        """Returns the result of administration_click_save_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.ADMINISTRATION_CLICK_SAVE_BUTTON,
                                    **kwargs)
