import unittest
import itertools
from ExtremeAutomation.Library.Utils.CloudConnect import CloudConnectEncryption
from ExtremeAutomation.Library.Utils.CloudConnect.CloudConnectRoutes import CloudConnectRoutes
from ExtremeAutomation.Unittests.PythonTests.UtilTests.CloudConnectUnitTestConstants import \
    CloudConnectUnitTestConstants


class CcsResponseTest(unittest.TestCase):
    """
    Unit Test setup and teardown methods.
    Run before/after each test case.
    """

    def setUp(self):
        self.ccr = CloudConnectRoutes()
        self.cce = CloudConnectEncryption
        self.serial = "1111-ASDF"
        self.test_count = 0

    def tearDown(self):
        pass

    ####################################################################################################################
    # ###   Test Cases   ###############################################################################################
    ####################################################################################################################
    def test_connect_response(self):
        action = ["ACCEPT", "PENDING", "REDIRECT", "RESET"]
        standby_timeout = [5, 10, 50, 100, 500, 1000, 3600]
        login = ["admin", "administrator", "robot", "user", "BeExtreme!"]
        password = ["extreme", "admin", "administrator", "robot", "user", "BeExtreme!"]

        combos = list(itertools.product(action, standby_timeout, login, password))
        for i, combo in enumerate(combos):
            print("Test Iteration: " + str(i))
            self.test_count += 1
            json_dict = {"serial": self.serial,
                         "action": combo[0],
                         "standby_timeout": combo[1],
                         "login": combo[2],
                         "password": combo[3]}
            self.ccr.configure_connect(json_dict)
            self.assertEqual(self.ccr.connect(self.serial), self.connect_verify(combo[0], combo[1], combo[2], combo[3]))
        print("Test count: " + str(self.test_count))

    def test_upgrade_response(self):
        upgrade = [True, False]
        uri = ["http://extremecontrol.extremenetworks.com/images/summitX-VERSION1.xos",
               "https://extremecontrol.extremenetworks.com/images/summitX-VERSION2.xmod",
               "tftp://extremecontrol.extremenetworks.com/images/summitX-VERSION2.xos",
               "ftp://devices.extremenetworks.com/images/summitX-VERSION2.xos",
               "ssh://devices.extremenetworks.com/images/summitX-VERSION2.xos",
               "scp://devices.extremenetworks.com/images/summitX-VERSION2.xml"]
        timeout = [5, 10, 50, 100, 500, 1000, 3600]
        asset_name = [["summitX-VERSION1.xos", "!@#$%^&*()", "<>?{}:]=+-_>"]]
        asset_version = ["1.0.0.1", "1.1.1.2", "1.1.1.1", "2.2.2.2", "444.555.666.777.888.999"]
        asset_type = ["firmware", "xmod", "script", "library", "xml", "other"]
        asset_size = ["1234567", "9876", "987654321", "00000000", "000001", "777777777777777777777777777"]

        combos = list(itertools.product(upgrade, uri, timeout, asset_name, asset_version, asset_type, asset_size))
        for i, combo in enumerate(combos, 0):
            self.test_count += 1
            self.ccr.configure_upgrade({"serial": self.serial,
                                        "upgrade": combo[0],
                                        "uri": combo[1],
                                        "timeout": combo[2],
                                        "asset_name": combo[3],
                                        "asset_version": combo[4],
                                        "asset_type": combo[5],
                                        "asset_size": combo[6]})
            self.assertEqual(self.ccr.image_upgrade(self.serial), self.upgrade_verify(combo[0], combo[1], combo[2],
                                                                                      combo[3], combo[4], combo[5],
                                                                                      combo[6]))
        print("Test count: " + str(self.test_count))

    def test_config_response(self):
        json_dict = {"serial": self.serial,
                     self.serial: CloudConnectUnitTestConstants.config_block_robot,
                     "merge": False}
        self.ccr.configure_config(json_dict)
        self.assertEqual(self.ccr.configuration(self.serial, CloudConnectUnitTestConstants.config_block_dut),
                         CloudConnectUnitTestConstants.config_block_robot)

    def test_config_response_merged(self):
        json_dict = {"serial": self.serial,
                     self.serial: CloudConnectUnitTestConstants.config_block_robot,
                     "merge": True}
        self.ccr.configure_config(json_dict)
        self.assertEqual(self.ccr.configuration(self.serial, CloudConnectUnitTestConstants.config_block_dut),
                         CloudConnectUnitTestConstants.config_block_result)

    ####################################################################################################################
    # ###   Helper Methods   ###########################################################################################
    ####################################################################################################################
    def connect_verify(self, action, standby, login, passwd):
        return {"action": action,
                "standbyTimeout": standby,
                "credentials": {
                    "login": self.cce.des3_encrypt(login),
                    "password": self.cce.des3_encrypt(passwd)}}

    @staticmethod
    def upgrade_verify(upgrade, uri, timeout, asset_name, asset_version, asset_type, asset_size):
        return {"imageUpgradeBlock": [{
            "upgrade": upgrade,
            "uri": uri,
            "timeout": timeout,
            "assetName": asset_name,
            "assetVersion": asset_version,
            "assetType": asset_type.upper(),
            "assetSize": int(asset_size)}
        ]}


if __name__ == '__main__':
    unittest.main()
