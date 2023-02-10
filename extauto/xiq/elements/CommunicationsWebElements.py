from extauto.xiq.defs.CommunicationsWebElementDefs import CommunicationsWebElementDefs
from extauto.common.WebElementHandler import WebElementHandler


class CommunicationsWebElements(CommunicationsWebElementDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_communications_page_error_field(self):
        return self.weh.get_element(self.field_form_error)

    def get_communications_page_text(self):
        return self.weh.get_element(self.comm_page_text)

    def get_notifications_page_text(self):
        return self.weh.get_element(self.notification_page_text)

    def get_previews_page_text(self):
        return self.weh.get_element(self.preview_page_text)

    def get_new_in_extremecloud_page_text(self):
        return self.weh.get_element(self.new_in_extreme_page_text)

    def get_notifications_nav(self):
        return self.weh.get_element(self.communications_notification_nav)

    def get_preview_nav(self):
        return self.weh.get_element(self.communications_preview_nav)

    def get_new_updates_nav(self):
        return self.weh.get_element(self.communications_new_updates_nav)

    def get_iframe_url(self):
        url = self.weh.get_element(self.iframe_url)
        url_href = self.weh.get_element(self.iframe_url_href, parent=url)
        return url_href.get_attribute("src")
