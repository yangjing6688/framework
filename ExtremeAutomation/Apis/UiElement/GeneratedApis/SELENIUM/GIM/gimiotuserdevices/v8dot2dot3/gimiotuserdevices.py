from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as GimiotuserdevicesBase
# All imports above this line will be removed after generation.
# User imports must be added below.
import re
import datetime


class Gimiotuserdevices(GimiotuserdevicesBase):
    def dev_sel_ot_devices(self, ui_cmd_obj, arg_dict):
        self.navigate_devices(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@class ='x-btn x-unselectable x-box-item x-toolbar-item x-btn-"
                                       "default-toolbar-small'][1]")
        self.spinner_loading(ui_cmd_obj)
        self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['de_otname'],
                                                 "//input[@name='onboardingTemplate']",
                                                 self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.base_builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Save']", retry=5)

        return ui_cmd_obj

    def dev_add_mac_devices(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 2)
        arg_dict['device_mac'] = arg_dict['device_mac'].strip()
        self.builder.enter_text(ui_cmd_obj, arg_dict['device_mac'], "//input[@name='mac']")
        self.builder.delay(ui_cmd_obj, 1)
        self.builder.enter_text(ui_cmd_obj, arg_dict['device_name'], "//input[@name='deviceName']")
        self.builder.click(ui_cmd_obj, "//span[text()='Save']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def dev_select_device_type(self, ui_cmd_obj, arg_dict):
        self.navigate_devices(ui_cmd_obj, arg_dict)
        self.builder.click(ui_cmd_obj, "//a[@class ='x-btn x-unselectable x-box-item x-toolbar-item x-btn-"
                                       "default-toolbar-small'][1]")
        self.spinner_loading(ui_cmd_obj)
        self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['ot_name'],
                                                 "//input[@name='onboardingTemplate']",
                                                 self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)
        self.base_builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Save']", retry=5)
        self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['device_grp_name'],
                                                 "//input[@name='deviceFamilyGroup']",
                                                 self.builder.constants.STRATEGY_XPATH)
        self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['device_type_name'],
                                                 "//input[@name='deviceTypes']",
                                                 self.builder.constants.STRATEGY_XPATH)

        return ui_cmd_obj

    def dev_verify_device_added(self, ui_cmd_obj, arg_dict):
        self.navigate_devices(ui_cmd_obj, arg_dict)
        self.filtering_devices_based_on_mac(ui_cmd_obj, arg_dict)
        all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
        row_count = len(all_count)
        self.logger.log_info("row_count: " + str(row_count))
        if row_count <= 0:
            ui_cmd_obj.error_state = True
        for index in range(1, (row_count + 1)):
            web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                            "(" + str(index) + ") [role='gridcell']:nth-of-type(1)"
                                                                               " .x-grid-cell-inner",
                                                self.builder.constants.STRATEGY_CSS_SELECTOR)
            return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.logger.log_info("device_mac: " + str(index) + "::" + return_text)
            # device name
            if return_text == arg_dict['device_mac']:
                web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                "(" + str(index) + ") [role='gridcell']:nth-of-type(2)"
                                                                                   " .x-grid-cell-inner",
                                                    self.builder.constants.STRATEGY_CSS_SELECTOR)
                return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                self.logger.log_info("device_name: " + str(index) + "::" + return_text)
                self.builder.delay(ui_cmd_obj, 2)
                if return_text == " ":
                    self.logger.log_info(
                        "<" + arg_dict['device_name'] + "> device_name: is equal to None ::" + return_text)
                    ui_cmd_obj.error_state = False
                if return_text != " " and return_text != arg_dict['device_name']:
                    self.logger.log_info("<" + arg_dict['device_name'] + "> device_name: "
                                                                         "is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # device type group
                if return_text == arg_dict['device_name']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(3)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_type: " + str(index) + "::" + return_text)
                if return_text != arg_dict['device_type']:
                    self.logger.log_info("<" + arg_dict['device_type'] + "> device_type: is not "
                                                                         "equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # device type -sub type
                if return_text == arg_dict['device_type']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(4)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_subtype: " + str(index) + "::" + return_text)
                if return_text == " " and arg_dict['device_subtype'] == "NA":
                    self.logger.log_info("return text is empty and subtype is NA" + return_text +
                                         arg_dict['device_subtype'])
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['device_subtype']:
                    self.logger.log_info(
                        "<" + arg_dict['device_subtype'] + "> device_subtype: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # source
                if return_text == arg_dict['device_subtype']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(5)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_source: " + str(index) + "::" + return_text)
                if return_text != arg_dict['device_source']:
                    self.logger.log_info(
                        "<" + arg_dict['device_source'] + "> device_source: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # enabled
                if return_text == arg_dict['device_source']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(6)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_enabled: " + str(index) + "::" + return_text)
                if return_text != arg_dict['device_enabled']:
                    self.logger.log_info(
                        "<" + arg_dict['device_enabled'] + "> device_enabled: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # asset type
                if return_text == arg_dict['device_enabled']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(7)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_asset_type: " + str(index) + "::" + return_text)
                if return_text != arg_dict['device_asset_type']:
                    self.logger.log_info(
                        "<" + arg_dict[
                            'device_asset_type'] + "> device_asset_type: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                # onboarding template
                if return_text == arg_dict['device_asset_type']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(11)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_ot: " + str(index) + "::" + return_text)
                if return_text != arg_dict['device_ot']:
                    self.logger.log_info(
                        "<" + arg_dict['device_ot'] + "> device_ot: is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
                self.builder.move_cursor(ui_cmd_obj, "//div[@role='columnheader'][11]",
                                         self.builder.constants.STRATEGY_XPATH)
                self.builder.delay(ui_cmd_obj, 5)
                # provisioner name
                if return_text == arg_dict['device_ot']:
                    web_obj = self.builder.find_element(ui_cmd_obj, ".x-grid-item:nth-of-type"
                                                                    "(" + str(index) +
                                                                    ") [role='gridcell']:nth-of-type(12)"
                                                                    " .x-grid-cell-inner",
                                                        self.builder.constants.STRATEGY_CSS_SELECTOR)
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("device_prv: " + str(index) + "::" + return_text)
                if return_text == arg_dict['device_prv']:
                    ui_cmd_obj.error_state = False
                    break
                elif return_text != arg_dict['device_prv']:
                    self.logger.log_info("<" + arg_dict['device_prv'] + "> device_prv:is not equal to ::" + return_text)
                    ui_cmd_obj.error_state = True
                    break
            elif return_text == '':
                ui_cmd_obj.error_state = True
                break
            else:
                self.logger.log_info("<" + arg_dict['device_mac'] + "> device_mac: is not equal to ::" + return_text)
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def dev_navigate_device_types(self, ui_cmd_obj, arg_dict):
        self.builder.click(ui_cmd_obj, "//span[text()='Device Type Groups']", self.builder.constants.STRATEGY_XPATH)
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def dev_verify_default_selected_device_types(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//span[text()='Summary']")
        self.spinner_loading(ui_cmd_obj)
        web_element = self.builder.find_element(ui_cmd_obj, "//fieldset[@aria-label='Device Type Groups field set']",
                                                self.builder.constants.STRATEGY_XPATH)
        web_ele_data = self.base_builder.get_text_from_element(ui_cmd_obj, web_element)
        new_arr = web_ele_data.split("\n")
        self.logger.log_info("Length of device type and subtype " + str(len(new_arr)))
        self.logger.log_info("Summary of device type and subtype " + str(new_arr))
        self.logger.log_info("new_arr[0] " + new_arr[0])
        if new_arr[0] != "Device Type Groups":
            ui_cmd_obj.error_state = True
        self.logger.log_info("new_arr[1] " + new_arr[1])
        if new_arr[1] != arg_dict['device_type_name']:
            ui_cmd_obj.error_state = True
        self.logger.log_info("new_arr[2] " + new_arr[2])
        if len(new_arr) > 3:
            ui_cmd_obj.error_state = True
        else:
            ui_cmd_obj.error_state = False

        return ui_cmd_obj

    def dev_create_device_using_self_provisioner(self, ui_cmd_obj, arg_dict):
        try:
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "//input[@name='macAddress']", self.builder.constants.STRATEGY_XPATH)
            self.spinner_loading(ui_cmd_obj)
            mac_array = arg_dict['de_mac'].split(":")
            for x in mac_array:
                self.builder.enter_text(ui_cmd_obj, str(x), "//input[@name='macAddress']", clear_existing=False)
            self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['device_grp_name'],
                                                     "//input[@name='deviceFamily']",
                                                     self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 2)
            self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['device_type_name'],
                                                     "//input[@name='deviceType']",
                                                     self.builder.constants.STRATEGY_XPATH)
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "//span[text()='Submit']")
            self.spinner_loading(ui_cmd_obj)
            if self.builder.find_element(ui_cmd_obj, "//div[text()='Success']"):
                self.builder.click(ui_cmd_obj, "//span[text()='OK']")
                self.builder.delay(ui_cmd_obj, arg_dict)
        except TypeError:
            return ui_cmd_obj

        return ui_cmd_obj

    def dev_de_select_device_type(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "// span[text() = 'Device Type Groups']", self.builder.constants.STRATEGY_XPATH)
        self.base_builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//div[text()='Available Device Type Groups']",
                           self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//label[text()='Select All']", self.builder.constants.STRATEGY_XPATH)
        self.base_builder.delay(ui_cmd_obj, 1000)
        self.builder.click(ui_cmd_obj, "//label[text()='Select All']", self.builder.constants.STRATEGY_XPATH)
        i = 0
        if arg_dict["device_type_name"] == 'Android':
            i = 1
        elif arg_dict["device_type_name"] == 'Apple iOS':
            i = 2
        elif arg_dict["device_type_name"] == 'BlackBerry':
            i = 3
        elif arg_dict["device_type_name"] == 'Chrome OS':
            i = 4
        elif arg_dict["device_type_name"] == 'Game Console':
            i = 5
        elif arg_dict["device_type_name"] == 'Linux':
            i = 6
        elif arg_dict["device_type_name"] == 'Mac':
            i = 7
        elif arg_dict["device_type_name"] == 'Windows':
            i = 8
        elif arg_dict["device_type_name"] == 'Windows Mobile':
            i = 9
        web_element_device_name = self.builder.find_element(ui_cmd_obj,
                                                            "//div[@role='treegrid']/div[@role='presentation']/"
                                                            "table[" + str(i) + "]//span[text()=" + "'" +
                                                            arg_dict["device_type_name"] + "'" + "]")
        if web_element_device_name.text == "Android" or "Apple iOS" or "BlackBerry" or "Chrome OS" or \
                "Game Console" or "Linux" or "Mac" or "Windows" or "Windows Mobile":
            self.builder.click(ui_cmd_obj, "//div[@role='treegrid']/div[@role='presentation']"
                                           "/table[" + str(i) + "]//div[@role='button']")
            self.base_builder.delay(ui_cmd_obj, 2000)

        return ui_cmd_obj

    def dev_verify_only_selected_device_type_in_drop_down(self, ui_cmd_obj, arg_dict):
        self.builder.delay(ui_cmd_obj, 2)
        self.builder.click(ui_cmd_obj, "//input[@name='deviceFamily']",
                           self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 2)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@role='option']")
        if len(items) == 1 and items[0].text == arg_dict["device_type_name"]:
            self.logger.log_info("Only one item is present in drop down: " + arg_dict['device_type_name'])
            ui_cmd_obj.error_state = False
        else:
            ui_cmd_obj.error_state = True
        for item in items:
            self.logger.log_info("element name " + item.text)
            if arg_dict["device_type_name"] in item.text:
                item.click()
                break
        self.logger.log_info("from summary arg[]: " + arg_dict['summary'])
        exp_text = arg_dict['summary']
        exp_split = exp_text.split(",")
        self.builder.click(ui_cmd_obj, "//input[@name='deviceType']")
        self.builder.delay(ui_cmd_obj, 5)
        web_obj = self.builder.find_elements(ui_cmd_obj, "(//ul[@role='listbox'])[2]/li[@role='option']")
        self.logger.log_info("actual_device_type length "
                             "<" + str(len(web_obj)) + "> expected_device_type_length "
                                                       "<" + str(len(exp_split)) + ">")
        if len(exp_split) != len(web_obj):
            ui_cmd_obj.error_state = True
        length = len(exp_split)
        for i in range(length):
            web_text = web_obj[i].text
            act_text = web_text.strip()
            exp_text = exp_split[i].strip()
            self.logger.log_info("actual_device_type <" + act_text + "> expected_device_type <" + exp_text + ">")
            if act_text != exp_text:
                self.logger.log_info("actual_device_type <" + act_text + "> is not equal to expected_device_type "
                                                                         "<" + exp_text + ">")
                ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def dev_create_dev_validate_acc_validity(self, ui_cmd_obj, arg_dict):
        self.dev_sel_ot_devices(ui_cmd_obj, arg_dict)
        if arg_dict['change_nochan'] == "change":
            list_duration = re.findall('[0-9]+', arg_dict['change_time'])
            list_durationunit = re.findall('[a-z]+', arg_dict['change_time'])
            self.logger.log_info("LIST_DURATION_UNIT[0]:" + str(list_durationunit[0]))
            self.builder.delay(ui_cmd_obj, 5)
            web_element = self.builder.find_element(ui_cmd_obj, "//input[@name='durationUnits']")
            self.builder.delay(ui_cmd_obj, 5)
            self.base_builder.click(ui_cmd_obj, web_element)
            web_items = self.builder.find_elements(ui_cmd_obj, "(//ul[@role='listbox'])[2]/li[@role='option']")
            for item in web_items:
                if item.get_attribute("innerText") == list_durationunit[0]:
                    self.base_builder.click(ui_cmd_obj, item)
                    self.builder.delay(ui_cmd_obj, 5)
                    break
            web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='duration']",
                                                self.builder.constants.STRATEGY_XPATH)
            timestamp = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "value")
            # timestamp = web_obj.get_attribute("value")
            if timestamp != str(list_duration[0]):
                self.builder.delay(ui_cmd_obj, 5)
                self.builder.enter_text(ui_cmd_obj, list_duration[0], "//input[@name='duration']",
                                        self.builder.constants.STRATEGY_XPATH, clear_existing=True)
        self.builder.enter_text(ui_cmd_obj, arg_dict['device_mac'], "//input[@name='mac']")
        self.builder.enter_text(ui_cmd_obj, arg_dict['de_name'], "//input[@name='deviceName']")
        self.builder.click(ui_cmd_obj, "//input[@name='deviceFamilyGroup']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[1]", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//input[@name='deviceTypes']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[2]", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//span[text()='Save']", self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 5000)
        if arg_dict['error_no_error'] == "error":
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[text()='Error']",
                                                self.builder.constants.STRATEGY_XPATH)
            web_obj_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
            self.builder.click(ui_cmd_obj, "(//span[text()='Cancel'])[1]")
            if web_obj_text != "Error":
                ui_cmd_obj.error_state = True
        else:
            self.filtering_devices_based_on_mac(ui_cmd_obj, arg_dict)
            all_count = self.builder.find_elements(ui_cmd_obj, "//div[@class ='x-grid-item-container']/table")
            row_count = len(all_count)
            if row_count == 0:
                ui_cmd_obj.error_state = True
            else:
                for index in range(1, (row_count + 1)):
                    web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                    "/table[" + str(index) + "]/tbody/tr/td[1]")
                    return_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj)
                    self.logger.log_info("Device_MAC: " + str(index) + "::" + return_text)
                    if return_text == arg_dict['device_mac']:
                        ui_cmd_obj.error_state = False
                        self.logger.log_info("<" + arg_dict['device_mac'] + "> device_mac: exists ::" + return_text)
                        start_time_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                               "/table[" + str(index) +
                                                                               "]/tbody/tr/td[9]")
                        start_time = start_time_obj.get_attribute('innerText')
                        end_time_obj = self.builder.find_element(ui_cmd_obj, "//div[@class ='x-grid-item-container']"
                                                                             "/table[" + str(index) +
                                                                             "]/tbody/tr/td[10]")
                        end_time = end_time_obj.get_attribute('innerText')
                        date_time_format = '%Y/%m/%d %I:%M:%S %p %Z'
                        diff = datetime.datetime.strptime(end_time, date_time_format) - \
                            datetime.datetime.strptime(start_time, date_time_format)
                        self.logger.log_info("Difference:" + str(diff))
                        self.logger.log_info("Days:" + str(diff.days))
                        self.logger.log_info("Seconds:" + str(float(diff.total_seconds())))
                        if arg_dict['change_nochan'] == "change":
                            if "days" in arg_dict["change_time"]:
                                time_d = int(arg_dict['change_time'].strip("days"))
                                total_time = time_d * 60 * 60 * 24
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "hours" in arg_dict["change_time"]:
                                time_d = int(arg_dict['change_time'].strip("hours"))
                                total_time = time_d * 60 * 60
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "minutes" in arg_dict["change_time"]:
                                time_d = (arg_dict['change_time']).strip("minutes")
                                self.logger.log_info("TIme:" + str(time_d))
                                time_d = int(time_d)
                                total_time = time_d * 60
                                self.logger.log_info("total time in sec:" + str(total_time))
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                        else:
                            if "days" in arg_dict["time"]:
                                time_d = int(arg_dict['time'].strip("days"))
                                total_time = time_d * 60 * 60 * 24
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "hrs" in arg_dict["time"]:
                                time_d = int(arg_dict['time'].strip("hrs"))
                                total_time = time_d * 60 * 60
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                            elif "min" in arg_dict["time"]:
                                time_d = int(arg_dict['time'].strip("min"))
                                total_time = time_d * 60
                                self.logger.log_info("total time in sec:" + str(total_time))
                                if diff.total_seconds() != total_time:
                                    ui_cmd_obj.error_state = True
                        break
                    elif return_text == '':
                        ui_cmd_obj.error_state = True
                        break
                    else:
                        self.logger.log_info("<" + arg_dict['de_mac'] + "> de_mac: does not exists ::" + return_text)
                        ui_cmd_obj.error_state = True

        return ui_cmd_obj

    def dev_locale_register_devices(self, ui_cmd_obj, arg_dict):
        try:
            # locale click
            self.base_builder.delay(ui_cmd_obj, 2000)
            self.builder.click(ui_cmd_obj, "//span[text()='" + arg_dict['locale_name'] + "']")
            self.base_builder.delay(ui_cmd_obj, 2000)
            # with authenticator
            if arg_dict['with_authenticator'] == "yes_with_authenticator":
                self.builder.enter_text(ui_cmd_obj, arg_dict['prv_un'], "//input[@name='deviceUsername']")
                self.builder.enter_text(ui_cmd_obj, arg_dict['prv_pwd'], "//input[@name='deviceUserPassword']")
            # without authenticator
            self.builder.delay(ui_cmd_obj, 2)
            self.builder.click(ui_cmd_obj, "//input[@name='macAddress']", self.builder.constants.STRATEGY_XPATH)
            mac_array = arg_dict['dev_mac'].split(":")
            for x in mac_array:
                self.builder.enter_text(ui_cmd_obj, str(x), "//input[@name='macAddress']", clear_existing=False)
            self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['device_grp_name'],
                                                     "//input[@name='deviceFamily']",
                                                     self.builder.constants.STRATEGY_XPATH)
            self.select_dev_type_from_drop_self_prov(ui_cmd_obj, arg_dict['device_type_name'],
                                                     "//input[@name='deviceType']",
                                                     self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "//div[@class='x-box-scroller x-box-scroller-left x-box-scroller-toolbar "
                                           "x-box-scroller-toolbar-footer x-unselectable']/following::div/div/a[1]")
            self.base_builder.delay(ui_cmd_obj, 2000)
            if arg_dict['click_ok'] == "yes_click_ok":
                self.builder.click(ui_cmd_obj, "//div[@class='x-window-bodyWrap']/div[2]/div/div/a[1]")
                self.logger.log_info("try: clicked on OK button: ")
            self.builder.delay(ui_cmd_obj, 2)
            return ui_cmd_obj
        except TypeError:
            return ui_cmd_obj

    def dev_locale_error_success_validation(self, ui_cmd_obj, arg_dict):
        self.base_builder.delay(ui_cmd_obj, 2000)
        # locale click
        if arg_dict['locale_selection'] == "yes_locale_selection":
            web_obj = self.builder.find_elements(ui_cmd_obj, "//a[@class='x-btn x-unselectable x-box-item "
                                                             "x-toolbar-item x-btn-default-toolbar-small']")
            locale_count = len(web_obj)
            self.logger.log_info("locale_count: " + str(locale_count))
            for index in range(1, (locale_count + 1)):
                web_locale = self.builder.find_element(ui_cmd_obj, "#top-locales-toolbar [hidefocus='on']:nth-of-"
                                                                   "type(" + str(index) + ") .x-btn-inner-default-"
                                                                                          "toolbar-small",
                                                       self.builder.constants.STRATEGY_CSS_SELECTOR)
                locale_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_locale)
                self.logger.log_info("locale_text: " + locale_text)
                if locale_text == arg_dict['locale_name']:
                    self.base_builder.click(ui_cmd_obj, web_locale)
                    self.logger.log_info("clicked on selected locale: " + arg_dict['locale_name'])
                    self.base_builder.delay(ui_cmd_obj, 2000)
        if arg_dict['submit'] == "yes_submit":
            self.builder.click(ui_cmd_obj, "//div[@class='x-box-scroller x-box-scroller-left x-box-scroller-toolbar "
                                           "x-box-scroller-toolbar-footer x-unselectable']/following::div/div/a[1]")
            self.base_builder.delay(ui_cmd_obj, 2000)
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@role='alertdialog']/div[1]")
        web_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj).strip()
        self.logger.log_info("error text: " + web_text)
        if web_text != arg_dict['title_error'].strip():
            self.logger.log_info("title_error: " + web_text + "is not equal to" + arg_dict['title_error'])
            ui_cmd_obj.error_state = True
        if arg_dict['body_text'] == "yes_body_text":
            web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-window-bodyWrap']/div[1]")
            web_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj).strip()
            self.logger.log_info("body text alert window: " + web_text)
            if web_text != arg_dict['body_text_content'].strip():
                self.logger.log_info("body_text_content: " + web_text + "is not "
                                                                        "equal to " + arg_dict['error2'].strip())
                ui_cmd_obj.error_state = True
        web_obj = self.builder.find_element(ui_cmd_obj, "//div[@class='x-window-bodyWrap']/div[2]")
        web_text = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj).strip()
        self.logger.log_info("OK button: " + web_text)
        if web_text != arg_dict['ok_button'].strip():
            self.logger.log_info("ok_button: " + web_text + "is not equal to " + arg_dict['ok_button'].strip())
            ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//div[@class='x-window-bodyWrap']/div[2]/div/div/a[1]")
        self.builder.delay(ui_cmd_obj, 2)

        return ui_cmd_obj

    def dev_create_accessible_to_prov_options(self, ui_cmd_obj, arg_dict):
        self.dev_sel_ot_devices(ui_cmd_obj, arg_dict)
        if arg_dict['error_or_no'] == "no_error":
            self.builder.enter_text(ui_cmd_obj, arg_dict['de_mac'], "//input[@name='mac']")
        if arg_dict['name_yes_or_no'] == "name_yes":
            self.builder.enter_text(ui_cmd_obj, arg_dict['de_name'], "//input[@name='deviceName']")
        if "yes" in arg_dict['dtg_option']:
            self.builder.click(ui_cmd_obj, "//input[@name='deviceFamilyGroup']", self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[1]", self.builder.constants.STRATEGY_XPATH)
        if "yes" in arg_dict['dt_option']:
            self.builder.click(ui_cmd_obj, "//input[@name='deviceTypes']", self.builder.constants.STRATEGY_XPATH)
            self.builder.click(ui_cmd_obj, "(//li[text()='Android'])[2]", self.builder.constants.STRATEGY_XPATH)
        if arg_dict['asset'] == "asset_yes":
            asset_obj = self.builder.find_element(ui_cmd_obj, "//span[contains(text(),'Asset Type') and "
                                                              "@class='x-form-item-label-text']")
            asset_txt = self.base_builder.get_attribute_from_element(ui_cmd_obj, asset_obj, "innerText")
            if asset_txt != "Asset Type *:":
                ui_cmd_obj.error_state = True
            if arg_dict['asset_change'] == "asset_change_yes":
                self.builder.click(ui_cmd_obj,
                                   "[role] [role='presentation']:nth-child(12) .x-form-trigger-wrap-default"
                                   " [role='presentation']:nth-of-type(2)",
                                   self.builder.constants.STRATEGY_CSS_SELECTOR)
                self.builder.delay(ui_cmd_obj, 2)
                self.builder.click(ui_cmd_obj, "//li[text()='" + arg_dict['asset_change_type'] + "']")
            if arg_dict['doe_enable_disable'] == "doe_enable":
                self.builder.delay(ui_cmd_obj, 5)
                web_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='deleteOnExpire']")
                web_obj_doe_status = self.base_builder.is_element_selected(ui_cmd_obj, web_obj)

                if arg_dict['doe_option'] == "doe":
                    if str(web_obj_doe_status) != "True":
                        ui_cmd_obj.error_state = True
                if arg_dict['doe_option'] == "do_not_doe":
                    self.logger.log_info("Into DOE block")
                    if str(web_obj_doe_status) != "False":
                        ui_cmd_obj.error_state = True
            asset_type_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='assetType']")
            asset_type = self.base_builder.get_attribute_from_element(ui_cmd_obj, asset_type_obj, "value")
            self.logger.log_info("Asset_type:" + asset_type)
            if asset_type == "Temporary":
                self.logger.log_info("into the temporary Block")
                if arg_dict['account_activation_type'] == "firstlogin":
                    self.logger.log_info("Into the FirstLogin Block")
                    firstlogin_obj = self.builder.find_element(ui_cmd_obj,
                                                               "//div[@class='x-field x-form-item "
                                                               "x-form-item-default x-form-readonly x-form-type-text"
                                                               " x-box-item x-field-default x-vbox-form-item']",
                                                               self.builder.constants.STRATEGY_XPATH)
                    firstlogin_txt = self.base_builder.get_attribute_from_element(ui_cmd_obj, firstlogin_obj,
                                                                                  "textContent")
                    self.logger.log_info("firstlogin_txt:" + firstlogin_txt)
                    if firstlogin_txt != "Activate on First Login:Yes":
                        ui_cmd_obj.error_state = True
                elif arg_dict['account_activation_type'] == "timebased":
                    self.logger.log_info("into the timebased Block")
                    timebased_obj = self.builder.find_element(ui_cmd_obj,
                                                              "//div[@class='x-field x-form-field-date x-form-item "
                                                              "x-form-item-default x-form-type-text x-box-item "
                                                              "x-field-default x-hbox-form-item x-form-dirty']",
                                                              self.builder.constants.STRATEGY_XPATH)
                    timebased_txt = self.base_builder.get_attribute_from_element(ui_cmd_obj, timebased_obj,
                                                                                 "textContent")
                    self.logger.log_info("TimeBased_txt:" + timebased_txt)
                    if timebased_txt != "Activate Account On  *:Expected date format Y/m/d.":
                        ui_cmd_obj.error_state = True
                if arg_dict['acc_exp'] == "acc_exp_yes":
                    self.logger.log_info("into the acc exp yes block")
                    acc_exp_obj = self.builder.find_element(ui_cmd_obj,
                                                            "//div[@class='x-field x-form-item x-form-item-default "
                                                            "x-form-type-text x-box-item x-field-default "
                                                            "x-hbox-form-item x-form-dirty']")
                    acc_exp_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, acc_exp_obj, "textContent")
                    self.logger.log_info("acc_exp_text:" + acc_exp_text)
                    if acc_exp_text != "Duration  *:":
                        ui_cmd_obj.error_state = True
        if arg_dict['source_yes_or_no'] == "source_yes":
            src_obj = self.builder.find_element(ui_cmd_obj, "//input[@name='source']")
            src_txt = self.base_builder.get_attribute_from_element(ui_cmd_obj, src_obj, "value")
            if arg_dict['source_option'] == "auto":
                if src_txt != "GIM-" + arg_dict['de_otname'] + "":
                    ui_cmd_obj.error_state = True
            elif arg_dict['source_option'] == "static":
                if src_txt != "" + arg_dict['static_source_value'] + "":
                    ui_cmd_obj.error_state = True
            if arg_dict['change_source'] == "change_yes":
                self.builder.enter_text(ui_cmd_obj, arg_dict['source_changed_name'], "//input[@name='source']")
        if arg_dict['admin_comment'] == "admin_comment_yes":
            web_obj = self.builder.find_element(ui_cmd_obj, "//label[@class='x-component x-component-default' "
                                                            "and @style='font-weight:bold;']")
            web_text = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "innerText")
            if web_text != "Admin's Comment":
                ui_cmd_obj.error_state = True
            web_obj1 = self.builder.find_element(ui_cmd_obj, "//textarea")
            web_text1 = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj1, "value")
            if web_text1 != "" + arg_dict['admin_comment_value'] + "":
                self.logger.log_info("into the if block")
                ui_cmd_obj.error_state = True
        self.builder.click(ui_cmd_obj, "//span[text()='Save']", self.builder.constants.STRATEGY_XPATH)
        self.builder.delay(ui_cmd_obj, 2000)
        if arg_dict['device_limit'] == "limit_reached":
            self.builder.delay(ui_cmd_obj, 5)
            web_obj1 = self.builder.find_element(ui_cmd_obj, "//div[text()='Enabled Device Limit']",
                                                 self.builder.constants.STRATEGY_XPATH)
            web_text1 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj1)
            web_obj2 = self.builder.find_element(ui_cmd_obj, ".x-window-text",
                                                 self.builder.constants.STRATEGY_CSS_SELECTOR)
            web_text2 = self.base_builder.get_text_from_element(ui_cmd_obj, web_obj2)
            if web_text1 != "Enabled Device Limit":
                ui_cmd_obj.error_state = True
            if "Limit on Number of enabled devices has been reached." not in web_text2:
                ui_cmd_obj.error_state = True
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
        if arg_dict['error_or_no'] == "error":
            web_obj = self.builder.find_element(ui_cmd_obj,
                                                "(//div[@class='x-title x-window-header-title "
                                                "x-window-header-title-default x-box-item x-title-default "
                                                "x-title-rotate-none x-title-align-left'])[2]")
            web_txt = self.base_builder.get_attribute_from_element(ui_cmd_obj, web_obj, "textContent")
            if web_txt != "Error":
                ui_cmd_obj.error_state = True
            self.builder.click(ui_cmd_obj, "//span[text()='OK']")
            self.builder.click(ui_cmd_obj, "(//span[@class='x-btn-inner x-btn-inner-default-small' "
                                           "and text()='Cancel'])[1]")

        return ui_cmd_obj

    def spinner_loading(self, ui_cmd_obj):
        self.builder.webdriver_wait_until(ui_cmd_obj, ".x-mask-msg-text", retry=5,
                                          strategy=self.builder.constants.STRATEGY_CSS_SELECTOR,
                                          condition=self.builder.constants.CONDITION_INVISIBILITY_OF_ELEMENT)
        return ui_cmd_obj

    def wait_for_page_load_completely(self, ui_cmd_obj):
        self.logger.log_info("waiting for the page to load ...")
        for x in range(1, 25):
            self.base_builder.delay(ui_cmd_obj, 1000)
            self.base_builder.execute_script(ui_cmd_obj, "return document.readyState;")
            self.logger.log_info("page readyState:  " + str(ui_cmd_obj.return_data))
            if ui_cmd_obj.return_data == "complete":
                self.logger.log_info("page loaded completely: ")
                break

        return ui_cmd_obj

    def navigate_devices(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-"
                                                      "button-small' and text()='Devices']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[@class='x-btn-inner x-btn-inner-extr-nav-toolbar-button-small' "
                                       "and text()='Devices']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//a[@role='tab']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def filtering_devices_based_on_mac(self, ui_cmd_obj, arg_dict):
        self.builder.webdriver_wait_until(ui_cmd_obj, "//span[text()='Show Filter']", retry=5)
        self.builder.click(ui_cmd_obj, "//span[text()='Show Filter']")
        self.spinner_loading(ui_cmd_obj)
        self.builder.click(ui_cmd_obj, "//label[contains(text(),'Specify Filter')]",
                           self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//input[@name='primaryFilterValue']")
        self.builder.click(ui_cmd_obj, "//li[text()='MAC Address']", self.builder.constants.STRATEGY_XPATH)
        self.builder.click(ui_cmd_obj, "//input[@name='comparisionValue']")
        self.builder.click(ui_cmd_obj, "//li[text()='Equals']", self.builder.constants.STRATEGY_XPATH)
        self.builder.enter_text(ui_cmd_obj, arg_dict['device_mac'], "//input[@name='textValue']")
        self.builder.click(ui_cmd_obj, "//span[text()='Apply Filter']")
        self.spinner_loading(ui_cmd_obj)

        return ui_cmd_obj

    def select_dev_type_from_drop_self_prov(self, ui_cmd_obj, expected_list_option, element_locator, strategy):
        self.builder.click(ui_cmd_obj, element_locator, strategy)
        self.base_builder.delay(ui_cmd_obj, 1000)
        items = self.builder.find_elements(ui_cmd_obj, "//li[@role='option']")
        for item in items:
            self.logger.log_info("element name " + item.text)
            if expected_list_option in item.text:
                self.base_builder.click(ui_cmd_obj, item)
                break

        return ui_cmd_obj
