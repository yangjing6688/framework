"""
Base class for all accesscontrol northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject


class AccesscontrolBase(BaseApi):
    def __init__(self, device):
        self.device = device

        def show_accesscontrol_nacversion(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_addendsystemgroupinfos(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_allappliancegroups(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_alldevice_types_includediscoveredtypes(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_alldevice_types(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_allendsystemmacs(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_allendsystems(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_allgroupinfos(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_allgroupnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_allgroups(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_appliancegroup(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_canconnectstart(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_canfusionstart(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_checkforassesmentupdates(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystemandhrbymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystembyip(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystembymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystemcategorygroup(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystemcategorygroupnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endhealthresultdetails(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystemingroups(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsysteminfoarrbymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsysteminfobymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_endsystemsbymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_enginestatus(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_extendedendsystemarrbymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_extendedendsystembymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_group(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_groupcategory(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_groupinfobyname(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_groupnamesbytype(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_ldapConfigs(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_localuser(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_locationcategorygroup(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_locationcategorygroupnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_nacconfiguration(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_radiusservers(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_registereddevicesbymacaddress(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_registereddevicesbyusername(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_registeredusersbymacaddress(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_registeredusersbyusername(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_registrationgroupnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_registrationgroupnamesbymac(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_timecategorygroup(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_timecategorygroupnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_usercategorygroup(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request

        def show_accesscontrol_usercategorygroupnames(self, data_dict):
            rest_request = RestCommandObject()
            rest_request.not_supported = True

            return rest_request
