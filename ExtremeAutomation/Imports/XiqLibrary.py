from ExtremeAutomation.Library.Logger.Logger import Logger
import traceback

try:
    from extauto.common.Ap import Ap
    from extauto.common.Cli import Cli
    from extauto.common.Utils import Utils
    from extauto.common.CloudDriver import CloudDriver
    from extauto.common.AutoActions import AutoActions
    from extauto.common.Debugging import Debugging
    from extauto.common.GmailHandler import GmailHandler
    # from extauto.common.Iapi import Iapi
    from extauto.common.ImageAnalysis import ImageAnalysis
    from extauto.common.ImageHandler import ImageHandler
    from extauto.common.Mu import Mu
    from extauto.common.Rest import Rest
    from extauto.common.Screen import Screen
    from extauto.common.ScreenDiff import ScreenDiff
    from extauto.common.SNMPTraps import SNMPTraps
    from extauto.common.TestFlow import TestFlow
    from extauto.common.Tshark import Tshark
    from extauto.common.WindowsMU import WindowsMU
    from extauto.common.WingAP import WingAP
    from extauto.common.Xapi import Xapi
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
    from extauto.xiq.flows.manage.Location import Location
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
    from extauto.xiq.flows.manage.XiqVerifications import XiqVerifications
    from extauto.xiq.flows.mlinsights.MLInsightClient360 import MLInsightClient360
    ## -- typo in lib ---from extauto.xiq.flows.mlinsights.MLInsights import MLInsights
    from extauto.xiq.flows.mlinsights.Network360Monitor import Network360Monitor
    from extauto.xiq.flows.mlinsights.Network360Plan import Network360Plan


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
        self.CloudDriver = CloudDriver()
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
        self.Utils = Utils()

        self.xflowscommonAutoActions = AutoActions()
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
        self.xflowsmlinsightsNetwork360Plan = Network360Plan()
        self.xflowsmlinsightsNetwork360Monitor = Network360Monitor()
        self.xflowsmanageXiqVerifications = XiqVerifications()
        self.xflowsDebuggging = Debugging()


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
