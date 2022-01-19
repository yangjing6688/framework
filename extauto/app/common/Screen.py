import time
from PIL import Image
import extauto.common.CloudDriver
from robot.libraries.BuiltIn import BuiltIn


class Screen:
    def __init__(self):
        self.driver = extauto.common.CloudDriver.cloud_driver

    def save_screen_shot(self, _driver=None):
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        file_name = str(int(time.time())) + ".png"
        file_path = output_folder + "/" + file_name
        if _driver:
            _driver.get_screenshot_as_file(file_path)
        else:
            self.driver.get_screenshot_as_file(file_path)
        print(
            "*HTML* <a href=" + file_name + "> <img src=" + file_name + " width=\"600px\" style=\"border:5px solid red\"></a>")
        return file_name

    def save_element_screen_shot64(self):
        self.driver.get_screenshot_as_file()

    def save_element_screen_shot(self, element):
        location = element.location
        size = element.size
        self.driver.save_screenshot('tmp.png')
        # Uses PIL library to open image in memory
        im = Image.open('tmp.png')
        left = int(location['x'])
        top = int(location['y'])
        right = int(location['x']) + int(size['width'])
        bottom = int(location['y']) + int(size['height'])
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
