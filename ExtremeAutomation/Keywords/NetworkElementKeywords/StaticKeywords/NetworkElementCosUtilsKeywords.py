from ExtremeAutomation.Library.Utils.ListUtils import ListUtils
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass \
    import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.CosConstants \
    import CosConstants as CommandConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.CosConstants \
    import CosConstants as ParseConstants
from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementCosGenKeywords \
    import NetworkElementCosGenKeywords as GeneratedCosKeywords


class NetworkElementCosUtilsKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementCosUtilsKeywords, self).__init__()
        self.api_const = self.constants.API_COS
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.gen_cos = GeneratedCosKeywords()

    # ##################################################################################################################
    #   Configuration Keywords   #######################################################################################
    # ##################################################################################################################
    def configure_txq_weights(self, device_name, group, weights, **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device(s) the keyword should run against.
        [group] - The TXQ port group that should be configured.
                  EOS group format should be #.# for group number and port type.
        [weights] - The weight that should be given to each queue. Should be in the format of
                    "#,#,#,#,#,#,#,#" for 8 queues "#,#,#,#,#,#,#,#,#,#,#" for 11 queues, or
                    "#,#,#,#,#,#,#,#,#,#,#,#,#,#,#" for 15 queues.

        Configures the weight for each TXQ on a given device.
        """
        device_name = ListUtils.convert_to_list(device_name)

        kw_results = []
        for device_name in device_name:
            dev, cmd_api, _ = self._init_keyword(device_name, self.constants.API_COS, **kwargs)

            args = {"group": group,
                    "weights": weights}

            if dev.oper_sys == self.constants.OS_EXOS:
                weights_list = weights.split(",")

                if len(weights_list) != 8:
                    self.logger.log_error("Invalid number of queues specified for EXOS, only 8 queues supported.")
                else:
                    for index, weight in enumerate(weights_list):
                        args["txq"] = "qp" + str(index + 1)
                        args["weight"] = weight

                        cmd_obj = dev.send_command_object(cmd_api.set_txq_weights(args))
                        kw_results.append(self._determine_result(dev, cmd_obj))
            else:
                cmd_obj = dev.send_command_object(cmd_api.set_txq_weights(args))
                kw_results.append(self._determine_result(dev, cmd_obj))
        return self._keyword_cleanup(kw_results)

  

   
