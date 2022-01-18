from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import BaseShowApi
from ExtremeAutomation.Library.Device.EndsystemElement.Constants.EndsystemElementConstants import EndsystemElementConstants


class AccesscontrolBaseCustomShowTools(BaseShowApi):
    def __init__(self, device):
        super(AccesscontrolBaseCustomShowTools, self).__init__()
        self.device = device

    def show_accesscontrol_nacversion(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_addendsystemgroupinfos(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_allappliancegroups(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_alldevice_types_includediscoveredtypes(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_alldevice_types(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_allendsystemmacs(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_allendsystems(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_allgroupinfos(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_allgroupnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_allgroups(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_appliancegroup(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_canconnectstart(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_canfusionstart(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_checkforassesmentupdates(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystemandhrbymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystembyip(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystembymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystemcategorygroup(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystemcategorygroupnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endhealthresultdetails(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystemingroups(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsysteminfoarrbymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsysteminfobymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_endsystemsbymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_enginestatus(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_extendedendsystemarrbymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_extendedendsystembymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_group(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_groupcategory(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_groupinfobyname(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_groupnamesbytype(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_ldapconfigs(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_localuser(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_locationcategorygroup(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_locationcategorygroupnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_nacconfiguration(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_radiusservers(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_registereddevicesbymacaddress(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_registereddevicesbyusername(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_registeredusersbymacaddress(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_registeredusersbyusername(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_registrationgroupnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_registrationgroupnamesbymac(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_timecategorygroup(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_timecategorygroupnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_usercategorygroup(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED

    def show_accesscontrol_usercategorygroupnames(self, *args):
        return EndsystemElementConstants.METHOD_NOT_SUPPORTED
