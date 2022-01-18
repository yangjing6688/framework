from ExtremeAutomation.Library.Logger.Logger import Logger
import traceback

try:
    from common.Ap import Ap
    from common.Cli import Cli
    from common.Utils import Utils
    from common.AutoActions import AutoActions
    from common.GmailHandler import GmailHandler
    # from common.Iapi import Iapi
    from common.IdentifiAP import IdentifiAP
    from common.ImageAnalysis import ImageAnalysis
    from common.ImageHandler import ImageHandler
    from common.LoadBrowser import LoadBrowser
    from common.Logging import Logging
    from common.Mu import Mu
    from common.Rest import Rest
    from common.Screen import Screen
    from common.ScreenDiff import ScreenDiff
    from common.SNMPTraps import SNMPTraps
    from common.Syslog import Syslog
    from common.TestFlow import TestFlow
    from common.Tshark import Tshark
    from common.WebElementHandler import WebElementHandler
    from common.WindowsMU import WindowsMU
    from common.WingAP import WingAP
    from common.Xapi import Xapi
    from common.tools.remote.LinMuConnect import LinMuConnect
    from common.tools.remote.MacMuConnect import MacMuConnect
    from common.tools.remote.Recording import Recording
    #from common.tools.remote.RFTestClient import RFTestClient
    from common.tools.remote.WinMuConnect import WinMuConnect
    from common.tools.remote.captiveportal.CaptivePortal import CPWebElements
    from common.tools.remote.captiveportal.CPWebElementDefinitions import CPWebElementDefinitions
    from xiq.defs.A3InventoryWebElementsDefs import A3InventoryWebElementsDefs
    from xiq.defs.AccntMgmtWebElementsDefs import AccntMgmtWebElementsDefs
    from xiq.defs.AdspWebElementsDefinitions import AdspWebElementsDefinitions
    from xiq.defs.AdvanceOnboardingDefinitions import AdvanceOnboardingDefinitions
    from xiq.defs.AdvOnboardDefs import AdvOnboardDefs
    from xiq.defs.AlarmsWebElementsDefs import AlarmsWebElementsDefs
    from xiq.defs.APPElementDefs import APPElementDefs
    from xiq.defs.ApplicationSpecificSearchWebElementsDefinition import \
        ApplicationSpecificSearchWebElementsDefinition
    from xiq.defs.ApSpecificSearchWebElementsDefinition import ApSpecificSearchWebElementsDefinition
    from xiq.defs.ClientMonitorWebElementsDefs import ClientMonitorWebElementsDefs
    from xiq.defs.ClientWebElementsDefinitions import ClientWebElementsDefinitions
    from xiq.defs.CommonObjectsWebElementsDefinitions import CommonObjectsWebElementsDefinitions
    from xiq.defs.CommunicationsWebElementDefs import CommunicationsWebElementDefs
    from xiq.defs.CredDistrGrupWebElemntsDefs import CredDistrGrupWebElemntsDefs
    from xiq.defs.Device360WebElementDefs import Device360WebElementDefs
    from xiq.defs.DeviceActionsDefs import DeviceActionsDefs
    from xiq.defs.DeviceCliAccessDefs import DeviceCliAccessDefs
    from xiq.defs.DeviceCommonDefs import DeviceCommonDefs
    from xiq.defs.DeviceConfigDefs import DeviceConfigDefs
    from xiq.defs.DevicesWebElementsDefinitions import DevicesWebElementsDefinitions
    from xiq.defs.DeviceTemplateWebElementsDefinitions import DeviceTemplateWebElementDefinitions
    from xiq.defs.DeviceUpdateDefs import DeviceUpdateDefs
    from xiq.defs.DialogWebElementsDefinitions import DialogWebElementsDefinitions
    from xiq.defs.EventsWebElementsDefs import EventsWebElementsDefs
    from xiq.defs.ExpSettingsWebElementsDefinitions import ExpSettingsWebElementsDefinitions
    from xiq.defs.ExtremeGuestWebElementsDefs import ExtremeGuestWebElementsDefs
    from xiq.defs.ExtremeIOTWebElementsDefs import ExtremeIOTWebElementsDefs
    from xiq.defs.extreme_location.ExtremeLocationWebElementsDefs import ExtremeLocationWebElementsDefs
    from xiq.defs.FilterManageClientDefinitions import FilterManageClientDefinitions
    from xiq.defs.FilterManageDeviceDefinitions import FilterManageDeviceDefinitions
    from xiq.defs.GlobalSearchWebElementsDefinitions import GlobalSearchWebElementsDefinitions
    from xiq.defs.GlobalSettingWebElementDefinitions import GlobalSettingWebElementDefinitions
    from xiq.defs.GuestAccessNetworkWebElementsDefinitions import GuestAccessNetworkWebElementsDefinitions
    from xiq.defs.GuestPasswdSettingDefs import GuestPasswdSettingDefs
    from xiq.defs.IPFirewallPoliciesDefinitions import IPFirewallPoliciesDefinitions
    from xiq.defs.LoginWebElementsDefinitions import LoginWebElementsDefinitions
    from xiq.defs.MLInsightsClient360Definitions import MLInsightsClient360Definitions
    from xiq.defs.MLInsightscmpAnalyticsDefinitions import MLInsightscmpAnalyticsDefinitions
    from xiq.defs.MLInsightsDefinitions import MLInsightsDefinitions
    from xiq.defs.MLInsightsMonitorDefinitions import MLInsightsMonitorDefinitions
    from xiq.defs.MLInsightsPlanDefinitions import MLInsightsPlanDefinitions
    from xiq.defs.MLInsightsProxPresenceDefinitions import MLInsightsProxPresenceDefinitions
    from xiq.defs.MLInsightsScoreCardDefinitions import MLInsightsScoreCardDefinitions
    from xiq.defs.MLInsightsWebElementsDefinitions import MLInsightsWebElementsDefinitions
    from xiq.defs.MuCPWebElemenetsDefinitions import MuCPWebElementDefinitions
    from xiq.defs.NavigatorWebElementDefinitions import NavigatorWebElementDefinitions
    from xiq.defs.Network360MonitorDefinitions import Network360MonitorDefinitions
    from xiq.defs.Network360PlanDefinitions import Network360PlanDefinitions
    from xiq.defs.NetworkPolicyWebElementDefinition import NetworkPolicyWebElementDefinition
    from xiq.defs.NPExpressPolicySetupDefinitions import NPExpressPolicySetupDefinitions
    from xiq.defs.PasswdSettingsWebElementsDefinitions import PasswdSettingsWebElementsDefinitions
    from xiq.defs.PasswordResetWebElementsDefinition import PasswordResetWebElementsDefinition
    from xiq.defs.ReportsWebElementDefs import ReportsWebElementDefs
    from xiq.defs.RouterTemplateWebElementsDefinitions import RouterTemplateWebElementsDefinitions
    from xiq.defs.RSWebElementsDefinitions import RSWebElementsDefinitions
    from xiq.defs.SwitchTemplateWebElementsDefinitions import SwitchTemplateWebElementDefinitions
    from xiq.defs.SwitchWebElementsDefinitions import SwitchWebElementsDefinitions
    from xiq.defs.ToolsUtilitiesDefs import ToolsUtilitiesDefs
    from xiq.defs.UserGroupsWebElementsDefinitions import UserGroupsWebElementsDefinitions
    from xiq.defs.UserProfileWebElementsDef import UserProfileWebElementsDef
    from xiq.defs.WipsWebElementsDefinitions import WipsWebElementDefinitions
    from xiq.defs.WirelessCWPWebElementsDefinitions import WirelessCWPWebElementsDefinitions
    from xiq.defs.WirelessNetworksDefinitions import WirelessNetworksDefinitions
    from xiq.elements.A3InventoryWebElements import A3InventoryWebElements
    from xiq.elements.AccntMgmtWebElements import AccntMgmtWebElements
    from xiq.elements.AdspWebElements import AdspWebElements
    from xiq.elements.AdvanceOnboardingWebElements import AdvanceOnboardingWebElements
    from xiq.elements.AdvOnboardWebElements import AdvOnboardWebElements
    from xiq.elements.AlarmsWebElements import AlarmsWebElements
    from xiq.elements.ApplicationSpecificSearchWebElements import ApplicationSpecificSearchWebElements
    from xiq.elements.ApSpecificSearchWebElements import ApSpecificSearchWebElements
    from xiq.elements.AutoprovisionWebElements import AutoprovisionWebElements
    from xiq.elements.ClientMonitorWebElements import ClientMonitorWebElements
    from xiq.elements.ClientWebElements import ClientWebElements
    from xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
    from xiq.elements.CommunicationsWebElements import CommunicationsWebElements
    from xiq.elements.CloudConfigGroupWebElements import CloudConfigGroupWebElements
    from xiq.elements.CredDistrGrupWebElemnts import CredDistrGrupWebElemnts
    from xiq.elements.Device360WebElements import Device360WebElements
    from xiq.elements.DeviceActions import DeviceActions
    from xiq.elements.DeviceCliAccessElements import DeviceCliAccessElements
    from xiq.elements.DeviceCommonElements import DeviceCommonElements
    from xiq.elements.DeviceConfigElements import DeviceConfigElements
    from xiq.elements.DevicesWebElements import DevicesWebElements
    from xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
    from xiq.elements.DeviceUpdate import DeviceUpdate
    from xiq.elements.DialogWebElements import DialogWebElements
    from xiq.elements.EventsWebElements import EventsWebElements
    from xiq.elements.ExpSettingsWebElements import ExpSettingsWebElements
    from xiq.elements.ExtremeIOTWebElements import ExtremeIOTWebElements
    from xiq.elements.extreme_location.ExtremeLocationWebElements import ExtremeLocationWebElements
    from xiq.elements.FilterManageClientsWebElements import FilterManageClientWebElements
    from xiq.elements.FilterManageDeviceWebElements import FilterManageDeviceWebElements
    from xiq.elements.GlobalSearchWebElements import GlobalSearchWebElements
    from xiq.elements.GlobalSettingWebElements import GlobalSettingWebElements
    from xiq.elements.GuestAccessNetworkWebElements import GuestAccessNetworkWebElements
    from xiq.elements.GuestPasswdSettingElements import GuestPasswdSettingElements
    from xiq.elements.LoginWebElements import LoginWebElements
    from xiq.elements.MLInsightsClients360WebElements import MLInsightsClients360WebElements
    from xiq.elements.MLInsightscmpAnalyticsWebElements import MLInsightscmpAnalyticsWebElements
    from xiq.elements.MLInsightsMonitorWebElements import MLInsighstMonitorWebElements
    from xiq.elements.MLInsightsPlanWebElements import MLInsightsPlanWebElements
    from xiq.elements.MLInsightsProxPresenceWebElements import MLInsightsProxPresenceWebElements
    from xiq.elements.MLInsightsScoreCardWebElements import MLInsightsScoreCardWebElements
    ##  typo in lib --  from xiq.elements.MLInsightsWebElements import MLInsightsWebElements
    from xiq.elements.MuCPWebElements import MuCPWebElement
    from xiq.elements.NavigatorWebElements import NavigatorWebElements
    from xiq.elements.Network360MonitorElements import Network360MonitorElements
    from xiq.elements.Network360PlanElements import Network360PlanElements
    from xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
    from xiq.elements.NPExpressPolicyWebelEments import NPExpressPolicyWebElements
    from xiq.elements.PasswdSettingsWebElements import PasswdSettingsWebElements
    from xiq.elements.PasswordResetWebElements import PasswordResetWebElements
    from xiq.elements.ReportsWebElements import ReportsWebElements
    from xiq.elements.RouterTemplateWebElements import RouterTemplateWebElements
    from xiq.elements.RSWebElements import RSWebElements
    from xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
    from xiq.elements.SwitchWebElements import SwitchWebElements
    from xiq.elements.ToolsElements import ToolsElements
    from xiq.elements.UserGroupsWebElements import UserGroupsWebElements
    from xiq.elements.UserProfileWebElements import UserProfileWebElements
    from xiq.elements.WipsWebElements import WipsWebElements
    from xiq.elements.WirelessCWPWebElements import WirelessCWPWebElements
    from xiq.elements.WirelessWebElements import WirelessWebElements
    from xiq.elements.CopilotWebElements import CopilotWebElements
    from xiq.flows.AirDefence.AirDefenceAlarms import AirDefenceAlarms
    from xiq.flows.common.adsp import Adsp
    from xiq.flows.common.DeviceCommon import DeviceCommon
    from xiq.flows.common.GlobalSearch import GlobalSearch
    from xiq.flows.common.Login import Login
    from xiq.flows.common.MuCaptivePortal import MuCaptivePortal
    from xiq.flows.common.Navigator import Navigator
    from xiq.flows.common.SpecificSearch import SpecificSearch
    from xiq.flows.configure.AutoProvisioning import AutoProvisioning
    from xiq.flows.configure.CommonObjects import CommonObjects
    from xiq.flows.configure.DeviceTemplate import DeviceTemplate
    from xiq.flows.configure.ExpirationSettings import ExpirationSettings
    from xiq.flows.configure.ExpressNetworkPolicies import ExpressNetworkPolicies
    from xiq.flows.configure.GuestAccessNetwork import GuestAccessNetwork
    from xiq.flows.configure.NetworkPolicy import NetworkPolicy
    from xiq.flows.configure.PasswdSettings import PasswdSettings
    from xiq.flows.configure.RadiusServer import RadiusServer
    from xiq.flows.configure.RouterTemplate import RouterTemplate
    from xiq.flows.configure.SwitchTemplate import SwitchTemplate
    from xiq.flows.configure.UserGroups import UserGroups
    from xiq.flows.configure.UserProfile import UserProfile
    from xiq.flows.configure.Wips import Wips
    from xiq.flows.configure.WirelessCaptiveWebPortal import WirelessCaptiveWebPortal
    from xiq.flows.extreme_location.ExtremeLocation import ExtremeLocation
    from xiq.flows.globalsettings.AccountManagement import AccountManagement
    from xiq.flows.globalsettings.Communications import Communications
    from xiq.flows.globalsettings.CredDistrGrup import CredDistrGrup
    from xiq.flows.globalsettings.GlobalSetting import GlobalSetting
    from xiq.flows.globalsettings.PasswordReset import PasswordReset
    from xiq.flows.manage.AdvanceOnboarding import AdvanceOnboarding
    from xiq.flows.manage.AdvanceOnboarding import Location
    from xiq.flows.manage.AdvOnboard import AdvOnboard
    from xiq.flows.manage.Alarms import Alarms
    from xiq.flows.manage.Client import Client
    from xiq.flows.manage.ClientMonitor import ClientMonitor
    from xiq.flows.manage.Device360 import Device360
    from xiq.flows.manage.DeviceCliAccess import DeviceCliAccess
    from xiq.flows.manage.DeviceConfig import DeviceConfig
    from xiq.flows.manage.Devices import Devices
    from xiq.flows.manage.DevicesActions import DevicesActions
    from xiq.flows.manage.Events import Events
    from xiq.flows.manage.FilterManageDevices import FilterManageDevices
    from xiq.flows.manage.Reports import Reports
    from xiq.flows.manage.Switch import Switch
    from xiq.flows.mlinsights.MLInsightClient360 import MLInsightClient360
    ## -- typo in lib ---from xiq.flows.mlinsights.MLInsights import MLInsights
    from xiq.flows.mlinsights.Network360Monitor import Network360Monitor
    from xiq.flows.mlinsights.Network360Plan import Network360Plan
    from xiq.flows.mlinsights.Network360ScoreCard import Network360ScoreCard
except Exception as e:
    Logger().log_warn("Unable to load the XIQ libraries!")
    Logger().log_error(e)
    Logger().log_error(traceback.format_exc())

      


class XiqLibrary():
    
    def __init__(self):
        pass
        
    def init_xiq_libaries_and_login(self, username, password, capture_version=False, code="default", url="default", incognito_mode="False"):
        res = -1
        try:
            self.login = Login()
            res = self.login.login_user(username, password, capture_version=False, url=url, incognito_mode=incognito_mode)
                    
            self.Ap = Ap()
            self.Cli = Cli()
            self.Utils = Utils()
            self.AutoActions = AutoActions()
            self.WebElementHandler = WebElementHandler()
            self.Screen = Screen()
            self.GmailHandler = GmailHandler()
            # self.Iapi         = Iapi()
            self.IdentifiAP = IdentifiAP()
            self.ImageAnalysis = ImageAnalysis()
            self.ImageHandler = ImageHandler()
            self.LoadBrowser = LoadBrowser()
            self.Logging = Logging()
            self.Mu = Mu()
            self.Rest = Rest()
            self.ScreenDiff = ScreenDiff()
            self.SNMPTraps = SNMPTraps()
            self.Syslog = Syslog()
            self.TestFlow = TestFlow()
            self.Tshark = Tshark()
            self.WindowsMU = WindowsMU()
            self.WingAP = WingAP()
            self.Xapi = Xapi()
            self.toolsremoteLinMuConnect = LinMuConnect()
            self.toolsremoteMacMuConnect = MacMuConnect()
            self.toolsremoteRecording = Recording()
            #self.toolsremoteRFTestClient = RFTestClient()
            self.toolsremoteWinMuConnect = WinMuConnect()
            self.toolsremoteCPWebElements = CPWebElements()
            self.toolsremoteCPWebElementDefinitions = CPWebElementDefinitions()
    
    
            self.A3InventoryWebElementsDefs = A3InventoryWebElementsDefs()
            self.AccntMgmtWebElementsDefs = AccntMgmtWebElementsDefs()
            self.AdspWebElementsDefinitions = AdspWebElementsDefinitions()
            self.AdvanceOnboardingDefinitions = AdvanceOnboardingDefinitions()
            self.AdvOnboardDefs = AdvOnboardDefs()
            self.AlarmsWebElementsDefs = AlarmsWebElementsDefs()
            self.APPElementDefs = APPElementDefs()
            self.ApplicationSpecificSearchWebElementsDefinition = ApplicationSpecificSearchWebElementsDefinition()
            self.ApSpecificSearchWebElementsDefinition = ApSpecificSearchWebElementsDefinition()
            self.ClientMonitorWebElementsDefs = ClientMonitorWebElementsDefs()
            self.ClientWebElementsDefinitions = ClientWebElementsDefinitions()
            self.CommonObjectsWebElementsDefinitions = CommonObjectsWebElementsDefinitions()
            self.CommunicationsWebElementDefs = CommunicationsWebElementDefs()
            self.CredDistrGrupWebElemntsDefs = CredDistrGrupWebElemntsDefs()
            self.Device360WebElementDefs = Device360WebElementDefs()
            self.DeviceActionsDefs = DeviceActionsDefs()
            self.DeviceCliAccessDefs = DeviceCliAccessDefs()
            self.DeviceCommonDefs = DeviceCommonDefs()
            self.DeviceConfigDefs = DeviceConfigDefs()
            self.DevicesWebElementsDefinitions = DevicesWebElementsDefinitions()
            self.DeviceTemplateWebElementDefinitions = DeviceTemplateWebElementDefinitions()
            self.DeviceUpdateDefs = DeviceUpdateDefs()
            self.DialogWebElementsDefinitions = DialogWebElementsDefinitions()
            self.EventsWebElementsDefs = EventsWebElementsDefs()
            self.ExpSettingsWebElementsDefinitions = ExpSettingsWebElementsDefinitions()
            self.ExtremeGuestWebElementsDefs = ExtremeGuestWebElementsDefs()
            self.ExtremeIOTWebElementsDefs = ExtremeIOTWebElementsDefs()
            self.ExtremeLocationExtremeLocationWebElementsDefs = ExtremeLocationWebElementsDefs()
            self.FilterManageClientDefinitions = FilterManageClientDefinitions()
            self.FilterManageDeviceDefinitions = FilterManageDeviceDefinitions()
            self.GlobalSearchWebElementsDefinitions = GlobalSearchWebElementsDefinitions()
            self.GlobalSettingWebElementDefinitions = GlobalSettingWebElementDefinitions()
            self.GuestAccessNetworkWebElementsDefinitions = GuestAccessNetworkWebElementsDefinitions()
            self.GuestPasswdSettingDefs = GuestPasswdSettingDefs()
            self.IPFirewallPoliciesDefinitions = IPFirewallPoliciesDefinitions()
            self.LoginWebElementsDefinitions = LoginWebElementsDefinitions()
            self.MLInsightsClient360Definitions = MLInsightsClient360Definitions()
            self.MLInsightscmpAnalyticsDefinitions = MLInsightscmpAnalyticsDefinitions()
            self.MLInsightsDefinitions = MLInsightsDefinitions()
            self.MLInsightsMonitorDefinitions = MLInsightsMonitorDefinitions()
            self.MLInsightsPlanDefinitions = MLInsightsPlanDefinitions()
            self.MLInsightsProxPresenceDefinitions = MLInsightsProxPresenceDefinitions()
            self.MLInsightsScoreCardDefinitions = MLInsightsScoreCardDefinitions()
            self.MLInsightsWebElementsDefinitions = MLInsightsWebElementsDefinitions()
            self.MuCPWebElementDefinitions = MuCPWebElementDefinitions()
            self.NavigatorWebElementDefinitions = NavigatorWebElementDefinitions()
            self.Network360MonitorDefinitions = Network360MonitorDefinitions()
            self.Network360PlanDefinitions = Network360PlanDefinitions()
            self.NetworkPolicyWebElementDefinition = NetworkPolicyWebElementDefinition()
            self.NPExpressPolicySetupDefinitions = NPExpressPolicySetupDefinitions()
            self.PasswdSettingsWebElementsDefinitions = PasswdSettingsWebElementsDefinitions()
            self.PasswordResetWebElementsDefinition = PasswordResetWebElementsDefinition()
            self.ReportsWebElementDefs = ReportsWebElementDefs()
            self.RouterTemplateWebElementsDefinitions = RouterTemplateWebElementsDefinitions()
            self.RSWebElementsDefinitions = RSWebElementsDefinitions()
            self.SwitchTemplateWebElementDefinitions = SwitchTemplateWebElementDefinitions()
            self.SwitchWebElementsDefinitions = SwitchWebElementsDefinitions()
            self.ToolsUtilitiesDefs = ToolsUtilitiesDefs()
            self.UserGroupsWebElementsDefinitions = UserGroupsWebElementsDefinitions()
            self.UserProfileWebElementsDef = UserProfileWebElementsDef()
            self.WipsWebElementDefinitions = WipsWebElementDefinitions()
            self.WirelessCWPWebElementsDefinitions = WirelessCWPWebElementsDefinitions()
            self.WirelessNetworksDefinitions = WirelessNetworksDefinitions()

            self.xeleA3InventoryWebElements = A3InventoryWebElements()
            self.xeleAccntMgmtWebElements = AccntMgmtWebElements()
            self.xeleAdspWebElements = AdspWebElements()
            self.xeleAdvanceOnboardingWebElements = AdvanceOnboardingWebElements()
            self.xeleAdvOnboardWebElements = AdvOnboardWebElements()
            self.xeleAlarmsWebElements = AlarmsWebElements()
            self.xeleApplicationSpecificSearchWebElements = ApplicationSpecificSearchWebElements()
            self.xeleApSpecificSearchWebElements = ApSpecificSearchWebElements()
            self.xeleAutoprovisionWebElements = AutoprovisionWebElements()
            self.xeleClientMonitorWebElements = ClientMonitorWebElements()
            self.xeleClientWebElements = ClientWebElements()
            self.xeleCloudConfigGroupWebElements = CloudConfigGroupWebElements()
            self.xeleCommonObjectsWebElements = CommonObjectsWebElements()
            self.xeleCommunicationsWebElements = CommunicationsWebElements()
            self.xeleCredDistrGrupWebElemnts = CredDistrGrupWebElemnts()
            self.xeleDevice360WebElements = Device360WebElements()
            self.xeleDeviceActions = DeviceActions()
            self.xeleDeviceCliAccessElements = DeviceCliAccessElements()
            self.xeleDeviceCommonElements = DeviceCommonElements()
            self.xeleDeviceConfigElements = DeviceConfigElements()
            self.xeleDevicesWebElements = DevicesWebElements()
            self.xeleDeviceTemplateWebElements = DeviceTemplateWebElements()
            self.xeleDeviceUpdate = DeviceUpdate()
            self.xeleDialogWebElements = DialogWebElements()
            self.xeleEventsWebElements = EventsWebElements()
            self.xeleExpSettingsWebElements = ExpSettingsWebElements()
            self.xeleExtremeIOTWebElements = ExtremeIOTWebElements()
            self.xeleExtreme_locationExtremeLocationWebElements = ExtremeLocationWebElements()
            self.xeleFilterManageClientWebElements = FilterManageClientWebElements()
            self.xeleFilterManageDeviceWebElements = FilterManageDeviceWebElements()
            self.xeleGlobalSearchWebElements = GlobalSearchWebElements()
            self.xeleGlobalSettingWebElements = GlobalSettingWebElements()
            self.xeleGuestAccessNetworkWebElements = GuestAccessNetworkWebElements()
            self.xeleGuestPasswdSettingElements = GuestPasswdSettingElements()
            self.xeleLoginWebElements = LoginWebElements()
            self.xeleMLInsightsClients360WebElements = MLInsightsClients360WebElements()
            self.xeleMLInsightscmpAnalyticsWebElements = MLInsightscmpAnalyticsWebElements()
            self.xeleMLInsighstMonitorWebElements = MLInsighstMonitorWebElements()
            self.xeleMLInsightsPlanWebElements = MLInsightsPlanWebElements()
            self.xeleMLInsightsProxPresenceWebElements = MLInsightsProxPresenceWebElements()
            self.xeleMLInsightsScoreCardWebElements = MLInsightsScoreCardWebElements()
            ## --- typo in lib  ---  self.xeleMLInsightsWebElements = MLInsightsWebElements()
            self.xeleMuCPWebElement = MuCPWebElement()
            self.xeleNavigatorWebElements = NavigatorWebElements()
            self.xeleNetwork360MonitorElements = Network360MonitorElements()
            self.xeleNetwork360PlanElements = Network360PlanElements()
            self.xeleNetworkPolicyWebElements = NetworkPolicyWebElements()
            self.xeleNPExpressPolicyWebElements = NPExpressPolicyWebElements()
            self.xelePasswdSettingsWebElements = PasswdSettingsWebElements()
            self.xelePasswordResetWebElements = PasswordResetWebElements()
            self.xeleReportsWebElements = ReportsWebElements()
            self.xeleRouterTemplateWebElements = RouterTemplateWebElements()
            self.xeleRSWebElements = RSWebElements()
            self.xeleSwitchTemplateWebElements = SwitchTemplateWebElements()
            self.xeleSwitchWebElements = SwitchWebElements()
            self.xeleToolsElements = ToolsElements()
            self.xeleUserGroupsWebElements = UserGroupsWebElements()
            self.xeleUserProfileWebElements = UserProfileWebElements()
            self.xeleWipsWebElements = WipsWebElements()
            self.xeleWirelessCWPWebElements = WirelessCWPWebElements()
            self.xeleWirelessWebElements = WirelessWebElements()
    
            self.xflowsmanageFilterManageDevices = FilterManageDevices()
            self.xflowsAirDefenceAirDefenceAlarms = AirDefenceAlarms()
            self.xflowscommonAdsp = Adsp()
            self.xflowscommonDeviceCommon = DeviceCommon()
            self.xflowscommonDevices = Devices()
            self.xflowscommonGlobalSearch = GlobalSearch()
            self.xflowscommonMuCaptivePortal = MuCaptivePortal()
            self.xflowscommonNavigator = Navigator()
            self.xflowscommonSpecificSearch = SpecificSearch()
            self.xflowsconfigureAutoProvisioning = AutoProvisioning()
            self.xflowsconfigureCommonObjects = CommonObjects()
            self.xflowsconfigureDeviceTemplate = DeviceTemplate()
            self.xflowsconfigureExpirationSettings = ExpirationSettings()
            self.xflowsconfigureExpressNetworkPolicies = ExpressNetworkPolicies()
            self.xflowsconfigureGuestAccessNetwork = GuestAccessNetwork()
            self.xflowsconfigureNetworkPolicy = NetworkPolicy()
            self.xflowsconfigurePasswdSettings = PasswdSettings()
            self.xflowsconfigureRadiusServer = RadiusServer()
            self.xflowsconfigureRouterTemplate = RouterTemplate()
            self.xflowsconfigureSwitchTemplate = SwitchTemplate()
            self.xflowsconfigureUserGroups = UserGroups()
            self.xflowsconfigureUserProfile = UserProfile()
            self.xflowsconfigureWips = Wips()
            self.xflowsconfigureWirelessCaptiveWebPortal = WirelessCaptiveWebPortal()
            self.xflowsExtreme_LocationExtremeLocation = ExtremeLocation()
            self.xflowsglobalsettingsAccountManagement = AccountManagement()
            self.xflowsglobalsettingsCommunications = Communications()
            self.xflowsglobalsettingsCredDistrGrup = CredDistrGrup()
            self.xflowsglobalsettingsGlobalSetting = GlobalSetting()
            self.xflowsglobalsettingsPasswordReset = PasswordReset()
            self.xflowsmanageAdvanceOnboarding = AdvanceOnboarding()
            self.xflowsmanageLocation = Location()
            self.xflowsmanageAdvOnboard = AdvOnboard()
            self.xflowsmanageAlarms = Alarms()
            self.xflowsmanageClient = Client()
            self.xflowsmanageClientMonitor = ClientMonitor()
            self.xflowsmanageDevice360 = Device360()
            self.xflowsmanageDeviceCliAccess = DeviceCliAccess()
            self.xflowsmanageDeviceConfig = DeviceConfig()
            self.xflowsmanageDevices = Devices()
            self.xflowsmanageDevicesActions = DevicesActions()
            self.xflowsmanageEvents = Events()
            self.xflowsmanageReports = Reports()
            self.xflowsmanageSwitch = Switch()
            self.xflowsmlinsightsMLInsightClient360 = MLInsightClient360()
            ##  remark until typo fixed ---   self.xflowsmlinsightsMLInsights = MLInsights()
            self.xflowsmlinsightsNetwork360Monitor = Network360Monitor()
            ## util is not imported in lib --- self.xflowsmlinsightsNetwork360Plan = Network360Plan()
            ## util is not imported in lib --- self.xflowsmlinsightsNetwork360ScoreCard = Network360ScoreCard()
        except Exception as e:
            Logger().log_error("Unable to load the XIQ libraries and login!")
            Logger().log_error(e)
            Logger().log_error(traceback.format_exc())

        
        return res