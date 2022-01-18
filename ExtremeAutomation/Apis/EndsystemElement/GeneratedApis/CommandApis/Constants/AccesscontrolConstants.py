"""
This class outlines all the constants for the accesscontrol API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(AccesscontrolConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class AccesscontrolConstants(ApiConstants):
    def __init__(self):
        super(AccesscontrolConstants, self).__init__()
        self.SHOW_ACCESSCONTROL_ADDENDSYSTEMGROUPINFOS = {"constant": "show_accesscontrol_addendsystemgroupinfos",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_addendsystemgroupinfos}
        self.SHOW_ACCESSCONTROL_ALLAPPLIANCEGROUPS = {"constant": "show_accesscontrol_allappliancegroups",
                                                      "tags": ["COMMAND_NORTHBOUND"],
                                                      "link": self.link.show_accesscontrol_allappliancegroups}
        self.SHOW_ACCESSCONTROL_ALLDEVICE_TYPES = {"constant": "show_accesscontrol_alldevice_types",
                                                   "tags": ["COMMAND_NORTHBOUND"],
                                                   "link": self.link.show_accesscontrol_alldevice_types}
        self.SHOW_ACCESSCONTROL_ALLDEVICE_TYPES_INCLUDEDISCOVEREDTYPES = {"constant": "show_accesscontrol_alldevice_types_includediscoveredtypes",
                                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                                          "link": self.link.show_accesscontrol_alldevice_types_includediscoveredtypes}
        self.SHOW_ACCESSCONTROL_ALLENDSYSTEMMACS = {"constant": "show_accesscontrol_allendsystemmacs",
                                                    "tags": ["COMMAND_NORTHBOUND"],
                                                    "link": self.link.show_accesscontrol_allendsystemmacs}
        self.SHOW_ACCESSCONTROL_ALLENDSYSTEMS = {"constant": "show_accesscontrol_allendsystems",
                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                 "link": self.link.show_accesscontrol_allendsystems}
        self.SHOW_ACCESSCONTROL_ALLGROUPINFOS = {"constant": "show_accesscontrol_allgroupinfos",
                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                 "link": self.link.show_accesscontrol_allgroupinfos}
        self.SHOW_ACCESSCONTROL_ALLGROUPNAMES = {"constant": "show_accesscontrol_allgroupnames",
                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                 "link": self.link.show_accesscontrol_allgroupnames}
        self.SHOW_ACCESSCONTROL_ALLGROUPS = {"constant": "show_accesscontrol_allgroups",
                                             "tags": ["COMMAND_NORTHBOUND"],
                                             "link": self.link.show_accesscontrol_allgroups}
        self.SHOW_ACCESSCONTROL_APPLIANCEGROUP = {"constant": "show_accesscontrol_appliancegroup",
                                                  "tags": ["COMMAND_NORTHBOUND"],
                                                  "link": self.link.show_accesscontrol_appliancegroup}
        self.SHOW_ACCESSCONTROL_CANCONNECTSTART = {"constant": "show_accesscontrol_canconnectstart",
                                                   "tags": ["COMMAND_NORTHBOUND"],
                                                   "link": self.link.show_accesscontrol_canconnectstart}
        self.SHOW_ACCESSCONTROL_CANFUSIONSTART = {"constant": "show_accesscontrol_canfusionstart",
                                                  "tags": ["COMMAND_NORTHBOUND"],
                                                  "link": self.link.show_accesscontrol_canfusionstart}
        self.SHOW_ACCESSCONTROL_CHECKFORASSESMENTUPDATES = {"constant": "show_accesscontrol_checkforassesmentupdates",
                                                            "tags": ["COMMAND_NORTHBOUND"],
                                                            "link": self.link.show_accesscontrol_checkforassesmentupdates}
        self.SHOW_ACCESSCONTROL_ENDHEALTHRESULTDETAILS = {"constant": "show_accesscontrol_endhealthresultdetails",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_endhealthresultdetails}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMANDHRBYMAC = {"constant": "show_accesscontrol_endsystemandhrbymac",
                                                       "tags": ["COMMAND_NORTHBOUND"],
                                                       "link": self.link.show_accesscontrol_endsystemandhrbymac}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMBYIP = {"constant": "show_accesscontrol_endsystembyip",
                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                 "link": self.link.show_accesscontrol_endsystembyip}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMBYMAC = {"constant": "show_accesscontrol_endsystembymac",
                                                  "tags": ["COMMAND_NORTHBOUND"],
                                                  "link": self.link.show_accesscontrol_endsystembymac}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMCATEGORYGROUP = {"constant": "show_accesscontrol_endsystemcategorygroup",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_endsystemcategorygroup}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMCATEGORYGROUPNAMES = {"constant": "show_accesscontrol_endsystemcategorygroupnames",
                                                               "tags": ["COMMAND_NORTHBOUND"],
                                                               "link": self.link.show_accesscontrol_endsystemcategorygroupnames}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMINFOARRBYMAC = {"constant": "show_accesscontrol_endsysteminfoarrbymac",
                                                         "tags": ["COMMAND_NORTHBOUND"],
                                                         "link": self.link.show_accesscontrol_endsysteminfoarrbymac}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMINFOBYMAC = {"constant": "show_accesscontrol_endsysteminfobymac",
                                                      "tags": ["COMMAND_NORTHBOUND"],
                                                      "link": self.link.show_accesscontrol_endsysteminfobymac}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMINGROUPS = {"constant": "show_accesscontrol_endsystemingroups",
                                                     "tags": ["COMMAND_NORTHBOUND"],
                                                     "link": self.link.show_accesscontrol_endsystemingroups}
        self.SHOW_ACCESSCONTROL_ENDSYSTEMSBYMAC = {"constant": "show_accesscontrol_endsystemsbymac",
                                                   "tags": ["COMMAND_NORTHBOUND"],
                                                   "link": self.link.show_accesscontrol_endsystemsbymac}
        self.SHOW_ACCESSCONTROL_ENGINESTATUS = {"constant": "show_accesscontrol_enginestatus",
                                                "tags": ["COMMAND_NORTHBOUND"],
                                                "link": self.link.show_accesscontrol_enginestatus}
        self.SHOW_ACCESSCONTROL_EXTENDEDENDSYSTEMARRBYMAC = {"constant": "show_accesscontrol_extendedendsystemarrbymac",
                                                             "tags": ["COMMAND_NORTHBOUND"],
                                                             "link": self.link.show_accesscontrol_extendedendsystemarrbymac}
        self.SHOW_ACCESSCONTROL_EXTENDEDENDSYSTEMBYMAC = {"constant": "show_accesscontrol_extendedendsystembymac",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_extendedendsystembymac}
        self.SHOW_ACCESSCONTROL_GROUP = {"constant": "show_accesscontrol_group",
                                         "tags": ["COMMAND_NORTHBOUND"],
                                         "link": self.link.show_accesscontrol_group}
        self.SHOW_ACCESSCONTROL_GROUPCATEGORY = {"constant": "show_accesscontrol_groupcategory",
                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                 "link": self.link.show_accesscontrol_groupcategory}
        self.SHOW_ACCESSCONTROL_GROUPINFOBYNAME = {"constant": "show_accesscontrol_groupinfobyname",
                                                   "tags": ["COMMAND_NORTHBOUND"],
                                                   "link": self.link.show_accesscontrol_groupinfobyname}
        self.SHOW_ACCESSCONTROL_GROUPNAMESBYTYPE = {"constant": "show_accesscontrol_groupnamesbytype",
                                                    "tags": ["COMMAND_NORTHBOUND"],
                                                    "link": self.link.show_accesscontrol_groupnamesbytype}
        self.SHOW_ACCESSCONTROL_LDAPCONFIGS = {"constant": "show_accesscontrol_ldapConfigs",
                                               "tags": ["COMMAND_NORTHBOUND"],
                                               "link": self.link.show_accesscontrol_ldapConfigs}
        self.SHOW_ACCESSCONTROL_LOCALUSER = {"constant": "show_accesscontrol_localuser",
                                             "tags": ["COMMAND_NORTHBOUND"],
                                             "link": self.link.show_accesscontrol_localuser}
        self.SHOW_ACCESSCONTROL_LOCATIONCATEGORYGROUP = {"constant": "show_accesscontrol_locationcategorygroup",
                                                         "tags": ["COMMAND_NORTHBOUND"],
                                                         "link": self.link.show_accesscontrol_locationcategorygroup}
        self.SHOW_ACCESSCONTROL_LOCATIONCATEGORYGROUPNAMES = {"constant": "show_accesscontrol_locationcategorygroupnames",
                                                              "tags": ["COMMAND_NORTHBOUND"],
                                                              "link": self.link.show_accesscontrol_locationcategorygroupnames}
        self.SHOW_ACCESSCONTROL_NACCONFIGURATION = {"constant": "show_accesscontrol_nacconfiguration",
                                                    "tags": ["COMMAND_NORTHBOUND"],
                                                    "link": self.link.show_accesscontrol_nacconfiguration}
        self.SHOW_ACCESSCONTROL_NACVERSION = {"constant": "show_accesscontrol_nacversion",
                                              "tags": ["COMMAND_NORTHBOUND"],
                                              "link": self.link.show_accesscontrol_nacversion}
        self.SHOW_ACCESSCONTROL_RADIUSSERVERS = {"constant": "show_accesscontrol_radiusservers",
                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                 "link": self.link.show_accesscontrol_radiusservers}
        self.SHOW_ACCESSCONTROL_REGISTEREDDEVICESBYMACADDRESS = {"constant": "show_accesscontrol_registereddevicesbymacaddress",
                                                                 "tags": ["COMMAND_NORTHBOUND"],
                                                                 "link": self.link.show_accesscontrol_registereddevicesbymacaddress}
        self.SHOW_ACCESSCONTROL_REGISTEREDDEVICESBYUSERNAME = {"constant": "show_accesscontrol_registereddevicesbyusername",
                                                               "tags": ["COMMAND_NORTHBOUND"],
                                                               "link": self.link.show_accesscontrol_registereddevicesbyusername}
        self.SHOW_ACCESSCONTROL_REGISTEREDUSERSBYMACADDRESS = {"constant": "show_accesscontrol_registeredusersbymacaddress",
                                                               "tags": ["COMMAND_NORTHBOUND"],
                                                               "link": self.link.show_accesscontrol_registeredusersbymacaddress}
        self.SHOW_ACCESSCONTROL_REGISTEREDUSERSBYUSERNAME = {"constant": "show_accesscontrol_registeredusersbyusername",
                                                             "tags": ["COMMAND_NORTHBOUND"],
                                                             "link": self.link.show_accesscontrol_registeredusersbyusername}
        self.SHOW_ACCESSCONTROL_REGISTRATIONGROUPNAMES = {"constant": "show_accesscontrol_registrationgroupnames",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_registrationgroupnames}
        self.SHOW_ACCESSCONTROL_REGISTRATIONGROUPNAMESBYMAC = {"constant": "show_accesscontrol_registrationgroupnamesbymac",
                                                               "tags": ["COMMAND_NORTHBOUND"],
                                                               "link": self.link.show_accesscontrol_registrationgroupnamesbymac}
        self.SHOW_ACCESSCONTROL_TIMECATEGORYGROUP = {"constant": "show_accesscontrol_timecategorygroup",
                                                     "tags": ["COMMAND_NORTHBOUND"],
                                                     "link": self.link.show_accesscontrol_timecategorygroup}
        self.SHOW_ACCESSCONTROL_TIMECATEGORYGROUPNAMES = {"constant": "show_accesscontrol_timecategorygroupnames",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_timecategorygroupnames}
        self.SHOW_ACCESSCONTROL_USERCATEGORYGROUP = {"constant": "show_accesscontrol_usercategorygroup",
                                                     "tags": ["COMMAND_NORTHBOUND"],
                                                     "link": self.link.show_accesscontrol_usercategorygroup}
        self.SHOW_ACCESSCONTROL_USERCATEGORYGROUPNAMES = {"constant": "show_accesscontrol_usercategorygroupnames",
                                                          "tags": ["COMMAND_NORTHBOUND"],
                                                          "link": self.link.show_accesscontrol_usercategorygroupnames}
