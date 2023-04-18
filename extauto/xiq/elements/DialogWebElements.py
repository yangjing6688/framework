from extauto.xiq.defs.DialogWebElementsDefinitions import DialogWebElementsDefinitions
from extauto.common.WebElementHandler import WebElementHandler


class DialogWebElements(DialogWebElementsDefinitions):
    def __init__(self):
        self.weh = WebElementHandler()

    def get_dialog_box(self):
        return self.weh.get_element(self.dialog_box)

    def get_dialog_message(self):
        if self.weh.get_element(self.dialog_message) is not None:
            return self.weh.get_element(self.dialog_message).text
        else:
            return False

    def get_dialog_box_ok_button(self):
        parent = self.get_dialog_box()
        return self.weh.get_element(self.dialog_ok_button, parent)

    def get_tooltip_text(self):
        elements = self.weh.get_elements(self.tooltip)
        for element in elements:
            if element.is_displayed():
                return element.text

    def get_confirm_message_dialog_box(self):
        return self.weh.get_element(self.confirm_message_dialog_box)

    def get_confirm_yes_button(self):
        elements = self.weh.get_elements(self.confirm_yes_button)
        if elements:
            for element in elements:
                if element.is_displayed():
                    return element
        else:
            return None

    def get_confirm_cancel_button(self):
        elements = self.weh.get_elements(self.confirm_cancel_button)
        for element in elements:
            if element.is_displayed():
                return element

    def get_confirm_deploy_button(self):
        elements = self.weh.get_elements(self.confirm_deploy_button)
        for element in elements:
            if element.is_displayed():
                return element

    def get_confirm_yes_button_reboot(self):
        return self.weh.get_elements(self.confirm_yes_button_reboot)

    def get_tooltip_close_button(self):
        return self.weh.get_elements(self.tooltip_close_button)
