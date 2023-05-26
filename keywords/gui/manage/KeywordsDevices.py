# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
import inspect
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

# Keyword imports required to run keywords implemented in this file
from extauto.xiq.xapi.manage.XapiDevices import XapiDevices
from extauto.xiq.flows.manage.Devices import Devices


class KeywordsDevices(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        # Object used to run keywords implemented in this file
        self.devices = Devices()
        self.xapiDevices = XapiDevices()

    def search_device(self, device_dict, select_device=False, skip_refresh=False, skip_navigation=False, **kwargs):
        """
        Searches for a device identified by 'serial' or 'mac' provided in device_dict

        search_device will search in the devices page for a specific device looking for 'mac' address first,
        then 'serial' number. The device (if found) can be optionally selected. Normally this keyword will navigate
        to the devices page and refresh the table, both of these can be skipped.

        Keyword Usage:
          Robot:
             Library  keywords/gui/manage/KeywordsDevices.py
             Search Device  ${ap1}    skip_refresh=True  skip_navigation=True

          Pytest:
             Imports:
                from keywords.gui.manage.KeywordsDevices import KeywordsDevices
             Calling Keyword:
                kwDevices = KeywordsDevices()
                kwDevices.search_device(self.tb.dut1, skip_refresh=True, skip_navigation=True)

        Keyword Implementations:
           GUI
           XAPI - Note that for XAPI, the refresh and navigation cannot be skipped, also the device cannot be selected

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1)
        :param select_device: True - to select the device, default set to False
        :param skip_refresh: True - to skip the refresh of the devices page, default set to False
        :param skip_navigation: True - to skip the navigation to the devices page, default set to False
        :param kwargs: Supports all standard kwargs

        :return: 1 if device found else -1
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("f7c9504a-9a3a-4398-afc1-be43dcfcb9a0", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        if 'serial' not in device_dict.keys() and 'mac' not in device_dict.keys():
            kwargs['fail_msg'] = "Invalid keyword arguments: ‘serial’ or ‘mac’ must be included in device_dict"

        # Assume a failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.devices.gui_search_device(device_dict, skip_refresh=skip_refresh,
                                                                 skip_navigation=skip_navigation, **kwargs)

                else:
                    if not select_device:
                        return_code = self.xapiDevices.xapi_search_device(device_dict=device_dict, **kwargs)
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def select_device(self, device_dict, skip_refresh=False, skip_navigation=False, **kwargs):
        """
         Selects a device identified by 'serial' or 'mac' provided in device_dict

         In the devices page, select_device will select a specific device using 'mac' address first,
         then 'serial' number. Normally this keyword will navigate to the devices page and refresh the table,
         both of these can be skipped.

        Keyword Usage:
          Robot:
             Library  keywords/gui/manage/KeywordsDevices.py
             Select Device  ${ap1}    skip_refresh=True  skip_navigation=True

          Pytest:
             Imports:
                from keywords.gui.manage.KeywordsDevices import KeywordsDevices
             Calling Keyword:
                kwDevices = KeywordsDevices()
                kwDevices.select_device(self.tb.dut1, skip_refresh=True, skip_navigation=True)

        Keyword Implementations:
               GUI
               XAPI - ** Not Supported**

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1):
        :param skip_refresh: True - to skip the refresh of the devices page, default set to False
        :param skip_navigation: True - to skip the navigation to the devices page, default set to False
        :param kwargs: Supports all standard kwargs

        :return: return 1 if device found else -1
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("914177d7-df55-4070-b113-84602016871c", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        if 'serial' not in device_dict.keys() and 'mac' not in device_dict.keys():
            kwargs['fail_msg'] = "Invalid keyword arguments: ‘serial’ or ‘mac’ must be included in device_dict"

        # Assume a failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.devices.gui_select_device(device_dict, skip_refresh=skip_refresh,
                                                                 skip_navigation=skip_navigation, **kwargs)

                else:
                    return_code = self.keyword_utils.implementations.not_supported(**kwargs)
                    # not_supported() returns True if keyword should pass else returns False
                    if return_code:
                        return_code = 0
                    else:
                        return_code = -1
        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def delete_device(self, device_dict, **kwargs):
        """
        Deletes a device identified by 'serial' or 'mac' provided in device_dict

        In the devices page delete_device will delete a specific device by using 'mac' address first, then 'serial'
        number. If the device platform is a "stack" then delete_device will try to delete the device using 'mac' address
        of the stack, otherwise will delete individual devices by using every 'serial' number provided in
        device_dict.

        Keyword Usage:
          Robot:
             Library  keywords/gui/manage/KeywordsDevices.py
             Delete Device  ${ap1}

          Pytest:
             Imports:
                from keywords.gui.manage.KeywordsDevices import KeywordsDevices
             Calling Keyword:
                kwDevices = KeywordsDevices()
                kwDevices.delete_device(self.tb.dut1)

        Keyword Implementations:
               GUI
               XAPI

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1)
        :param kwargs: Supports all standard kwargs

        :return: 1 if device deleted successfully or is already deleted/does not exist, else -1
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("54bc6dfc-81c5-4dd7-a231-457253994817", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name)
        self.keyword_utils.implementations.xapi_implemented(keyword_name)

        # Getting data from the dictionary for XAPI
        device_serial = device_dict.get("serial")
        device_mac = device_dict.get("mac")

        if 'serial' not in device_dict.keys() and 'mac' not in device_dict.keys():
            kwargs['fail_msg'] = "Invalid keyword arguments: ‘serial’ or ‘mac’ must be included in device_dict"

        # Assume a failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.devices.gui_delete_device(device_dict, **kwargs)

                else:
                    return_code = self.xapiDevices.xapi_delete_device(device_serial=device_serial,
                                                                      device_mac=device_mac, **kwargs)

        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code

    def wait_until_device_removed(self, device_dict, retry_duration=10, retry_count=30, **kwargs):
        """
         Waits for the device to be removed from the devices page

         In the devices page, wait_until_device_removed will search for a specific device looking for 'mac' address
         first, then 'serial' number to check if the device still exists in the devices page, or it was removed. By
         default loops 10 times every 30 seconds to check if the device still exists in the table.

        Keyword Usage:
          Robot:
             Library  keywords/gui/manage/KeywordsDevices.py
             Wait Until Device Removed  ${ap1}    retry_duration=15    retry_count=20

          Pytest:
             Imports:
                from keywords.gui.manage.KeywordsDevices import KeywordsDevices
             Calling Keyword:
                kwDevices = KeywordsDevices()
                kwDevices.wait_until_device_removed(self.tb.dut1, retry_duration=15, retry_count=20)

        Keyword Implementations:
           GUI
           XAPI - ** Not Implemented **

        :param device_dict: dictionary from .yaml testbed file (ex: ap1, netelem1)
        :param retry_duration: duration between each retry, by default set to 10 (times)
        :param retry_count: retry count, by default set to 30 (seconds)

        :return: 1 if device removed within time; else -1
        """
        # Notes:
        #   - The work for this keyword is in a separate file
        #   - The amount of time this keyword takes will be recorded and optionally recorded in a database
        #   - This method will catch any errors that are raised and not handled in the keyword
        keyword_name = inspect.stack()[0][3]
        self.keyword_utils.implementations.set_keyword_uuid("31c2990b-c22f-4cd9-b9d4-139b2e28e6ca", keyword_name)
        self.keyword_utils.implementations.gui_implemented(keyword_name, prefer_gui=True)

        if 'serial' not in device_dict.keys() and 'mac' not in device_dict.keys():
            kwargs['fail_msg'] = "Invalid keyword arguments: ‘serial’ or ‘mac’ must be included in device_dict"

        # Assume a failure
        return_code = -1

        # Call the helper function that implements this keyword
        try:
            implementation_to_run = self.keyword_utils.implementations.select_keyword_implementation(keyword_name, **kwargs)
            if implementation_to_run != '':
                self.keyword_utils.timing.start(keyword_name, implementation_to_run)
                if implementation_to_run == "GUI":
                    return_code = self.devices.gui_wait_until_device_removed(device_dict, retry_duration=retry_duration,
                                                                             retry_count=retry_count, **kwargs)

                else:
                    kwargs['fail_msg'] = "XAPI version is not yet implemented for gui_wait_until_device_removed()."
                    self.common_validation.fault(**kwargs)
                    return -1

        except Exception as e:
            kwargs['fail_msg'] = f"Error raised for keyword [{keyword_name}] Error: {e}"
            self.common_validation.fault(**kwargs)
        finally:
            self.keyword_utils.timing.end(keyword_name)

        # Return the return value of the keyword
        return return_code
