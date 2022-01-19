from extauto.common.WebElementHandler import *
from extauto.xiq.defs.EventsWebElementsDefs import *


class EventsWebElements(EventsWebElementsDefs):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_events_refresh_button(self):
        return self.weh.get_element(self.events_refresh_button)

    def get_events_download_button(self):
        return self.weh.get_element(self.events_download_button)

    def get_events_content_grid(self):
        return self.weh.get_elements(self.events_content_grid)

    def get_events_pagination(self):
        return self.weh.get_element(self.events_pagination)
