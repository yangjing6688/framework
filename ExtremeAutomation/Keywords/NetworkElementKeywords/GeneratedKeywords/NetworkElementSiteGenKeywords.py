"""
Keyword class for all site cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.SiteConstants import \
    SiteConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.SiteConstants import \
    SiteConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementSiteGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementSiteGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "site"

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def site_verify_exists(self, device_name, site_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name(s) that should exist on the device.

        Verifies that the given site is configured on the device.
        """
        args = {"site_name": site_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_SITE_EXISTS, True,
                                           "Site: {site_name} exists on {device_name}.",
                                           "Site: {site_name} DOES NOT exist on {device_name}!",
                                           **kwargs)

    def site_verify_does_not_exist(self, device_name, site_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name(s) that should not exist on the device.

        Verifies that the given site is not configured on the device.
        """
        args = {"site_name": site_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_ALL,
                                           self.parse_const.CHECK_SITE_EXISTS, False,
                                           "Site: {site_name} correctly does not exist on {device_name}.",
                                           "Site: {site_name} incorrectly exists on {device_name}!",
                                           **kwargs)

    def site_verify_associated_ap_exists(self, device_name, site_name='', ap_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name on the device.
        [ap_name]     - The AP name that should be associated with the site.

        Verifies that the given AP is associated with the given site on the device.
        """
        args = {"site_name": site_name,
                "ap_name": ap_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DETAIL,
                                           self.parse_const.CHECK_SITE_AP_EXISTS, True,
                                           "Associated AP: {ap_name} exists on {site_name}.",
                                           "Associated AP: {ap_name} DOES NOT exist on {site_name}!",
                                           **kwargs)

    def site_verify_associated_ap_does_not_exist(self, device_name, site_name='', ap_name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name on the device.
        [ap_name]     - The AP name that should not be associated with the site.

        Verifies that the given AP is not associated with the given site on the device.
        """
        args = {"site_name": site_name,
                "ap_name": ap_name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DETAIL,
                                           self.parse_const.CHECK_SITE_AP_EXISTS, False,
                                           "Associated AP: {ap_name} correctly does not exist on {site_name}.",
                                           "Associated AP: {ap_name} incorrectly exists on {site_name}!",
                                           **kwargs)

    def site_verify_dns_server_exists(self, device_name, site_name='', dns_server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name on the device.
        [dns_server]  - The DNS server that should be configured on the site(s).

        Verifies that the given DNS server is configured on the given site(s) on the device.
        """
        args = {"site_name": site_name,
                "dns_server": dns_server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DETAIL,
                                           self.parse_const.CHECK_SITE_DNS_SERVER_EXISTS, True,
                                           "DNS server: {dns_server} exists on {site_name}.",
                                           "DNS server: {dns_server} DOES NOT exist on {site_name}!",
                                           **kwargs)

    def site_verify_dns_server_does_not_exist(self, device_name, site_name='', dns_server='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name on the device.
        [dns_server]  - The DNS server that should not be configured on the site(s).

        Verifies that the given DNS server is not configured on the given site(s) on the device.
        """
        args = {"site_name": site_name,
                "dns_server": dns_server}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DETAIL,
                                           self.parse_const.CHECK_SITE_DNS_SERVER_EXISTS, False,
                                           "DNS server: {dns_server} correctly does not exist on {site_name}.",
                                           "DNS server: {dns_server} incorrectly exists on {site_name}!",
                                           **kwargs)

    def site_verify_associated_wlan_radio_exists(self, device_name, site_name='', wlan_name='', radio_mode='',
                                                 **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword should be run against.
        [site_name]   - The site name on the device.
        [wlan_name]   - The WLAN Service name that should be associated with the site.
        [radio_mode]  - The radio mode that should be configured on the WLAN Service.

        Verifies that the given Radio Mode is configured on the WLAN Service on the given site on the device.
        """
        args = {"site_name": site_name,
                "wlan_name": wlan_name,
                "radio_mode": radio_mode}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_DETAIL,
                                           self.parse_const.CHECK_SITE_WLAN_RADIO_MODE_EXISTS, True,
                                           "Radio mode: {radio_mode} exists on {site_name}.",
                                           "Radio mode: {radio_mode} DOES NOT exist on {site_name}!",
                                           **kwargs)
