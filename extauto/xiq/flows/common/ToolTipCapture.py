from time import sleep
import threading
from extauto.common.CloudDriver import CloudDriver


tool_tip_text = None


def tool_tip_capture():
    """
    Capture tool tip in daemon process and append to global list

    :return: None
    """
    global tool_tip_text
    tool_tip_text = []
    # driver = extauto.common.CloudDriver.cloud_driver
    t = threading.current_thread()
    while getattr(t, "do_run", True):
        try:
            tool_tip_elemnt = CloudDriver().cloud_driver.find_element_by_css_selector(".ui-tipbox-ctn")
            if text := tool_tip_elemnt.text:
                if text not in tool_tip_text:
                    tool_tip_text.append(text)

            tool_tip_elemnts = CloudDriver().cloud_driver.find_elements_by_css_selector(".ui-tipbox-title")
            for tool_tip_element in tool_tip_elemnts:
                if text := tool_tip_element.text:
                    if text not in tool_tip_text:
                        tool_tip_text.append(text)
            sleep(1)
        except Exception as e:
            pass
