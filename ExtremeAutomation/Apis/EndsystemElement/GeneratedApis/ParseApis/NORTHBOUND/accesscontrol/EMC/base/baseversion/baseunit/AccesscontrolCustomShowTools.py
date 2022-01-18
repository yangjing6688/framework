from ExtremeAutomation.Library.Device.Common.Apis.BaseShowApi import NorthboundResults
from ExtremeAutomation.Apis.EndsystemElement.GeneratedApis.ParseApis.NORTHBOUND.accesscontrol.base.\
    AccesscontrolBaseCustomShowTools import AccesscontrolBaseCustomShowTools


class AccesscontrolCustomShowTools(AccesscontrolBaseCustomShowTools):
    def show_accesscontrol_nacversion(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['NACVersion'], args['nacversion'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_addendsystemgroupinfos(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['addEndSystemGroupInfos']['description'], args['description'])
            result.add_result(output['data']['accessControl']['addEndSystemGroupInfos']['dynamic'], args['dynamic'])
            result.add_result(output['data']['accessControl']['addEndSystemGroupInfos']['name'], args['name'])
            result.add_result(output['data']['accessControl']['addEndSystemGroupInfos']['type'], args['type'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_allappliancegroups(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allApplianceGroups']['authorizationGroup'], args['authorizationgroup'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['communicationChannel'], args['communicationchannel'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['dbEncryptedRadiusMonitorSharedSecret'], args['dbencryptedradiusmonitorsharedsecret'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['distributedCache'], args['distributedcache'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['distributedLoadBalanceMode'], args['distributedloadbalancemode'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['internalLoadBalancingStr'], args['internalloadbalancingstr'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['loadBalancingEnabled'], args['loadbalancingenabled'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['nacApplianceSettings'], args['nacappliancesettings'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['nacConfiguration'], args['nacconfiguration'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['name'], args['name'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['policyDomain'], args['policydomain'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['radiusMonitorSharedSecret'], args['radiusmonitorsharedsecret'])
            result.add_result(output['data']['accessControl']['allApplianceGroups']['radiusMonitoringEnabled'], args['radiusmonitoringenabled'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_alldevice_types_includediscoveredtypes(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allDeviceTypes'], args['alldevicetypes'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_alldevice_types(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allDeviceTypes'], args['alldevicetypes'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_allendsystemmacs(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allEndSystemMacs'], args['allendsystemmacs'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_allendsystems(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allEndSystems'], args['allendsystems'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_allgroupinfos(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allGroupInfos']['description'], args['description'])
            result.add_result(output['data']['accessControl']['allGroupInfos']['dynamic'], args['dynamic'])
            result.add_result(output['data']['accessControl']['allGroupInfos']['name'], args['name'])
            result.add_result(output['data']['accessControl']['allGroupInfos']['type'], args['type'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_allgroupnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allGroupNames'], args['allgroupnames'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_allgroups(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['allGroups']['GetMode'], args['getmode'])
            result.add_result(output['data']['accessControl']['allGroups']['GetScopeType'], args['getscopetype'])
            result.add_result(output['data']['accessControl']['allGroups']['GetType'], args['gettype'])
            result.add_result(output['data']['accessControl']['allGroups']['createdBy'], args['createdby'])
            result.add_result(output['data']['accessControl']['allGroups']['creationTime'], args['creationtime'])
            result.add_result(output['data']['accessControl']['allGroups']['description'], args['description'])
            result.add_result(output['data']['accessControl']['allGroups']['dynamic'], args['dynamic'])
            result.add_result(output['data']['accessControl']['allGroups']['lastModifiedBy'], args['lastmodifiedby'])
            result.add_result(output['data']['accessControl']['allGroups']['lastModifiedTime'], args['lastmodifiedtime'])
            result.add_result(output['data']['accessControl']['allGroups']['modeStr'], args['modestr'])
            result.add_result(output['data']['accessControl']['allGroups']['name'], args['name'])
            result.add_result(output['data']['accessControl']['allGroups']['outOfSynch'], args['outofsynch'])
            result.add_result(output['data']['accessControl']['allGroups']['revisionCounter'], args['revisioncounter'])
            result.add_result(output['data']['accessControl']['allGroups']['scopeType'], args['scopetype'])
            result.add_result(output['data']['accessControl']['allGroups']['source'], args['source'])
            result.add_result(output['data']['accessControl']['allGroups']['typeStr'], args['typestr'])
            result.add_result(output['data']['accessControl']['allGroups']['zone'], args['zone'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_appliancegroup(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['applianceGroup']['authorizationGroup'], args['authorizationgroup'])
            result.add_result(output['data']['accessControl']['applianceGroup']['communicationChannel'], args['communicationchannel'])
            result.add_result(output['data']['accessControl']['applianceGroup']['dbEncryptedRadiusMonitorSharedSecret'], args['dbencryptedradiusmonitorsharedsecret'])
            result.add_result(output['data']['accessControl']['applianceGroup']['distributedCache'], args['distributedcache'])
            result.add_result(output['data']['accessControl']['applianceGroup']['distributedLoadBalanceMode'], args['distributedloadbalancemode'])
            result.add_result(output['data']['accessControl']['applianceGroup']['internalLoadBalancingStr'], args['internalloadbalancingstr'])
            result.add_result(output['data']['accessControl']['applianceGroup']['loadBalancingEnabled'], args['loadbalancingenabled'])
            result.add_result(output['data']['accessControl']['applianceGroup']['nacApplianceSettings'], args['nacappliancesettings'])
            result.add_result(output['data']['accessControl']['applianceGroup']['nacConfiguration'], args['nacconfiguration'])
            result.add_result(output['data']['accessControl']['applianceGroup']['name'], args['name'])
            result.add_result(output['data']['accessControl']['applianceGroup']['policyDomain'], args['policydomain'])
            result.add_result(output['data']['accessControl']['applianceGroup']['radiusMonitorSharedSecret'], args['radiusmonitorsharedsecret'])
            result.add_result(output['data']['accessControl']['applianceGroup']['radiusMonitoringEnabled'], args['radiusmonitoringenabled'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_canconnectstart(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['canConnectStart'], args['canconnectstart'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_canfusionstart(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['canFusionStart'], args['canfusionstart'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_checkforassesmentupdates(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['checkForAssessmentUpdates'], args['checkforassessmentupdates'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystemandhrbymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemAndHrByMac'], args['endsystemandhrbymac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystembyip(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemByIp']['endSystemSwitchSupportsReauth'], args['endsystemswitchsupportsreauth'])
            result.add_result(output['data']['accessControl']['endSystemByIp']['errorCode'], args['errorcode'])
            result.add_result(output['data']['accessControl']['endSystemByIp']['errorMessage'], args['errormessage'])
            result.add_result(output['data']['accessControl']['endSystemByIp']['success'], args['success'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystembymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemByMac']['endSystemSwitchSupportsReauth'], args['endsystemswitchsupportsreauth'])
            result.add_result(output['data']['accessControl']['endSystemByMac']['errorCode'], args['errorcode'])
            result.add_result(output['data']['accessControl']['endSystemByMac']['errorMessage'], args['errormessage'])
            result.add_result(output['data']['accessControl']['endSystemByMac']['success'], args['success'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystemcategorygroup(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemCategoryGroup'], args['endsystemcategorygroup'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystemcategorygroupnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemCategoryGroupNames'], args['endsystemcategorygroupnames'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endhealthresultdetails(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemHealthResultDetails'], args['endsystemhealthresultdetails'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystemingroups(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemInGroups']['description'], args['description'])
            result.add_result(output['data']['accessControl']['endSystemInGroups']['dynamic'], args['dynamic'])
            result.add_result(output['data']['accessControl']['endSystemInGroups']['name'], args['name'])
            result.add_result(output['data']['accessControl']['endSystemInGroups']['type'], args['type'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsysteminfoarrbymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemInfoArrByMac'], args['endsysteminfoarrbymac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsysteminfobymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemInfoByMac']['errorCode'], args['errorcode'])
            result.add_result(output['data']['accessControl']['endSystemInfoByMac']['errorMessage'], args['errormessage'])
            result.add_result(output['data']['accessControl']['endSystemInfoByMac']['success'], args['success'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_endsystemsbymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['endSystemsByMac']['errorCode'], args['errorcode'])
            result.add_result(output['data']['accessControl']['endSystemsByMac']['errorMessage'], args['errormessage'])
            result.add_result(output['data']['accessControl']['endSystemsByMac']['success'], args['success'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_enginestatus(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['engineStatus'], args['enginestatus'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_extendedendsystemarrbymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['extendedEndSystemArrByMac'], args['extendedendsystemarrbymac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_extendedendsystembymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['extendedEndSystemByMac'], args['extendedendsystembymac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_group(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['group']['GetMode'], args['getmode'])
            result.add_result(output['data']['accessControl']['group']['GetScopeType'], args['getscopetype'])
            result.add_result(output['data']['accessControl']['group']['GetType'], args['gettype'])
            result.add_result(output['data']['accessControl']['group']['createdBy'], args['createdby'])
            result.add_result(output['data']['accessControl']['group']['creationTime'], args['creationtime'])
            result.add_result(output['data']['accessControl']['group']['description'], args['description'])
            result.add_result(output['data']['accessControl']['group']['dynamic'], args['dynamic'])
            result.add_result(output['data']['accessControl']['group']['lastModifiedBy'], args['lastmodifiedby'])
            result.add_result(output['data']['accessControl']['group']['lastModifiedTime'], args['lastmodifiedtime'])
            result.add_result(output['data']['accessControl']['group']['modeStr'], args['modestr'])
            result.add_result(output['data']['accessControl']['group']['name'], args['name'])
            result.add_result(output['data']['accessControl']['group']['outOfSynch'], args['outofsynch'])
            result.add_result(output['data']['accessControl']['group']['revisionCounter'], args['revisioncounter'])
            result.add_result(output['data']['accessControl']['group']['scopeType'], args['scopetype'])
            result.add_result(output['data']['accessControl']['group']['source'], args['source'])
            result.add_result(output['data']['accessControl']['group']['typeStr'], args['typestr'])
            result.add_result(output['data']['accessControl']['group']['zone'], args['zone'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_groupcategory(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['groupCategory'], args['groupcategory'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_groupinfobyname(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['groupInfoByName']['description'], args['description'])
            result.add_result(output['data']['accessControl']['groupInfoByName']['dynamic'], args['dynamic'])
            result.add_result(output['data']['accessControl']['groupInfoByName']['name'], args['name'])
            result.add_result(output['data']['accessControl']['groupInfoByName']['type'], args['type'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_groupnamesbytype(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['groupNamesByType'], args['groupnamesbytype'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_ldapconfigs(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['ldapConfigs']['GetLdapAuthType'], args['getldapauthtype'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['OUObjectClass'], args['ouobjectclass'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['adminPassword'], args['adminpassword'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['adminUsername'], args['adminusername'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['connectionURL'], args['connectionurl'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['hostObjectClass'], args['hostobjectclass'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['hostSearchAttribute'], args['hostsearchattribute'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['hostSearchRoot'], args['hostsearchroot'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['includeDomNameForHost'], args['includedomnameforhost'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['includeDomNameForUser'], args['includedomnameforuser'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['ldapAuthTypeStr'], args['ldapauthtypestr'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['ldapPasswordAttribute'], args['ldappasswordattribute'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['name'], args['name'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['ouSearchRoot'], args['ousearchroot'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['timeoutInSecs'], args['timeoutinsecs'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['userObjecClass'], args['userobjecclass'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['userSearchAttribute'], args['usersearchattribute'])
            result.add_result(output['data']['accessControl']['ldapConfigs']['userSearchRoot'], args['usersearchroot'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_localuser(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['localUser']['errorCode'], args['errorcode'])
            result.add_result(output['data']['accessControl']['localUser']['errorMessage'], args['errormessage'])
            result.add_result(output['data']['accessControl']['localUser']['success'], args['success'])
            result.add_result(output['data']['accessControl']['localUser']['tableTotalRecords'], args['tabletotalrecords'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_locationcategorygroup(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['locationCategoryGroup'], args['locationcategorygroup'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_locationcategorygroupnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['locationCategoryGroupNames'], args['locationcategorygroupnames'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_nacconfiguration(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['nacConfiguration']['aaaConfiguration'], args['aaaconfiguration'])
            result.add_result(output['data']['accessControl']['nacConfiguration']['name'], args['name'])
            result.add_result(output['data']['accessControl']['nacConfiguration']['portalConfiguration'], args['portalconfiguration'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_radiusservers(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['radiusServers']['GetAuthAccessType'], args['getauthaccesstype'])
            result.add_result(output['data']['accessControl']['radiusServers']['accessRequestPassword'], args['accessrequestpassword'])
            result.add_result(output['data']['accessControl']['radiusServers']['accessRequestUsername'], args['accessrequestusername'])
            result.add_result(output['data']['accessControl']['radiusServers']['acctPort'], args['acctport'])
            result.add_result(output['data']['accessControl']['radiusServers']['authPort'], args['authport'])
            result.add_result(output['data']['accessControl']['radiusServers']['checkInterval'], args['checkinterval'])
            result.add_result(output['data']['accessControl']['radiusServers']['disableAccessRequest'], args['disableaccessrequest'])
            result.add_result(output['data']['accessControl']['radiusServers']['disableServerStatus'], args['disableserverstatus'])
            result.add_result(output['data']['accessControl']['radiusServers']['enable'], args['enable'])
            result.add_result(output['data']['accessControl']['radiusServers']['ipAddress'], args['ipaddress'])
            result.add_result(output['data']['accessControl']['radiusServers']['keepDomainName'], args['keepdomainname'])
            result.add_result(output['data']['accessControl']['radiusServers']['numberOfAnswersUntilAlive'], args['numberofanswersuntilalive'])
            result.add_result(output['data']['accessControl']['radiusServers']['radiusAccountingEnabled'], args['radiusaccountingenabled'])
            result.add_result(output['data']['accessControl']['radiusServers']['requireMessageAuthenticator'], args['requiremessageauthenticator'])
            result.add_result(output['data']['accessControl']['radiusServers']['responseWindow'], args['responsewindow'])
            result.add_result(output['data']['accessControl']['radiusServers']['retries'], args['retries'])
            result.add_result(output['data']['accessControl']['radiusServers']['reviveInterval'], args['reviveinterval'])
            result.add_result(output['data']['accessControl']['radiusServers']['sharedSecret'], args['sharedsecret'])
            result.add_result(output['data']['accessControl']['radiusServers']['timeout'], args['timeout'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_registereddevicesbymacaddress(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['registeredDevicesByMacAddress'], args['registereddevicesbymacaddress'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_registereddevicesbyusername(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['registeredDevicesByUsername'], args['registereddevicesbyusername'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_registeredusersbymacaddress(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['registeredUsersByMacAddress'], args['registeredusersbymacaddress'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_registeredusersbyusername(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['registeredUsersByUsername'], args['registeredusersbyusername'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_registrationgroupnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['registrationGroupNames'], args['registrationgroupnames'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_registrationgroupnamesbymac(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['registrationGroupNamesByMac'], args['registrationgroupnamesbymac'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_timecategorygroup(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['timeCategoryGroup'], args['timecategorygroup'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_timecategorygroupnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['timeCategoryGroupNames'], args['timecategorygroupnames'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_usercategorygroup(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['userCategoryGroup'], args['usercategorygroup'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False

    def show_accesscontrol_usercategorygroupnames(self, output, args, **kwargs):
        try:
            result = NorthboundResults()
            result.add_result(output['data']['accessControl']['userCategoryGroupNames'], args['usercategorygroupnames'])
            return result.return_result()
        except KeyError:
            self.logger.log_info("KEY ERROR")
            return False
