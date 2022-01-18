import mock
from ExtremeAutomation.Unittests.Utilities.RobotUnitTest import RobotUnitTest
from ExtremeAutomation.Library.Device.Common.Agents.CliAgent import CliAgent
from ExtremeAutomation.Library.Device.Common.Agents.TelnetAgent import TelnetAgent
from ExtremeAutomation.Library.Device.Common.PromptHandler.PromptObj import PromptObj
from ExtremeAutomation.Library.Device.Common.PromptHandler.ALPHA.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as AlphaPromptHandler
from ExtremeAutomation.Library.Device.Common.PromptHandler.BOSS.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as BossPromptHandler
from ExtremeAutomation.Library.Device.Common.PromptHandler.EOS.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as EosPromptHandler
from ExtremeAutomation.Library.Device.Common.PromptHandler.EOSSTACKS.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as EosStacksPromptHandler
from ExtremeAutomation.Library.Device.Common.PromptHandler.EXTRWIRELESS.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as ExtrWirelessPromptHandler
from ExtremeAutomation.Library.Device.Common.PromptHandler.SLX.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as SlxPromptHandler
from ExtremeAutomation.Library.Device.Common.PromptHandler.VOSS.base.baseversion.baseunit.PromptHandler \
    import PromptHandler as VossPromptHandler


class PromptHandlerUnittest(RobotUnitTest):
    debug = False

    def setUp(self):
        self.create_dummy_devices()
        self.configure_alpha_device()
        self.configure_boss_device()
        self.configure_eos_device()
        self.configure_eos_stacks_device()
        self.configure_extr_wireless_device()
        self.configure_slx_device()
        self.configure_voss_device()

    # +------------------+
    # | Helper Functions |
    # +------------------+
    def configure_alpha_device(self):
        self.alpha_dev.version = "1.1.1"
        self.alpha_dev.current_agent = TelnetAgent(self.alpha_dev)
        self.alpha_dev.prompt_handler = AlphaPromptHandler(self.alpha_dev)
        self.alpha_dev.prompt_handler.debug = self.debug

    def configure_boss_device(self):
        self.boss_dev.version = "1.1.1"
        self.boss_dev.current_agent = TelnetAgent(self.boss_dev)
        self.boss_dev.prompt_handler = BossPromptHandler(self.boss_dev)
        self.boss_dev.prompt_handler.debug = self.debug

    def configure_eos_device(self):
        self.eos_dev.version = "08.62.04.0001"
        self.eos_dev.debug_password = "kVzst64Qxq"
        self.eos_dev.current_agent = TelnetAgent(self.eos_dev)
        self.eos_dev.prompt_handler = EosPromptHandler(self.eos_dev)
        self.eos_dev.prompt_handler.debug = self.debug

    def configure_eos_stacks_device(self):
        self.eos_stacks_dev.version = "1.1.1"
        self.eos_stacks_dev.current_agent = TelnetAgent(self.eos_stacks_dev)
        self.eos_stacks_dev.prompt_handler = EosStacksPromptHandler(self.eos_stacks_dev)
        self.eos_stacks_dev.prompt_handler.debug = self.debug

    def configure_extr_wireless_device(self):
        self.extr_wireless_dev.version = "1.1.1"
        self.extr_wireless_dev.current_agent = TelnetAgent(self.extr_wireless_dev)
        self.extr_wireless_dev.prompt_handler = ExtrWirelessPromptHandler(self.extr_wireless_dev)
        self.extr_wireless_dev.prompt_handler.debug = self.debug

    def configure_slx_device(self):
        self.slx_dev.version = "1.1.1"
        self.slx_dev.current_agent = TelnetAgent(self.slx_dev)
        self.slx_dev.prompt_handler = SlxPromptHandler(self.slx_dev)
        self.slx_dev.prompt_handler.debug = self.debug

    def configure_voss_device(self):
        self.voss_dev.version = "1.1.1"
        self.voss_dev.current_agent = TelnetAgent(self.voss_dev)
        self.voss_dev.prompt_handler = VossPromptHandler(self.voss_dev)
        self.voss_dev.prompt_handler.debug = self.debug

    def user_chain(self):
        return [PromptObj(self.constants.PROMPT_USER)]

    def debug_chain(self):
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_DEBUG)]

    def router_chain(self):
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_ROUTER_BASE)]

    def router_config_chain(self, base=False):
        if base:
            return [PromptObj(self.constants.PROMPT_USER),
                    PromptObj(self.constants.PROMPT_ROUTER_BASE),
                    PromptObj(self.constants.PROMPT_ROUTER_CONFIG)]
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_ROUTER_CONFIG)]

    def interface_chain(self, interface_name, base=False):
        if base:
            return [PromptObj(self.constants.PROMPT_USER),
                    PromptObj(self.constants.PROMPT_ROUTER_BASE),
                    PromptObj(self.constants.PROMPT_ROUTER_CONFIG),
                    PromptObj(self.constants.PROMPT_INTERFACE, interface_name=interface_name)]
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_ROUTER_CONFIG),
                PromptObj(self.constants.PROMPT_INTERFACE, interface_name=interface_name)]

    def router_proto_chain(self, proto, instance, base=False):
        if base:
            return [PromptObj(self.constants.PROMPT_USER),
                    PromptObj(self.constants.PROMPT_ROUTER_BASE),
                    PromptObj(self.constants.PROMPT_ROUTER_CONFIG),
                    PromptObj(self.constants.PROMPT_ROUTER_PROTO, router_proto=proto, protocol_instance=instance)]
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_ROUTER_CONFIG),
                PromptObj(self.constants.PROMPT_ROUTER_PROTO, router_proto=proto, protocol_instance=instance)]

    def topology_chain(self):
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY)]

    def base_role_chain(self):
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE)]

    def role_chain(self, role_name):
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ROLE, role_name=role_name)]

    def acl_filter_chain(self, role_name):
        return [PromptObj(self.constants.PROMPT_USER),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ROLE, role_name=role_name),
                PromptObj(self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER)]

    def check_chain(self, actual, expected):
        if len(actual) == len(expected):
            for a, e in zip(actual, expected):
                if a.prompt_name != e.prompt_name:
                    return False
                if a.prompt_name == self.constants.PROMPT_INTERFACE:
                    if a.interface_name != e.interface_name:
                        return False
                elif a.prompt_name == self.constants.PROMPT_ROUTER_PROTO:
                    if a.router_proto != e.router_proto or a.protocol_instance != e.protocol_instance:
                        return False
                elif a.prompt_name == self.constants.PROMPT_EXTR_WIRELESS_ROLE:
                    if a.role_name != e.role_name:
                        return False
            return True
        else:
            return False

    # +----------------------------+
    # | Alpha Prompt Handler Tests |
    # +----------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.alpha_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.alpha_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_handler_debug(self, mock_agent):
        mock_agent.return_value = ""

        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()

        return_flag, error = self.alpha_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.alpha_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_handler_config(self, mock_agent):
        mock_agent.return_value = ""

        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()

        return_flag, error = self.alpha_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.alpha_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_handler_interface(self, mock_agent):
        mock_agent.return_value = ""

        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        return_flag, error = self.alpha_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.alpha_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_handler_router_proto(self, mock_agent):
        mock_agent.return_value = ""

        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.alpha_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        return_flag, error = self.alpha_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.alpha_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_user_change(self, mock_agent):
        mock_agent.return_value = ""

        self.assertTrue(self.alpha_dev.prompt_handler.user_to_config())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.user_to_debug())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.user_to_interface("1"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.alpha_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.user_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_debug_change(self, mock_agent):
        mock_agent.return_value = ""
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.debug_to_config())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.debug_to_user())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.debug_to_interface("1"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.alpha_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.debug_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_router_config_change(self, mock_agent):
        mock_agent.return_value = ""
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.config_to_debug())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.config_to_user())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.config_to_interface("1"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.alpha_dev.prompt_handler.config_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_interface_change(self, mock_agent):
        mock_agent.return_value = ""
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.alpha_dev.prompt_handler.interface_to_debug())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.alpha_dev.prompt_handler.interface_to_user())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.alpha_dev.prompt_handler.interface_to_config())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.alpha_dev.prompt_handler.interface_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.alpha_dev.prompt_handler.interface_to_interface("2"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.interface_chain("2", True)))
        self.alpha_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.alpha_dev.prompt_handler.interface_to_interface("1"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_alpha_router_proto_change(self, mock_agent):
        mock_agent.return_value = ""
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.alpha_dev.prompt_handler.router_proto_to_debug())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.alpha_dev.prompt_handler.router_proto_to_user())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.alpha_dev.prompt_handler.router_proto_to_config())
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.alpha_dev.prompt_handler.router_proto_to_interface("1"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.alpha_dev.prompt_handler.router_proto_to_router_proto("3", "4"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("3", "4", True)))
        self.alpha_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.alpha_dev.prompt_handler.router_proto_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.alpha_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    # +---------------------------+
    # | BOSS Prompt Handler Tests |
    # +---------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.boss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.boss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_handler_debug(self, mock_agent):
        mock_agent.return_value = ""

        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()

        return_flag, error = self.boss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.boss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_handler_config(self, mock_agent):
        mock_agent.return_value = ""

        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        return_flag, error = self.boss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.boss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_handler_interface(self, mock_agent):
        mock_agent.return_value = ""

        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        return_flag, error = self.boss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.boss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_handler_router_proto(self, mock_agent):
        mock_agent.return_value = ""

        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.boss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        return_flag, error = self.boss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.boss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_user_change(self, mock_agent):
        mock_agent.return_value = ""

        self.assertTrue(self.boss_dev.prompt_handler.user_to_config())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.boss_dev.prompt_handler.user_to_debug())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.boss_dev.prompt_handler.user_to_interface("1"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.boss_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.boss_dev.prompt_handler.user_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_debug_change(self, mock_agent):
        mock_agent.return_value = ""
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.boss_dev.prompt_handler.debug_to_config())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.boss_dev.prompt_handler.debug_to_user())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.boss_dev.prompt_handler.debug_to_interface("1"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.boss_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.boss_dev.prompt_handler.debug_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_router_config_change(self, mock_agent):
        mock_agent.return_value = ""
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.boss_dev.prompt_handler.config_to_debug())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.boss_dev.prompt_handler.config_to_user())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.boss_dev.prompt_handler.config_to_interface("1"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.boss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.boss_dev.prompt_handler.config_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_interface_change(self, mock_agent):
        mock_agent.return_value = ""
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.boss_dev.prompt_handler.interface_to_debug())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.boss_dev.prompt_handler.interface_to_user())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.boss_dev.prompt_handler.interface_to_config())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.boss_dev.prompt_handler.interface_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.boss_dev.prompt_handler.interface_to_interface("2"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.interface_chain("2", True)))
        self.boss_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.boss_dev.prompt_handler.interface_to_interface("1"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_boss_router_proto_change(self, mock_agent):
        mock_agent.return_value = ""
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.boss_dev.prompt_handler.router_proto_to_debug())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.boss_dev.prompt_handler.router_proto_to_user())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.boss_dev.prompt_handler.router_proto_to_config())
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.boss_dev.prompt_handler.router_proto_to_interface("1"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.boss_dev.prompt_handler.router_proto_to_router_proto("3", "4"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("3", "4", True)))
        self.boss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.boss_dev.prompt_handler.router_proto_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.boss_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    # +--------------------------+
    # | EOS Prompt Handler Tests |
    # +--------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.eos_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_handler_debug(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()

        return_flag, error = self.eos_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_handler_router_base(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()

        return_flag, error = self.eos_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_handler_config(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        return_flag, error = self.eos_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_handler_interface(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        return_flag, error = self.eos_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_handler_router_proto(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        return_flag, error = self.eos_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_user_change(self, mock_agent):
        mock_agent.return_value = ""

        self.assertTrue(self.eos_dev.prompt_handler.user_to_router())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_dev.prompt_handler.user_to_config())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_config_chain(True)))
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_dev.prompt_handler.user_to_debug())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_dev.prompt_handler.user_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_dev.prompt_handler.user_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_debug_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_dev.prompt_handler.debug_to_router())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_dev.prompt_handler.debug_to_config())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_config_chain(True)))
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_dev.prompt_handler.debug_to_user())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_dev.prompt_handler.debug_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_dev.prompt_handler.debug_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_router_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_dev.prompt_handler.router_to_debug())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_dev.prompt_handler.router_to_config())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_config_chain(True)))
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_dev.prompt_handler.router_to_user())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_dev.prompt_handler.router_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_dev.prompt_handler.router_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_router_config_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_dev.prompt_handler.config_to_debug())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_dev.prompt_handler.config_to_router())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_dev.prompt_handler.config_to_user())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_dev.prompt_handler.config_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_dev.prompt_handler.config_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_interface_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_debug())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_router())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_user())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_config())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_config_chain(True)))
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_interface("2"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("2", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_dev.prompt_handler.interface_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_router_proto_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_debug())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_router())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_user())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_config())
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.router_config_chain(True)))
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_router_proto("3", "4"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("3", "4", True)))
        self.eos_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_dev.prompt_handler.router_proto_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    # +--------------------------------+
    # | EOS Stack Prompt Handler Tests |
    # +--------------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stack_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.eos_stacks_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_stacks_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stack_handler_debug(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()

        return_flag, error = self.eos_stacks_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_stacks_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stack_handler_router_base(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()

        return_flag, error = self.eos_stacks_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_stacks_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stack_handler_config(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        return_flag, error = self.eos_stacks_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_stacks_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stack_handler_interface(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        return_flag, error = self.eos_stacks_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_stacks_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stack_handler_router_proto(self, mock_agent):
        mock_agent.return_value = ""

        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_BASE, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_DEBUG, "")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)
        self.assertTrue(self.eos_stacks_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        return_flag, error = self.eos_stacks_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.eos_stacks_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stacks_user_change(self, mock_agent):
        mock_agent.return_value = ""

        self.assertTrue(self.eos_stacks_dev.prompt_handler.user_to_router())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.user_to_config())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_config_chain(True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.user_to_debug())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.user_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("1", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.user_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stacks_debug_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.debug_to_router())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.debug_to_config())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_config_chain(True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.debug_to_user())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.debug_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("1", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.debug_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.debug_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stacks_router_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_to_debug())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_to_config())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_config_chain(True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_to_user())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("1", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_chain()

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stacks_router_config_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.config_to_debug())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.config_to_router())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.config_to_user())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.config_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("1", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_config_chain(True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.config_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stacks_interface_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_debug())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_router())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_user())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_config())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_config_chain(True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_interface("2"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("2", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.interface_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("1", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_eos_stacks_router_proto_change(self, mock_agent):
        mock_agent.return_value = ""
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_debug())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.debug_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_router())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.router_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_user())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_config())
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_config_chain(True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_interface("1"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.interface_chain("1", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_router_proto("3", "4"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("3", "4", True)))
        self.eos_stacks_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.eos_stacks_dev.prompt_handler.router_proto_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.eos_stacks_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    # +---------------------------------------+
    # | Extreme Wireless Prompt Handler Tests |
    # +---------------------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_USER, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ROLE, "1")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER, "2||3")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.extr_wireless_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.extr_wireless_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_handler_topology(self, mock_agent):
        mock_agent.return_value = ""

        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_USER, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ROLE, "1")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER, "2||3")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()

        return_flag, error = self.extr_wireless_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.extr_wireless_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_handler_base_role(self, mock_agent):
        mock_agent.return_value = ""

        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_USER, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ROLE, "1")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER, "2||3")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()

        return_flag, error = self.extr_wireless_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.extr_wireless_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_handler_role(self, mock_agent):
        mock_agent.return_value = ""

        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_USER, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ROLE, "1")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER, "2||3")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        return_flag, error = self.extr_wireless_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.extr_wireless_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_handler_acl_filter(self, mock_agent):
        mock_agent.return_value = ""

        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_USER, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_TOPOLOGY, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_BASE_ROLE, "")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ROLE, "1")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")
        self.assertTrue(self.extr_wireless_dev.prompt_handler.change_prompt(
            self.constants.PROMPT_EXTR_WIRELESS_ACLFILTER, "2||3")[0])
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        return_flag, error = self.extr_wireless_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.extr_wireless_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_user_change(self, mock_agent):
        mock_agent.return_value = ""
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.user_to_topology())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.topology_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.user_to_base_role())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.base_role_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.user_to_role("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.user_to_acl_filter("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("2")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_topology_change(self, mock_agent):
        mock_agent.return_value = ""
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.topology_to_user())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.topology_to_base_role())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.base_role_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.topology_to_role("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.topology_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.topology_to_acl_filter("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("2")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_base_role_change(self, mock_agent):
        mock_agent.return_value = ""
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.base_role_to_user())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.base_role_to_topology())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.topology_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.base_role_to_role("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.base_role_chain()

        self.assertTrue(self.extr_wireless_dev.prompt_handler.base_role_to_acl_filter("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("2")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_role_change(self, mock_agent):
        mock_agent.return_value = ""
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_user())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_topology())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.topology_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_role("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_role("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("2")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_base_role())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.base_role_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_acl_filter("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.role_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.role_to_acl_filter("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("2")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_extr_wireless_aclfilter_change(self, mock_agent):
        mock_agent.return_value = ""
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_user())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_topology())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.topology_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_role("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_role("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.role_chain("2")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_base_role())
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain, self.base_role_chain()))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_acl_filter("1"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("1")))
        self.extr_wireless_dev.prompt_handler.prompt_chain = self.acl_filter_chain("1")

        self.assertTrue(self.extr_wireless_dev.prompt_handler.acl_filter_to_acl_filter("2"))
        self.assertTrue(self.check_chain(self.extr_wireless_dev.prompt_handler.prompt_chain,
                                         self.acl_filter_chain("2")))

    # +--------------------------+
    # | SLX Prompt Handler Tests |
    # +--------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.slx_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.slx_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_handler_config(self, mock_agent):
        mock_agent.return_value = ""

        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()

        return_flag, error = self.slx_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.slx_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_handler_interface(self, mock_agent):
        mock_agent.return_value = ""

        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        return_flag, error = self.slx_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.slx_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_handler_router_proto(self, mock_agent):
        mock_agent.return_value = ""

        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.slx_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        return_flag, error = self.slx_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.slx_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_user_change(self, mock_agent):
        mock_agent.return_value = ""

        self.assertTrue(self.slx_dev.prompt_handler.user_to_config())
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.slx_dev.prompt_handler.user_to_interface("1"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.slx_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.slx_dev.prompt_handler.user_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_router_config_change(self, mock_agent):
        mock_agent.return_value = ""
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.slx_dev.prompt_handler.config_to_user())
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.slx_dev.prompt_handler.config_to_interface("1"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.slx_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.slx_dev.prompt_handler.config_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_interface_change(self, mock_agent):
        mock_agent.return_value = ""
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.slx_dev.prompt_handler.interface_to_user())
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.slx_dev.prompt_handler.interface_to_config())
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.slx_dev.prompt_handler.interface_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.slx_dev.prompt_handler.interface_to_interface("2"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.interface_chain("2", True)))
        self.slx_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.slx_dev.prompt_handler.interface_to_interface("1"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_slx_router_proto_change(self, mock_agent):
        mock_agent.return_value = ""
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.slx_dev.prompt_handler.router_proto_to_user())
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.slx_dev.prompt_handler.router_proto_to_config())
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.slx_dev.prompt_handler.router_proto_to_interface("1"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.slx_dev.prompt_handler.router_proto_to_router_proto("3", "4"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("3", "4", True)))
        self.slx_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.slx_dev.prompt_handler.router_proto_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.slx_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))

    # +---------------------------+
    # | VOSS Prompt Handler Tests |
    # +---------------------------+
    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_handler_user(self, mock_agent):
        mock_agent.return_value = ""

        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()

        return_flag, error = self.voss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.voss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_handler_config(self, mock_agent):
        mock_agent.return_value = ""

        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        return_flag, error = self.voss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.voss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_handler_interface(self, mock_agent):
        mock_agent.return_value = ""

        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        return_flag, error = self.voss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.voss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_handler_router_proto(self, mock_agent):
        mock_agent.return_value = ""

        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_USER, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_CONFIG, "")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_INTERFACE, "1")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")
        self.assertTrue(self.voss_dev.prompt_handler.change_prompt(self.constants.PROMPT_ROUTER_PROTO, "2||3")[0])
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        return_flag, error = self.voss_dev.prompt_handler.change_prompt("bad prompt", "")

        self.assertFalse(return_flag)
        self.assertEqual(error, "Unrecognized prompt (" + self.voss_dev.oper_sys + "): bad prompt")

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_user_change(self, mock_agent):
        mock_agent.return_value = ""

        self.assertTrue(self.voss_dev.prompt_handler.user_to_config())
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.voss_dev.prompt_handler.user_to_interface("1"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.voss_dev.prompt_handler.prompt_chain = self.user_chain()

        self.assertTrue(self.voss_dev.prompt_handler.user_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_router_config_change(self, mock_agent):
        mock_agent.return_value = ""
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.voss_dev.prompt_handler.config_to_user())
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.voss_dev.prompt_handler.config_to_interface("1"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.voss_dev.prompt_handler.prompt_chain = self.router_config_chain()

        self.assertTrue(self.voss_dev.prompt_handler.config_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_interface_change(self, mock_agent):
        mock_agent.return_value = ""
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.voss_dev.prompt_handler.interface_to_user())
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.voss_dev.prompt_handler.interface_to_config())
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1")

        self.assertTrue(self.voss_dev.prompt_handler.interface_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.router_proto_chain("2", "3")))
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.voss_dev.prompt_handler.interface_to_interface("2"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.interface_chain("2", True)))
        self.voss_dev.prompt_handler.prompt_chain = self.interface_chain("1", True)

        self.assertTrue(self.voss_dev.prompt_handler.interface_to_interface("1"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.interface_chain("1", True)))

    @mock.patch.object(CliAgent, "send_command_wait_for_prompt")
    def test_voss_router_proto_change(self, mock_agent):
        mock_agent.return_value = ""
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.voss_dev.prompt_handler.router_proto_to_user())
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.user_chain()))
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.voss_dev.prompt_handler.router_proto_to_config())
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.router_config_chain()))
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3")

        self.assertTrue(self.voss_dev.prompt_handler.router_proto_to_interface("1"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain, self.interface_chain("1")))
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.voss_dev.prompt_handler.router_proto_to_router_proto("3", "4"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("3", "4", True)))
        self.voss_dev.prompt_handler.prompt_chain = self.router_proto_chain("2", "3", True)

        self.assertTrue(self.voss_dev.prompt_handler.router_proto_to_router_proto("2", "3"))
        self.assertTrue(self.check_chain(self.voss_dev.prompt_handler.prompt_chain,
                                         self.router_proto_chain("2", "3", True)))


if __name__ == '__main__':
    RobotUnitTest.main()
