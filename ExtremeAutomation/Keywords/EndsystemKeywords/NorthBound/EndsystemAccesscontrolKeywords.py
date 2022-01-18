"""
Keyword class for all accesscontrol northbound commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.EndsystemKeywordBaseClass import EndsystemKeywordBaseClass
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.Constants.AccesscontrolConstants import \
    AccesscontrolConstants as ParseConstants
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.Constants.AccesscontrolConstants import \
    AccesscontrolConstants as CommandConstants


class EndsystemAccesscontrolKeywords(EndsystemKeywordBaseClass):
    def __init__(self):
        super(EndsystemAccesscontrolKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "accesscontrol"

    def verify_show_accesscontrol_nacversion(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_nacversion."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_NACVERSION,
                                           self.parse_const.SHOW_ACCESSCONTROL_NACVERSION,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_addendsystemgroupinfos(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_addendsystemgroupinfos."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ADDENDSYSTEMGROUPINFOS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ADDENDSYSTEMGROUPINFOS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_allappliancegroups(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_allappliancegroups."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLAPPLIANCEGROUPS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLAPPLIANCEGROUPS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_alldevice_types_includediscoveredtypes(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_alldevice_types_includediscoveredtypes."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLDEVICE_TYPES_INCLUDEDISCOVEREDTYPES,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLDEVICE_TYPES_INCLUDEDISCOVEREDTYPES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_alldevice_types(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_alldevice_types."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLDEVICE_TYPES,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLDEVICE_TYPES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_allendsystemmacs(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_allendsystemmacs."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLENDSYSTEMMACS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLENDSYSTEMMACS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_allendsystems(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_allendsystems."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLENDSYSTEMS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLENDSYSTEMS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_allgroupinfos(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_allgroupinfos."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLGROUPINFOS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLGROUPINFOS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_allgroupnames(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_allgroupnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLGROUPNAMES,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLGROUPNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_allgroups(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_allgroups."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ALLGROUPS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ALLGROUPS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_appliancegroup(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_appliancegroup."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_APPLIANCEGROUP,
                                           self.parse_const.SHOW_ACCESSCONTROL_APPLIANCEGROUP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_canconnectstart(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_canconnectstart."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_CANCONNECTSTART,
                                           self.parse_const.SHOW_ACCESSCONTROL_CANCONNECTSTART,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_canfusionstart(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_canfusionstart."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_CANFUSIONSTART,
                                           self.parse_const.SHOW_ACCESSCONTROL_CANFUSIONSTART,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_checkforassesmentupdates(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_checkforassesmentupdates."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_CHECKFORASSESMENTUPDATES,
                                           self.parse_const.SHOW_ACCESSCONTROL_CHECKFORASSESMENTUPDATES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystemandhrbymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystemandhrbymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMANDHRBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMANDHRBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystembyip(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystembyip."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMBYIP,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMBYIP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystembymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystembymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystemcategorygroup(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystemcategorygroup."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMCATEGORYGROUP,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMCATEGORYGROUP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystemcategorygroupnames(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystemcategorygroupnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMCATEGORYGROUPNAMES,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMCATEGORYGROUPNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endhealthresultdetails(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endhealthresultdetails."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDHEALTHRESULTDETAILS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDHEALTHRESULTDETAILS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystemingroups(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystemingroups."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMINGROUPS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMINGROUPS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsysteminfoarrbymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsysteminfoarrbymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMINFOARRBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMINFOARRBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsysteminfobymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsysteminfobymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMINFOBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMINFOBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_endsystemsbymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_endsystemsbymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENDSYSTEMSBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENDSYSTEMSBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_enginestatus(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_enginestatus."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_ENGINESTATUS,
                                           self.parse_const.SHOW_ACCESSCONTROL_ENGINESTATUS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_extendedendsystemarrbymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_extendedendsystemarrbymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_EXTENDEDENDSYSTEMARRBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_EXTENDEDENDSYSTEMARRBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_extendedendsystembymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_extendedendsystembymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_EXTENDEDENDSYSTEMBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_EXTENDEDENDSYSTEMBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_group(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_group."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_GROUP,
                                           self.parse_const.SHOW_ACCESSCONTROL_GROUP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_groupcategory(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_groupcategory."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_GROUPCATEGORY,
                                           self.parse_const.SHOW_ACCESSCONTROL_GROUPCATEGORY,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_groupinfobyname(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_groupinfobyname."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_GROUPINFOBYNAME,
                                           self.parse_const.SHOW_ACCESSCONTROL_GROUPINFOBYNAME,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_groupnamesbytype(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_groupnamesbytype."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_GROUPNAMESBYTYPE,
                                           self.parse_const.SHOW_ACCESSCONTROL_GROUPNAMESBYTYPE,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_ldapconfigs(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_ldapconfigs."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_LDAPCONFIGS,
                                           self.parse_const.SHOW_ACCESSCONTROL_LDAPCONFIGS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_localuser(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_localuser."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_LOCALUSER,
                                           self.parse_const.SHOW_ACCESSCONTROL_LOCALUSER,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_locationcategorygroup(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_locationcategorygroup."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_LOCATIONCATEGORYGROUP,
                                           self.parse_const.SHOW_ACCESSCONTROL_LOCATIONCATEGORYGROUP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_locationcategorygroupnames(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_locationcategorygroupnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_LOCATIONCATEGORYGROUPNAMES,
                                           self.parse_const.SHOW_ACCESSCONTROL_LOCATIONCATEGORYGROUPNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_nacconfiguration(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_nacconfiguration."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_NACCONFIGURATION,
                                           self.parse_const.SHOW_ACCESSCONTROL_NACCONFIGURATION,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_radiusservers(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_radiusservers."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_RADIUSSERVERS,
                                           self.parse_const.SHOW_ACCESSCONTROL_RADIUSSERVERS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_registereddevicesbymacaddress(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_registereddevicesbymacaddress."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_REGISTEREDDEVICESBYMACADDRESS,
                                           self.parse_const.SHOW_ACCESSCONTROL_REGISTEREDDEVICESBYMACADDRESS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_registereddevicesbyusername(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_registereddevicesbyusername."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_REGISTEREDDEVICESBYUSERNAME,
                                           self.parse_const.SHOW_ACCESSCONTROL_REGISTEREDDEVICESBYUSERNAME,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_registeredusersbymacaddress(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_registeredusersbymacaddress."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_REGISTEREDUSERSBYMACADDRESS,
                                           self.parse_const.SHOW_ACCESSCONTROL_REGISTEREDUSERSBYMACADDRESS,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_registeredusersbyusername(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_registeredusersbyusername."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_REGISTEREDUSERSBYUSERNAME,
                                           self.parse_const.SHOW_ACCESSCONTROL_REGISTEREDUSERSBYUSERNAME,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_registrationgroupnames(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_registrationgroupnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_REGISTRATIONGROUPNAMES,
                                           self.parse_const.SHOW_ACCESSCONTROL_REGISTRATIONGROUPNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_registrationgroupnamesbymac(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_registrationgroupnamesbymac."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_REGISTRATIONGROUPNAMESBYMAC,
                                           self.parse_const.SHOW_ACCESSCONTROL_REGISTRATIONGROUPNAMESBYMAC,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_timecategorygroup(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_timecategorygroup."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_TIMECATEGORYGROUP,
                                           self.parse_const.SHOW_ACCESSCONTROL_TIMECATEGORYGROUP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_timecategorygroupnames(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_timecategorygroupnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_TIMECATEGORYGROUPNAMES,
                                           self.parse_const.SHOW_ACCESSCONTROL_TIMECATEGORYGROUPNAMES,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_usercategorygroup(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_usercategorygroup."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_USERCATEGORYGROUP,
                                           self.parse_const.SHOW_ACCESSCONTROL_USERCATEGORYGROUP,
                                           True, "PASSED", "FAILED", **kwargs)

    def verify_show_accesscontrol_usercategorygroupnames(self, device_name, **kwargs):
        """Verifies the output from show_accesscontrol_usercategorygroupnames."""
        return self.execute_verify_keyword(device_name, kwargs,
                                           self.cmd_const.SHOW_ACCESSCONTROL_USERCATEGORYGROUPNAMES,
                                           self.parse_const.SHOW_ACCESSCONTROL_USERCATEGORYGROUPNAMES,
                                           True, "PASSED", "FAILED", **kwargs)
