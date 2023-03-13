from time import sleep
from extauto.common.AutoActions import AutoActions
from extauto.common.Screen import Screen
from extauto.common.Utils import Utils
from extauto.xiq.flows.manage.Devices import Devices
from extauto.xiq.flows.manage.Client import Client
from extauto.xiq.elements.DeviceActions import DeviceActions
from extauto.xiq.elements.MLInsightsScoreCardWebElements import MLInsightsScoreCardWebElements
from extauto.xiq.elements.MLInsightsWebElements import MLInsightsWebElements
from extauto.xiq.elements.NavigatorWebElements import NavigatorWebElements
from extauto.common.CommonValidation import CommonValidation


class Network360ScoreCard:

    def __init__(self):
        self.navigator = NavigatorWebElements()
        self.auto_actions = AutoActions()
        self.dev_action = DeviceActions()
        self.utils = Utils()
        self.dev = Devices()
        self.ml_insights = MLInsightsWebElements()
        self.ml_insights_sc = MLInsightsScoreCardWebElements()
        self.screen = Screen()
        self.client = Client()
        self.common_validation = CommonValidation()

    def goto_ml_insights_score_card(self, **kwargs):
        """
        - This keyword navigates to Network360 Plan page
        :return: returns 1 if successful
        """
        try:
            self.utils.print_info("Clicking on ML Insights button")
            self.auto_actions.click_reference(self.ml_insights.get_ml_insights_button)
            sleep(2)

            self.utils.print_info("Clicking on ML Insights Score Card button")
            self.auto_actions.click_reference(self.ml_insights.get_n360_scorecard_button)
            sleep(3)
            kwargs['pass_msg'] = "Successfully Clicking on ML Insights Score Card button"
            self.common_validation.passed(**kwargs)
            return 1
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Unable to Navigate to MLInsights Score Card Page"
            self.common_validation.fault(**kwargs)
            return 0

    def score_card_details(self, **kwargs):
        """
        - This keyword gets details of N360 Score Card page
        :return: dictionary of Score Card details
         """
        sleep(5)
        try:
            dev_cur_card_dict = dict()
            dev_cur_card_dict["dev_cur_total"] = self.ml_insights_sc.get_n360_score_dev_health_select_cur_total().text
            dev_cur_card_dict["dev_cur_rating"] = self.ml_insights_sc.get_n360_score_dev_health_select_cur_rating().text
            dev_cur_card_dict["dev_cur_avail"] = self.ml_insights_sc.get_n360_score_dev_health_select_cur_dev_avail().text
            dev_cur_card_dict["dev_cur_hw"] = self.ml_insights_sc.get_n360_score_dev_health_select_cur_dev_hw_health().text
            dev_cur_card_dict["dev_cur_conf"] = self.ml_insights_sc.get_n360_score_dev_health_select_cur_dev_conf_firmware().text

            dev_avg_card_dict = dict()
            dev_avg_card_dict["dev_avg_total"] = self.ml_insights_sc.get_n360_score_dev_health_select_avg_total().text
            dev_avg_card_dict["dev_avg_rating"] = self.ml_insights_sc.get_n360_score_dev_health_select_avg_rating().text
            dev_avg_card_dict["dev_avg_avail"] = self.ml_insights_sc.get_n360_score_dev_health_select_avg_dev_avail().text
            dev_avg_card_dict["dev_avg_hw"] = self.ml_insights_sc.get_n360_score_dev_health_select_avg_dev_hw_health().text
            dev_avg_card_dict["dev_avg_conf"] = self.ml_insights_sc.get_n360_score_dev_health_select_avg_dev_conf_firmware().text

            dev_all_card_dict = dict()
            dev_all_card_dict["dev_all_total"] = self.ml_insights_sc.get_n360_score_dev_health_all_total().text
            dev_all_card_dict["dev_all_rating"] = self.ml_insights_sc.get_n360_score_dev_health_all_rating().text
            dev_all_card_dict["dev_all_avail"] = self.ml_insights_sc.get_n360_score_dev_health_all_dev_avail().text
            dev_all_card_dict["dev_all_hw"] = self.ml_insights_sc.get_n360_score_dev_health_all_dev_hw().text
            dev_all_card_dict["dev_all_conf"] = self.ml_insights_sc.get_n360_score_dev_health_all_conf_firmware().text

            cl_cur_card_dict = dict()
            cl_cur_card_dict["cl_cur_total"] = self.ml_insights_sc.get_n360_score_client_health_select_cur_total().text
            cl_cur_card_dict["cl_cur_rating"] = self.ml_insights_sc.get_n360_score_client_health_select_cur_rating().text
            cl_cur_card_dict["cl_cur_avail"] = self.ml_insights_sc.get_n360_score_client_health_select_cur_dev_avail().text
            cl_cur_card_dict["cl_cur_hw"] = self.ml_insights_sc.get_n360_score_client_health_select_cur_dev_hw_health().text
            cl_cur_card_dict["cl_cur_conf"] = self.ml_insights_sc.get_n360_score_client_health_select_cur_dev_conf_firmware().text

            cl_avg_card_dict = dict()
            cl_avg_card_dict["cl_avg_total"] = self.ml_insights_sc.get_n360_score_client_health_select_avg_total().text
            cl_avg_card_dict["cl_avg_rating"] = self.ml_insights_sc.get_n360_score_client_health_select_avg_rating().text
            cl_avg_card_dict["cl_avg_avail"] = self.ml_insights_sc.get_n360_score_client_health_select_avg_dev_avail().text
            cl_avg_card_dict["cl_avg_hw"] = self.ml_insights_sc.get_n360_score_client_health_select_avg_dev_hw_health().text
            cl_avg_card_dict["cl_avg_conf"] = self.ml_insights_sc.get_n360_score_client_health_select_avg_dev_conf_firmware().text

            cl_all_card_dict = dict()
            cl_all_card_dict["cl_all_total"] = self.ml_insights_sc.get_n360_score_client_health_all_total().text
            cl_all_card_dict["cl_all_rating"] = self.ml_insights_sc.get_n360_score_client_health_all_rating().text
            cl_all_card_dict["cl_all_avail"] = self.ml_insights_sc.get_n360_score_client_health_all_dev_avail().text
            cl_all_card_dict["cl_all_hw"] = self.ml_insights_sc.get_n360_score_client_health_all_dev_hw().text
            cl_all_card_dict["cl_all_conf"] = self.ml_insights_sc.get_n360_score_client_health_all_conf_firmware().text

            wifi_cur_dict = dict()
            wifi_cur_dict["wifi_cur_total"] = self.ml_insights_sc.get_n360_score_wifi_health_select_cur_total().text
            wifi_cur_dict["wifi_cur_rating"] = self.ml_insights_sc.get_n360_score_wifi_health_select_cur_rating().text
            wifi_cur_dict["wifi_cur_snr"] = self.ml_insights_sc.get_n360_score_wifi_health_select_cur_snr_score().text
            wifi_cur_dict["wifi_cur_channel"] = self.ml_insights_sc.get_n360_score_wifi_health_select_cur_channel_util().text
            wifi_cur_dict["wifi_cur_associate"] = self.ml_insights_sc.get_n360_score_wifi_health_select_cur_association().text

            wifi_avg_dict = dict()
            wifi_avg_dict["wifi_avg_total"] = self.ml_insights_sc.get_n360_score_wifi_health_select_avg_total().text
            wifi_avg_dict["wifi_avg_rating"] = self.ml_insights_sc.get_n360_score_wifi_health_select_avg_rating().text
            wifi_avg_dict["wifi_avg_snr"] = self.ml_insights_sc.get_n360_score_wifi_health_select_avg_snr_score().text
            wifi_avg_dict["wifi_avg_channel"] = self.ml_insights_sc.get_n360_score_wifi_health_select_avg_channel_util().text
            wifi_avg_dict["wifi_avg_associate"] = self.ml_insights_sc.get_n360_score_wifi_health_select_avg_association().text

            wifi_all_dict = dict()
            wifi_all_dict["wifi_all_total"] = self.ml_insights_sc.get_n360_score_wifi_health_all_total().text
            wifi_all_dict["wifi_all_rating"] = self.ml_insights_sc.get_n360_score_wifi_health_all_rating().text
            wifi_all_dict["wifi_all_snr"] = self.ml_insights_sc.get_n360_score_wifi_health_all_snr_score().text
            wifi_all_dict["wifi_all_channel"] = self.ml_insights_sc.get_n360_score_wifi_health_all_channel_util().text
            wifi_all_dict["wifi_all_associate"] = self.ml_insights_sc.get_n360_score_wifi_health_all_association().text

            nw_cur_dict = dict()
            nw_cur_dict["nw_cur_total"] = self.ml_insights_sc.get_n360_score_nw_health_select_cur_total().text
            nw_cur_dict["nw_cur_rating"] = self.ml_insights_sc.get_n360_score_nw_health_select_cur_rating().text
            nw_cur_dict["nw_cur_avail"] = self.ml_insights_sc.get_n360_score_nw_health_select_cur_net_avail().text
            nw_cur_dict["nw_cur_perf"] = self.ml_insights_sc.get_n360_score_nw_health_select_cur_net_perf().text
            nw_cur_dict["nw_cur_usage"] = self.ml_insights_sc.get_n360_score_nw_health_select_net_usage().text

            nw_avg_dict = dict()
            nw_avg_dict["nw_avg_total"] = self.ml_insights_sc.get_n360_score_nw_health_select_avg_total().text
            nw_avg_dict["nw_avg_rating"] = self.ml_insights_sc.get_n360_score_nw_health_select_avg_rating().text
            nw_avg_dict["nw_avg_avail"] = self.ml_insights_sc.get_n360_score_nw_health_select_avg_net_avail().text
            nw_avg_dict["nw_avg_perf"] = self.ml_insights_sc.get_n360_score_nw_health_select_avg_net_perf().text
            nw_avg_dict["nw_avg_usage"] = self.ml_insights_sc.get_n360_score_nw_health_select_avg_net_usage().text

            nw_all_dict = dict()
            nw_all_dict["nw_all_total"] = self.ml_insights_sc.get_n360_score_nw_health_all_total().text
            nw_all_dict["nw_all_rating"] = self.ml_insights_sc.get_n360_score_nw_health_all_rating().text
            nw_all_dict["nw_all_avail"] = self.ml_insights_sc.get_n360_score_nw_health_all_net_avail().text
            nw_all_dict["nw_all_perf"] = self.ml_insights_sc.get_n360_score_nw_health_all_net_perf().text
            nw_all_dict["nw_all_usage"] = self.ml_insights_sc.get_n360_score_nw_health_all_net_usage().text

            sv_cur_dict = dict()
            sv_cur_dict["sv_cur_total"] = self.ml_insights_sc.get_n360_score_service_health_select_cur_total().text
            sv_cur_dict["sv_cur_rating"] = self.ml_insights_sc.get_n360_score_service_health_select_cur_rating().text
            sv_cur_dict["sv_cur_net"] = self.ml_insights_sc.get_n360_score_service_health_select_cur_net_service().text
            sv_cur_dict["sv_cur_auth"] = self.ml_insights_sc.get_n360_score_service_health_select_cur_auth_service().text
            sv_cur_dict["sv_cur_manage"] = self.ml_insights_sc.get_n360_score_service_health_select_cur_manage_service().text

            sv_avg_dict = dict()
            sv_avg_dict["sv_avg_total"] = self.ml_insights_sc.get_n360_score_service_health_select_avg_total().text
            sv_avg_dict["sv_avg_rating"] = self.ml_insights_sc.get_n360_score_service_health_select_avg_rating().text
            sv_avg_dict["sv_avg_net"] = self.ml_insights_sc.get_n360_score_service_health_select_avg_net_service().text
            sv_avg_dict["sv_avg_auth"] = self.ml_insights_sc.get_n360_score_service_health_select_avg_auth_service().text
            sv_avg_dict["sv_avg_manage"] = self.ml_insights_sc.get_n360_score_service_health_select_avg_manage_service().text

            sv_all_dict = dict()
            sv_all_dict["sv_all_total"] = self.ml_insights_sc.get_n360_score_service_health_all_total().text
            sv_all_dict["sv_all_rating"] = self.ml_insights_sc.get_n360_score_service_health_all_rating().text
            sv_all_dict["sv_all_net"] = self.ml_insights_sc.get_n360_score_service_health_all_net_service().text
            sv_all_dict["sv_all_auth"] = self.ml_insights_sc.get_n360_score_service_health_all_auth_service().text
            sv_all_dict["sv_all_manage"] = self.ml_insights_sc.get_n360_score_service_health_all_manage_service().text

            device_health_list = [dev_cur_card_dict, dev_avg_card_dict, dev_all_card_dict]
            client_health_list = [cl_cur_card_dict, cl_avg_card_dict, cl_all_card_dict]
            wifi_health_list = [wifi_cur_dict, wifi_avg_dict, wifi_all_dict]
            network_health_list = [nw_cur_dict, nw_avg_dict, nw_all_dict]
            service_health_list = [sv_cur_dict, sv_avg_dict, sv_all_dict]

            self.utils.print_info("Device Health List")
            self.utils.print_info(device_health_list)
            self.utils.print_info("Client Health List")
            self.utils.print_info(client_health_list)
            self.utils.print_info("Wifi Health List")
            self.utils.print_info(wifi_health_list)
            self.utils.print_info("Network Health List")
            self.utils.print_info(network_health_list)
            self.utils.print_info("Service Health List")
            self.utils.print_info(service_health_list)

            return device_health_list, client_health_list, network_health_list, wifi_health_list, service_health_list
        except Exception as e:
            self.utils.print_info(e)
            kwargs['fail_msg'] = "Unable to get MLInsights Score Card Details"
            self.common_validation.fault(**kwargs)
            return -1
