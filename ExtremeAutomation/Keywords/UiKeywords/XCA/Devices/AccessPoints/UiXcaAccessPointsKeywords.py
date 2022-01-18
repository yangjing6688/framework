from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.XCA.XcaaccesspointsConstants import \
    XcaaccesspointsConstants
from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass


class UiXcaAccessPointsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiXcaAccessPointsKeywords, self).__init__()
        self.api_const = self.constants.API_XCA_ACCESS_POINTS
        self.command_const = XcaaccesspointsConstants()

    def access_points_verify_access_point_is_associated_with_site(self, element_names, access_point_name,
                                                                  site_name, **kwargs):
        """Returns the result of access_points_verify_access_point_is_associated_with_site."""
        args = {"access_point_name": access_point_name,
                "site_name": site_name}

        return self.execute_keyword(element_names, args,
                                    self.command_const.VERIFY_ACCESS_POINT_IS_ASSOCIATED_WITH_SITE, **kwargs)
