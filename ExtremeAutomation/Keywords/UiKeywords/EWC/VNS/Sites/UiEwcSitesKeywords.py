from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EWC.EwcsitesConstants import EwcsitesConstants


class UiEwcSitesKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEwcSitesKeywords, self).__init__()
        self.api_const = self.constants.API_EWC_SITES
        self.command_const = EwcsitesConstants()

    def sites_create_site(self, element_name, site_name, site_roles, **kwargs):
        """Returns the result of sites_create_site."""
        args = {"site_name": site_name,
                "site_roles": site_roles}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CREATE_SITE, **kwargs)

    def sites_delete_site(self, element_name, site_name, **kwargs):
        """Returns the result of sites_delete_site."""
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_DELETE_SITE, **kwargs)

    def sites_click_save_button(self, element_name, **kwargs):
        """Returns the result of sites_click_save_button."""
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.SITES_CLICK_SAVE_BUTTON, **kwargs)

    def sites_select_tab_in_site_page(self, element_name, tab_name, **kwargs):
        """Returns the result of sites_select_tab_in_site_page."""
        args = {"tab_name": tab_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_SELECT_TAB_IN_SITE_PAGE, **kwargs)

    def sites_site_should_exist(self, element_name, site_name, **kwargs):
        """Returns the result of sites_site_should_exist."""
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_SITE_SHOULD_EXIST, **kwargs)

    def sites_site_should_not_exist(self, element_name, site_name, **kwargs):
        """Returns the result of sites_site_should_not_exist."""
        args = {"site_name": site_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_SITE_SHOULD_NOT_EXIST, **kwargs)

    def sites_add_ap_to_site(self, element_name, site_name, ap_name, **kwargs):
        """Returns the result of sites_add_ap_to_site."""
        args = {"site_name": site_name,
                "ap_name": ap_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_ADD_AP_TO_SITE, **kwargs)

    def sites_remove_ap_from_site(self, element_name, site_name, ap_name, **kwargs):
        """Returns the result of sites_remove_ap_from_site."""
        args = {"site_name": site_name,
                "ap_name": ap_name}

        return self.execute_keyword(element_name, args, self.command_const.SITES_REMOVE_AP_FROM_SITE, **kwargs)

    def sites_add_wlan_radios_to_site(self, element_name, site_name, wlan_name, radio, **kwargs):
        """Returns the result of sites_add_wlan_radios_to_site."""
        args = {"site_name": site_name,
                "wlan_name": wlan_name,
                "radio": radio}

        return self.execute_keyword(element_name, args, self.command_const.SITES_ADD_WLAN_RADIOS_TO_SITE, **kwargs)

    def sites_remove_wlan_radios_from_site(self, element_name, site_name, wlan_name, radio, **kwargs):
        """Returns the result of sites_remove_wlan_radios_from_site."""
        args = {"site_name": site_name,
                "wlan_name": wlan_name,
                "radio": radio}

        return self.execute_keyword(element_name, args, self.command_const.SITES_REMOVE_WLAN_RADIOS_FROM_SITE, **kwargs)

    def sites_add_default_dns_server_to_site(self, element_name, site_name, dns_ip, **kwargs):
        """Returns the result of sites_add_."""
        args = {"site_name": site_name,
                "dns_ip": dns_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_ADD_DEFAULT_DNS_SERVER_TO_SITE, **kwargs)

    def sites_ap_should_be_enabled_for_site(self, element_name, site_name, ap_name, **kwargs):
        """Returns the result of sites_ap_should_be_enabled_for_site."""
        args = {"site_name": site_name,
                "ap_name": ap_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_AP_SHOULD_BE_ENABLED_FOR_SITE, **kwargs)

    def sites_wlan_should_be_enabled_for_site(self, element_name, site_name, wlan_name, **kwargs):
        """Returns the result of sites_wlan_should_be_enabled_for_site."""
        args = {"site_name": site_name,
                "wlan_name": wlan_name}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_WLAN_SHOULD_BE_ENABLED_FOR_SITE, **kwargs)

    def sites_validate_default_dns_server_ip_for_site(self, element_name, site_name, dns_ip, **kwargs):
        """Returns the result of sites_validate_."""
        args = {"site_name": site_name,
                "dns_ip": dns_ip}

        return self.execute_keyword(element_name, args,
                                    self.command_const.SITES_VALIDATE_DEFAULT_DNS_SERVER_IP_FOR_SITE,
                                    **kwargs)
