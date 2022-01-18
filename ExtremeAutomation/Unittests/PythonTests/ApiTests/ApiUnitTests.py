from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.Common.Agents.AgentConstants import AgentConstants
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
# Test APIs
from ExtremeAutomation.Library.Device.Common.Apis.BaseApi import BaseApi
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.base.unittestbase \
    import UnittestBase as FeatureBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EOS.base.baseversion.\
    baseunit.unittest import Unittest as EosFeatureBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EXOS.base.baseversion.\
    baseunit.unittest import Unittest as ExosFeatureBase
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EOS.platform1.\
    baseversion.baseunit.unittest import Unittest as EosFeatureSpecificPlatform
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EXOS.platform1.\
    baseversion.baseunit.unittest import Unittest as ExosFeatureSpecificPlatform
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EOS.base.v1dot1.\
    baseunit.unittest import Unittest as EosFeatureSpecificVersion
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EXOS.base.v1dot1.\
    baseunit.unittest import Unittest as ExosFeatureSpecificVersion
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EOS.base.baseversion.\
    unit1.unittest import Unittest as EosFeatureSpecificUnit
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.CLI.unittest.EXOS.base.baseversion.\
    unit1.unittest import Unittest as ExosFeatureSpecificUnit


class ApiUnitTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.constants = NetworkElementConstants()
        cls.dev_bad_os = NetworkElement("not_a_real_os", cls.constants.PLATFORM_BASE, cls.constants.UNIT_BASE,
                                        cls.constants.VERSION_BASE)
        cls.dev_unsupported_agent = NetworkElement(cls.constants.OS_EXOS, cls.constants.PLATFORM_BASE,
                                                   cls.constants.UNIT_BASE, cls.constants.VERSION_BASE)
        cls.dev_eos_base = NetworkElement(cls.constants.OS_EOS, cls.constants.PLATFORM_BASE, cls.constants.UNIT_BASE,
                                          cls.constants.VERSION_BASE)
        cls.dev_eos_platform = NetworkElement(cls.constants.OS_EOS, "platform1",
                                              cls.constants.UNIT_BASE, cls.constants.VERSION_BASE)
        cls.dev_eos_version = NetworkElement(cls.constants.OS_EOS, cls.constants.PLATFORM_BASE, cls.constants.UNIT_BASE,
                                             "1.1")
        cls.dev_eos_unit = NetworkElement(cls.constants.OS_EOS, cls.constants.PLATFORM_BASE, "unit1",
                                          cls.constants.VERSION_BASE)
        cls.dev_exos_base = NetworkElement(cls.constants.OS_EXOS, cls.constants.PLATFORM_BASE, cls.constants.UNIT_BASE,
                                           cls.constants.VERSION_BASE)
        cls.dev_exos_platform = NetworkElement(cls.constants.OS_EXOS, "platform1", cls.constants.UNIT_BASE,
                                               cls.constants.VERSION_BASE)
        cls.dev_exos_version = NetworkElement(cls.constants.OS_EXOS, cls.constants.PLATFORM_BASE,
                                              cls.constants.UNIT_BASE, "1.1")
        cls.dev_exos_unit = NetworkElement(cls.constants.OS_EXOS, cls.constants.PLATFORM_BASE, "unit1",
                                           cls.constants.VERSION_BASE)

        cls.dev_bad_os.connection_method = AgentConstants.TYPE_SSH
        cls.dev_unsupported_agent.connection_method = AgentConstants.TYPE_REST
        cls.dev_eos_base.connection_method = AgentConstants.TYPE_SSH
        cls.dev_eos_platform.connection_method = AgentConstants.TYPE_SSH
        cls.dev_eos_version.connection_method = AgentConstants.TYPE_SSH
        cls.dev_eos_unit.connection_method = AgentConstants.TYPE_SSH
        cls.dev_exos_base.connection_method = AgentConstants.TYPE_TELNET
        cls.dev_exos_platform.connection_method = AgentConstants.TYPE_TELNET
        cls.dev_exos_version.connection_method = AgentConstants.TYPE_TELNET
        cls.dev_exos_unit.connection_method = AgentConstants.TYPE_TELNET

    def test_api_base(self):
        api = self.dev_unsupported_agent.api_factory.get_api(self.dev_unsupported_agent, "unittest")
        self.assertIsInstance(api, BaseApi)

    def test_feature_base(self):
        api = self.dev_bad_os.api_factory.get_api(self.dev_bad_os, "unittest")
        self.assertIsInstance(api, FeatureBase)

    def test_eos_feature_base(self):
        api = self.dev_eos_base.api_factory.get_api(self.dev_eos_base, "unittest")
        self.assertIsInstance(api, EosFeatureBase)

    def test_exos_feature_base(self):
        api = self.dev_exos_base.api_factory.get_api(self.dev_exos_base, "unittest")
        self.assertIsInstance(api, ExosFeatureBase)

    def test_eos_feature_specific_platform(self):
        api = self.dev_eos_platform.api_factory.get_api(self.dev_eos_platform, "unittest")
        self.assertIsInstance(api, EosFeatureSpecificPlatform)

    def test_exos_feature_specific_platform(self):
        api = self.dev_exos_platform.api_factory.get_api(self.dev_exos_platform, "unittest")
        self.assertIsInstance(api, ExosFeatureSpecificPlatform)

    def test_eos_feature_specific_version(self):
        api = self.dev_eos_version.api_factory.get_api(self.dev_eos_version, "unittest")
        self.assertIsInstance(api, EosFeatureSpecificVersion)

    def test_exos_feature_specific_version(self):
        api = self.dev_exos_version.api_factory.get_api(self.dev_exos_version, "unittest")
        self.assertIsInstance(api, ExosFeatureSpecificVersion)

    def test_eos_feature_specific_unit(self):
        api = self.dev_eos_unit.api_factory.get_api(self.dev_eos_unit, "unittest")
        self.assertIsInstance(api, EosFeatureSpecificUnit)

    def test_exos_feature_specific_unit(self):
        api = self.dev_exos_unit.api_factory.get_api(self.dev_exos_unit, "unittest")
        self.assertIsInstance(api, ExosFeatureSpecificUnit)


if __name__ == '__main__':
    RobotUnitTest.main()
