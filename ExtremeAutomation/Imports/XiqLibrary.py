from ExtremeAutomation.Library.Logger.Logger import Logger
import traceback

try:
    from extauto.common.Ap import Ap
    from extauto.common.Cli import Cli
    from extauto.common.Utils import Utils
    from extauto.common.AutoActions import AutoActions
    from extauto.common.GmailHandler import GmailHandler
    # from extauto.common.Iapi import Iapi
    from extauto.common.IdentifiAP import IdentifiAP
    from extauto.common.ImageAnalysis import ImageAnalysis
    from extauto.common.ImageHandler import ImageHandler
    from extauto.common.LoadBrowser import LoadBrowser
    from extauto.common.Logging import Logging
    from extauto.common.Mu import Mu
    from extauto.common.Rest import Rest
    from extauto.common.Screen import Screen
    from extauto.common.ScreenDiff import ScreenDiff
    from extauto.common.SNMPTraps import SNMPTraps
    from extauto.common.Syslog import Syslog
    from extauto.common.TestFlow import TestFlow
    from extauto.common.Tshark import Tshark
    from extauto.common.WebElementHandler import WebElementHandler
    from extauto.common.WindowsMU import WindowsMU
    from extauto.common.WingAP import WingAP
    from extauto.common.Xapi import Xapi
    from extauto.common.tools.remote.LinMuConnect import LinMuConnect
    from extauto.common.tools.remote.MacMuConnect import MacMuConnect
    from extauto.common.tools.remote.Recording import Recording
    # from extauto.common.tools.remote.RFTestClient import RFTestClient
    from extauto.common.tools.remote.WinMuConnect import WinMuConnect
    from extauto.common.tools.remote.captiveportal.CaptivePortal import CPWebElements
    from extauto.common.tools.remote.captiveportal.CPWebElementDefinitions import CPWebElementDefinitions
    from extauto.xiq.defs.A3InventoryWebElementsDefs import A3InventoryWebElementsDefs
    from extauto.xiq.defs.AccntMgmtWebElementsDefs import AccntMgmtWebElementsDefs
    from extauto.xiq.defs.AdspWebElementsDefinitions import AdspWebElementsDefinitions
    from extauto.xiq.defs.AdvanceOnboardingDefinitions import AdvanceOnboardingDefinitions
    from extauto.xiq.defs.AdvOnboardDefs import AdvOnboardDefs
    from extauto.xiq.defs.AlarmsWebElementsDefs import AlarmsWebElementsDefs
    from extauto.xiq.defs.APPElementDefs import APPElementDefs
    from extauto.xiq.defs.ApplicationSpecificSearchWebElementsDefinition import \
        ApplicationSpecificSearchWebElementsDefinition
    from extauto.xiq.defs.ApSpecificSearchWebElementsDefinition import ApSpecificSearchWebElementsDefinition
    from extauto.xiq.defs.ClientMonitorWebElementsDefs import ClientMonitorWebElementsDefs
    from extauto.xiq.defs.ClientWebElementsDefinitions import ClientWebElementsDefinitions
    from extauto.xiq.defs.CommonObjectsWebElementsDefinitions import CommonObjectsWebElementsDefinitions
    from extauto.xiq.defs.CommunicationsWebElementDefs import CommunicationsWebElementDefs
    from extauto.xiq.defs.CredDistrGrupWebElemntsDefs import CredDistrGrupWebElemntsDefs
    from extauto.xiq.defs.Device360WebElementDefs import Device360WebElementDefs
    from extauto.xiq.defs.DeviceActionsDefs import DeviceActionsDefs
    from extauto.xiq.defs.DeviceCliAccessDefs import DeviceCliAccessDefs
    from extauto.xiq.defs.DeviceCommonDefs import DeviceCommonDefs
    from extauto.xiq.defs.DeviceConfigDefs import DeviceConfigDefs
    from extauto.xiq.defs.DevicesWebElementsDefinitions import DevicesWebElementsDefinitions
    from extauto.xiq.defs.DeviceTemplateWebElementsDefinitions import DeviceTemplateWebElementDefinitions
    from extauto.xiq.defs.DeviceUpdateDefs import DeviceUpdateDefs
    from extauto.xiq.defs.DialogWebElementsDefinitions import DialogWebElementsDefinitions
    from extauto.xiq.defs.EventsWebElementsDefs import EventsWebElementsDefs
    from extauto.xiq.defs.ExpSettingsWebElementsDefinitions import ExpSettingsWebElementsDefinitions
    from extauto.xiq.defs.ExtremeGuestWebElementsDefs import ExtremeGuestWebElementsDefs
    from extauto.xiq.defs.ExtremeIOTWebElementsDefs import ExtremeIOTWebElementsDefs
    from extauto.xiq.defs.extreme_location.ExtremeLocationWebElementsDefs import ExtremeLocationWebElementsDefs
    from extauto.xiq.defs.FilterManageClientDefinitions import FilterManageClientDefinitions
    from extauto.xiq.defs.FilterManageDeviceDefinitions import FilterManageDeviceDefinitions
    from extauto.xiq.defs.GlobalSearchWebElementsDefinitions import GlobalSearchWebElementsDefinitions
    from extauto.xiq.defs.GlobalSettingWebElementDefinitions import GlobalSettingWebElementDefinitions
    from extauto.xiq.defs.GuestAccessNetworkWebElementsDefinitions import GuestAccessNetworkWebElementsDefinitions
    from extauto.xiq.defs.GuestPasswdSettingDefs import GuestPasswdSettingDefs
    from extauto.xiq.defs.IPFirewallPoliciesDefinitions import IPFirewallPoliciesDefinitions
    from extauto.xiq.defs.LoginWebElementsDefinitions import LoginWebElementsDefinitions
    from extauto.xiq.defs.MLInsightsClient360Definitions import MLInsightsClient360Definitions
    from extauto.xiq.defs.MLInsightscmpAnalyticsDefinitions import MLInsightscmpAnalyticsDefinitions
    from extauto.xiq.defs.MLInsightsDefinitions import MLInsightsDefinitions
    from extauto.xiq.defs.MLInsightsMonitorDefinitions import MLInsightsMonitorDefinitions
    from extauto.xiq.defs.MLInsightsPlanDefinitions import MLInsightsPlanDefinitions
    from extauto.xiq.defs.MLInsightsProxPresenceDefinitions import MLInsightsProxPresenceDefinitions
    from extauto.xiq.defs.MLInsightsScoreCardDefinitions import MLInsightsScoreCardDefinitions
    from extauto.xiq.defs.MLInsightsWebElementsDefinitions import MLInsightsWebElementsDefinitions
    from extauto.xiq.defs.MuCPWebElemenetsDefinitions import MuCPWebElementDefinitions
    from extauto.xiq.defs.NavigatorWebElementDefinitions import NavigatorWebElementDefinitions
    from extauto.xiq.defs.Network360MonitorDefinitions import Network360MonitorDefinitions
    from extauto.xiq.defs.Network360PlanDefinitions import Network360PlanDefinitions
    from extauto.xiq.defs.NetworkPolicyWebElementDefinition import NetworkPolicyWebElementDefinition
    from extauto.xiq.defs.NPExpressPolicySetupDefinitions import NPExpressPolicySetupDefinitions
    from extauto.xiq.defs.PasswdSettingsWebElementsDefinitions import PasswdSettingsWebElementsDefinitions
    from extauto.xiq.defs.PasswordResetWebElementsDefinition import PasswordResetWebElementsDefinition
    from extauto.xiq.defs.ReportsWebElementDefs import ReportsWebElementDefs
    from extauto.xiq.defs.RouterTemplateWebElementsDefinitions import RouterTemplateWebElementsDefinitions
    from extauto.xiq.defs.RSWebElementsDefinitions import RSWebElementsDefinitions
    from extauto.xiq.defs.SwitchTemplateWebElementsDefinitions import SwitchTemplateWebElementDefinitions
    from extauto.xiq.defs.SwitchWebElementsDefinitions import SwitchWebElementsDefinitions
    from extauto.xiq.defs.ToolsUtilitiesDefs import ToolsUtilitiesDefs
    from extauto.xiq.defs.UserGroupsWebElementsDefinitions import UserGroupsWebElementsDefinitions
    from extauto.xiq.defs.UserProfileWebElementsDef import UserProfileWebElementsDef
    from extauto.xiq.defs.WipsWebElementsDefinitions import WipsWebElementDefinitions
    from extauto.xiq.defs.WirelessCWPWebElementsDefinitions import WirelessCWPWebElementsDefinitions
    from extauto.xiq.defs.WirelessNetworksDefinitions import WirelessNetworksDefinitions
    from extauto.xiq.elements.A3InventoryWebElements import A3InventoryWebElements
    from extauto.xiq.elements.AccntMgmtWebElements import AccntMgmtWebElements
    from extauto.xiq.elements.AdspWebElements import AdspWebElements
    from extauto.xiq.elements.AdvanceOnboardingWebElements import AdvanceOnboardingWebElements
    from extauto.xiq.elements.AdvOnboardWebElements import AdvOnboardWebElements
    from extauto.xiq.elements.AlarmsWebElements import AlarmsWebElements
    from extauto.xiq.elements.ApplicationSpecificSearchWebElements import ApplicationSpecificSearchWebElements
    from extauto.xiq.elements.ApSpecificSearchWebElements import ApSpecificSearchWebElements
    from extauto.xiq.elements.AutoprovisionWebElements import AutoprovisionWebElements
    from extauto.xiq.elements.ClientMonitorWebElements import ClientMonitorWebElements
    from extauto.xiq.elements.ClientWebElements import ClientWebElements
    from extauto.xiq.elements.CommonObjectsWebElements import CommonObjectsWebElements
    from extauto.xiq.elements.CommunicationsWebElements import CommunicationsWebElements
    from extauto.xiq.elements.CloudConfigGroupWebElements import CloudConfigGroupWebElements
    from extauto.xiq.elements.CredDistrGrupWebElemnts import CredDistrGrupWebElemnts
    from extauto.xiq.elements.Device360WebElements import Device360WebElements
    from extauto.xiq.elements.DeviceActions import DeviceActions
    from extauto.xiq.elements.DeviceCliAccessElements import DeviceCliAccessElements
    from extauto.xiq.elements.DeviceCommonElements import DeviceCommonElements
    from extauto.xiq.elements.DeviceConfigElements import DeviceConfigElements
    from extauto.xiq.elements.DevicesWebElements import DevicesWebElements
    from extauto.xiq.elements.DeviceTemplateWebElements import DeviceTemplateWebElements
    from extauto.xiq.elements.DeviceUpdate import DeviceUpdate
    from extauto.xiq.elements.DialogWebElements import DialogWebElements
    from extauto.xiq.elements.EventsWebElements import EventsWebElements
    from extauto.xiq.elements.ExpSettingsWebElements import ExpSettingsWebElements
    from extauto.xiq.elements.ExtremeIOTWebElements import ExtremeIOTWebElements
    from extauto.xiq.elements.extreme_location.ExtremeLocationWebElements import ExtremeLocationWebElements
    from extauto.xiq.elements.FilterManageClientsWebElements import FilterManageClientWebElements
    from extauto.xiq.elements.FilterManageDeviceWebElements import FilterManageDeviceWebElements
    from extauto.xiq.elements.GlobalSearchWebElements import GlobalSearchWebElements
    from extauto.xiq.elements.GlobalSettingWebElements import GlobalSettingWebElements
    from extauto.xiq.elements.GuestAccessNetworkWebElements import GuestAccessNetworkWebElements
    from extauto.xiq.elements.GuestPasswdSettingElements import GuestPasswdSettingElements
    from extauto.xiq.elements.LoginWebElements import LoginWebElements
    from extauto.xiq.elements.MLInsightsClients360WebElements import MLInsightsClients360WebElements
    from extauto.xiq.elements.MLInsightscmpAnalyticsWebElements import MLInsightscmpAnalyticsWebElements
    from extauto.xiq.elements.MLInsightsMonitorWebElements import MLInsighstMonitorWebElements
    from extauto.xiq.elements.MLInsightsPlanWebElements import MLInsightsPlanWebElements
    from extauto.xiq.elements.MLInsightsProxPresenceWebElements import MLInsightsProxPresenceWebElements
    from extauto.xiq.elements.MLInsightsScoreCardWebElements import MLInsightsScoreCardWebElements
    ##  typo in lib --  from extauto.xiq.elements.MLInsightsWebElements import MLInsightsWebElements
    from extauto.xiq.elements.MuCPWebElements import MuCPWebElement
    from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
    from extauto.xiq.elements.Network360MonitorElements import Network360MonitorElements
    from extauto.xiq.elements.Network360PlanElements import Network360PlanElements
    from extauto.xiq.elements.NetworkPolicyWebElements import NetworkPolicyWebElements
    from extauto.xiq.elements.NPExpressPolicyWebelEments import NPExpressPolicyWebElements
    from extauto.xiq.elements.PasswdSettingsWebElements import PasswdSettingsWebElements
    from extauto.xiq.elements.PasswordResetWebElements import PasswordResetWebElements
    from extauto.xiq.elements.ReportsWebElements import ReportsWebElements
    from extauto.xiq.elements.RouterTemplateWebElements import RouterTemplateWebElements
    from extauto.xiq.elements.RSWebElements import RSWebElements
    from extauto.xiq.elements.SwitchTemplateWebElements import SwitchTemplateWebElements
    from extauto.xiq.elements.SwitchWebElements import SwitchWebElements
    from extauto.xiq.elements.ToolsElements import ToolsElements
    from extauto.xiq.elements.UserGroupsWebElements import UserGroupsWebElements
    from extauto.xiq.elements.UserProfileWebElements import UserProfileWebElements
    from extauto.xiq.elements.WipsWebElements import WipsWebElements
    from extauto.xiq.elements.WirelessCWPWebElements import WirelessCWPWebElements
    from extauto.xiq.elements.WirelessWebElements import WirelessWebElements
    from extauto.xiq.elements.CopilotWebElements import CopilotWebElements
    from extauto.xiq.flows.AirDefence.AirDefenceAlarms import AirDefenceAlarms
    from extauto.xiq.flows.common.adsp import Adsp
    from extauto.xiq.flows.common.DeviceCommon import DeviceCommon
    from extauto.xiq.flows.common.GlobalSearch import GlobalSearch
    from extauto.xiq.flows.common.Login import Login
    from extauto.xiq.flows.common.MuCaptivePortal import MuCaptivePortal
    from extauto.xiq.flows.common.Navigator import Navigator
    from extauto.xiq.flows.common.SpecificSearch import SpecificSearch
    from extauto.xiq.flows.configure.AutoProvisioning import AutoProvisioning
    from extauto.xiq.flows.configure.CommonObjects import CommonObjects
    from extauto.xiq.flows.configure.DeviceTemplate import DeviceTemplate
    from extauto.xiq.flows.configure.ExpirationSettings import ExpirationSettings
    from extauto.xiq.flows.configure.ExpressNetworkPolicies import ExpressNetworkPolicies
    from extauto.xiq.flows.configure.GuestAccessNetwork import GuestAccessNetwork
    from extauto.xiq.flows.configure.NetworkPolicy import NetworkPolicy
    from extauto.xiq.flows.configure.PasswdSettings import PasswdSettings
    from extauto.xiq.flows.configure.RadiusServer import RadiusServer
    from extauto.xiq.flows.configure.RouterTemplate import RouterTemplate
    from extauto.xiq.flows.configure.SwitchTemplate import SwitchTemplate
    from extauto.xiq.flows.configure.UserGroups import UserGroups
    from extauto.xiq.flows.configure.UserProfile import UserProfile
    from extauto.xiq.flows.configure.Wips import Wips
    from extauto.xiq.flows.configure.WirelessCaptiveWebPortal import WirelessCaptiveWebPortal
    from extauto.xiq.flows.extreme_location.ExtremeLocation import ExtremeLocation
    from extauto.xiq.flows.globalsettings.AccountManagement import AccountManagement
    from extauto.xiq.flows.globalsettings.Communications import Communications
    from extauto.xiq.flows.globalsettings.CredDistrGrup import CredDistrGrup
    from extauto.xiq.flows.globalsettings.GlobalSetting import GlobalSetting
    from extauto.xiq.flows.globalsettings.PasswordReset import PasswordReset
    from extauto.xiq.flows.manage.AdvanceOnboarding import AdvanceOnboarding
    from extauto.xiq.flows.manage.AdvanceOnboarding import Location
    from extauto.xiq.flows.manage.AdvOnboard import AdvOnboard
    from extauto.xiq.flows.manage.Alarms import Alarms
    from extauto.xiq.flows.manage.Client import Client
    from extauto.xiq.flows.manage.ClientMonitor import ClientMonitor
    from extauto.xiq.flows.manage.Device360 import Device360
    from extauto.xiq.flows.manage.DeviceCliAccess import DeviceCliAccess
    from extauto.xiq.flows.manage.DeviceConfig import DeviceConfig
    from extauto.xiq.flows.manage.Devices import Devices
    from extauto.xiq.flows.manage.DevicesActions import DevicesActions
    from extauto.xiq.flows.manage.Events import Events
    from extauto.xiq.flows.manage.FilterManageDevices import FilterManageDevices
    from extauto.xiq.flows.manage.Reports import Reports
    from extauto.xiq.flows.manage.Switch import Switch
    from extauto.xiq.flows.manage.Tools import Tools
    from extauto.xiq.flows.mlinsights.MLInsightClient360 import MLInsightClient360
    ## -- typo in lib ---from extauto.xiq.flows.mlinsights.MLInsights import MLInsights
    from extauto.xiq.flows.mlinsights.Network360Monitor import Network360Monitor
    from extauto.xiq.flows.mlinsights.Network360Plan import Network360Plan
    from extauto.xiq.flows.mlinsights.Network360ScoreCard import Network360ScoreCard
except Exception as e:
    Logger().log_warn("Unable to load the XIQ libraries!")
    Logger().log_error(e)
    Logger().log_error(traceback.format_exc())

from ExtremeAutomation.Utilities.deprecated import deprecated

      


class XiqLibrary():
    
    def __init__(self):
        self.login = Login()
        self.Ap = Ap()
        self.Cli = Cli()
        self.Utils = Utils()
        self.Screen = Screen()
        self.GmailHandler = GmailHandler()
        self.ImageAnalysis = ImageAnalysis()
        self.ImageHandler = ImageHandler()
        self.Mu = Mu()
        self.Rest = Rest()
        self.ScreenDiff = ScreenDiff()
        self.SNMPTraps = SNMPTraps()
        self.TestFlow = TestFlow()
        self.Tshark = Tshark()
        self.WindowsMU = WindowsMU()
        self.WingAP = WingAP()
        self.Xapi = Xapi()

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
        self.xflowsmanageTools = Tools()
        self.xflowsmlinsightsMLInsightClient360 = MLInsightClient360()
        self.xflowsmlinsightsNetwork360Plan = Network360Plan()
        self.xflowsmlinsightsNetwork360Monitor = Network360Monitor()


    @deprecated("Please use self.xiq.login.login_user(...)")
    def init_xiq_libaries_and_login(self, username, password, capture_version=False, code="default", url="default", incognito_mode="False", **kwargs):
        res = -1
        try:
            res = self.login.login_user(username, password, capture_version=False, url=url, incognito_mode=incognito_mode, **kwargs)
        except Exception as e:
            Logger().log_error("Unable to load the XIQ libraries and login!")
            Logger().log_error(e)
            Logger().log_error(traceback.format_exc())


        return res
