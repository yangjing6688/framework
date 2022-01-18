"""
All accesscontrol supported northbound commands.
"""
from ExtremeAutomation.Library.Device.Common.Apis.DeviceApi import DeviceApi
from ExtremeAutomation.Library.Device.Common.CommandObjects.RestCommandObject import RestCommandObject
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.CommandApis.NORTHBOUND.accesscontrol.base.accesscontrolbase \
    import AccesscontrolBase


class Accesscontrol(DeviceApi, AccesscontrolBase):
    def __init__(self, device):
        super(Accesscontrol, self).__init__(device)

    def show_accesscontrol_nacversion(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{NACVersion}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_addendsystemgroupinfos(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{addEndSystemGroupInfos{description dynamic name type}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_allappliancegroups(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allApplianceGroups{authorizationGroup communicationChannel dbEncryptedRadiusMonitorSharedSecret distributedCache distributedLoadBalanceMode internalLoadBalancingStr loadBalancingEnabled nacApplianceSettings nacConfiguration name policyDomain radiusMonitorSharedSecret radiusMonitoringEnabled}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_alldevice_types_includediscoveredtypes(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allDeviceTypes(includeDiscoveredTypes:true)}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_alldevice_types(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allDeviceTypes(includeDiscoveredTypes:false)}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_allendsystemmacs(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allEndSystemMacs}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_allendsystems(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allEndSystems}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_allgroupinfos(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allGroupInfos{description dynamic name type}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_allgroupnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allGroupNames}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_allgroups(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{allGroups{GetMode GetScopeType GetType createdBy creationTime description dynamic lastModifiedBy lastModifiedTime modeStr name outOfSynch revisionCounter scopeType source typeStr zone}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_appliancegroup(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{applianceGroup{authorizationGroup communicationChannel dbEncryptedRadiusMonitorSharedSecret distributedCache distributedLoadBalanceMode internalLoadBalancingStr loadBalancingEnabled nacApplianceSettings nacConfiguration name policyDomain radiusMonitorSharedSecret radiusMonitoringEnabled}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_canconnectstart(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{canConnectStart}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_canfusionstart(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{canFusionStart}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_checkforassesmentupdates(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{checkForAssessmentUpdates}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystemandhrbymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemAndHrByMac}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystembyip(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemByIp{endSystemSwitchSupportsReauth errorCode errorMessage success}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystembymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemByMac{endSystemSwitchSupportsReauth errorCode errorMessage success}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystemcategorygroup(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemCategoryGroup}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystemcategorygroupnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemCategoryGroupNames}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endhealthresultdetails(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemHealthResultDetails}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystemingroups(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemInGroups{description dynamic name type}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsysteminfoarrbymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemInfoArrByMac}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsysteminfobymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemInfoByMac{errorCode errorMessage success}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_endsystemsbymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{endSystemsByMac{errorCode errorMessage success}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_enginestatus(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{engineStatus}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_extendedendsystemarrbymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{extendedEndSystemArrByMac}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_extendedendsystembymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{extendedEndSystemByMac}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_group(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{group{GetMode GetScopeType GetType createdBy creationTime description dynamic lastModifiedBy lastModifiedTime modeStr name outOfSynch revisionCounter scopeType source typeStr zone}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_groupcategory(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{groupCategory}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_groupinfobyname(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{groupInfoByName{description dynamic name type}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_groupnamesbytype(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{groupNamesByType}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_ldapConfigs(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{ldapConfigs{GetLdapAuthType OUObjectClass adminPassword adminUsername connectionURL hostObjectClass hostSearchAttribute hostSearchRoot includeDomNameForHost includeDomNameForUser ldapAuthTypeStr ldapPasswordAttribute name ouSearchRoot timeoutInSecs userObjecClass userSearchAttribute userSearchRoot}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_localuser(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{localUser { errorCode errorMessage success tableTotalRecords}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_locationcategorygroup(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{locationCategoryGroup}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_locationcategorygroupnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{locationCategoryGroupNames}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_nacconfiguration(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{nacConfiguration {aaaConfiguration name portalConfiguration}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_radiusservers(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{radiusServers{ GetAuthAccessType accessRequestPassword accessRequestUsername acctPort authPort checkInterval disableAccessRequest disableServerStatus enable ipAddress keepDomainName numberOfAnswersUntilAlive radiusAccountingEnabled requireMessageAuthenticator responseWindow retries reviveInterval sharedSecret timeout}}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_registereddevicesbymacaddress(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{registeredDevicesByMacAddress}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_registereddevicesbyusername(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{registeredDevicesByUsername}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_registeredusersbymacaddress(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{registeredUsersByMacAddress}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_registeredusersbyusername(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{registeredUsersByUsername}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_registrationgroupnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{registrationGroupNames}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_registrationgroupnamesbymac(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{registrationGroupNamesByMac}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_timecategorygroup(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{timeCategoryGroup}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_timecategorygroupnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{timeCategoryGroupNames}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_usercategorygroup(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{userCategoryGroup}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)

    def show_accesscontrol_usercategorygroupnames(self, arg_dict):
        rest_request = RestCommandObject()
        rest_request.uri = "/nbi/graphql/"
        rest_request.data = '{accessControl{userCategoryGroupNames}}'
        rest_request.request_type = "post"

        return self.device.send_command_object(rest_request)
