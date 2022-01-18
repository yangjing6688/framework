from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.NetworkElement.NetworkElement import NetworkElement
from ExtremeAutomation.Keywords.Utils.DeviceCollectionManager import DeviceCollectionManager
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.PlatformVariables import PlatformVariables
from ExtremeAutomation.Library.Device.NetworkElement.Constants.NetworkElementConstants import NetworkElementConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.PlatformVariables.EOS.baseplatvars.EosPlatformVariables \
    import EosPlatformVariables
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.PlatformVariables.EXOS.baseplatvars.ExosPlatformVariables \
    import ExosPlatformVariables


class PlatformVariablesUnitTests(RobotUnitTest):
    @classmethod
    def setUpClass(cls):
        cls.eos_dev = NetworkElement(NetworkElementConstants.OS_EOS, NetworkElementConstants.PLATFORM_BASE,
                                     NetworkElementConstants.UNIT_BASE, NetworkElementConstants.VERSION_BASE)
        cls.exos_dev = NetworkElement(NetworkElementConstants.OS_EXOS, NetworkElementConstants.PLATFORM_BASE,
                                      NetworkElementConstants.UNIT_BASE, NetworkElementConstants.VERSION_BASE)

        cls.eos_dev.name = "eos_dev"
        cls.exos_dev_name = "exos_dev"

        cls.device_col = DeviceCollectionManager()

        cls.device_col.add_device(cls.eos_dev.name, cls.eos_dev)
        cls.device_col.add_device(cls.exos_dev.name, cls.exos_dev)

    def test_eos_plat_vars(self):
        plat_var_gen = PlatformVariables()
        eos_plat_vars = EosPlatformVariables().vars

        eos_generated_plat_vars = plat_var_gen.get_variables(self.eos_dev.name)

        self.assertEqual(eos_generated_plat_vars, eos_plat_vars)

    def test_exos_plat_vars(self):
        plat_var_gen = PlatformVariables()
        exos_plat_vars = ExosPlatformVariables().vars

        exos_generated_plat_vars = plat_var_gen.get_variables(self.exos_dev.name)

        self.assertEqual(exos_generated_plat_vars, exos_plat_vars)


if __name__ == '__main__':
    RobotUnitTest.main()
