import time
from PIL import Image

import common.CloudDriver
from extauto.common.Utils import Utils
from robot.libraries.BuiltIn import BuiltIn
try:
    import allure
    from allure_commons.types import AttachmentType
except:
    pass


class Screen:
    def __init__(self):
        self.utils = Utils()
        self.driver = common.CloudDriver.cloud_driver

    def add_screen_shot_to_allure(self, file_name, driver):
        try:
            allure.attach(driver.get_screenshot_as_png(), name=file_name, attachment_type=AttachmentType.PNG)
        except:
            pass

    def save_screen_shot(self, _driver=None):
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        file_name = str(int(time.time())) + ".png"
        file_path = output_folder + "/" + file_name
        if _driver:
            _driver.get_screenshot_as_file(file_path)
            self.add_screen_shot_to_allure(file_name, _driver)
        else:
            self.driver.get_screenshot_as_file(file_path)
            self.add_screen_shot_to_allure(file_name, self.driver)
        print(
            "*HTML* <a href=" + file_name + "> <img src=" + file_name + " width=\"600px\" style=\"border:5px solid red\"></a>")
        return file_name

    def save_element_screen_shot64(self):
        self.driver.get_screenshot_as_file()

    def save_element_screen_shot(self, element):
        location = element.location
        size = element.size

        self.utils.print_info("Element Image Size: ", size)
        self.utils.print_info("Element Image Location: ", location)

        self.driver.save_screenshot('tmp.png')
        # Uses PIL library to open image in memory
        im = Image.open('tmp.png')
        left = int(location['x'])
        top = int(location['y'])
        right = int(location['x']) + int(size['width'])
        bottom = int(location['y']) + int(size['height'])

        self.utils.print_info("Element Image Left: ", left)
        self.utils.print_info("Element Image Right: ", right)
        self.utils.print_info("Element Image Top: ", top)
        self.utils.print_info("Element Image Bottom: ", bottom)


        # Defines crop points
        im = im.crop((left, top, right, bottom))
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        file_name = str(int(time.time())) + ".png"
        file_path = output_folder + "/" + file_name
        im.save(file_path)
        print ("*HTML* <a href=" + file_name + "> <img src=" + file_name + " width=\"600px\"></a>")
        time.sleep(5)
        return file_name

    def take_screen_shot(self,  _driver=None):
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        file_name = str(int(time.time())) + ".png"
        file_path = output_folder + "/" + file_name

        if _driver is None:
            _driver = self.driver

        _driver.get_screenshot_as_file(file_path)
        time.sleep(5)
        return file_name
