import time
import shlex
import subprocess
import common.CloudDriver
from extauto.common.Utils import Utils
from extauto.common.Screen import Screen
from robot.libraries.BuiltIn import BuiltIn


class ScreenDiff:
    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()
        self.driver = common.CloudDriver.cloud_driver

    def compare_screens(self, input_image, scale=False, threshold='default'):
        """
        :param input_image: Input image to compare
        :param threshold: Threshold limit for comparison
        :param scale: scales the images
        :return: appends the images and diff in robot result log file
        """
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")

        on_run = self.screen.take_screen_shot(self.driver)
        time.sleep(5)

        self.utils.print_info("COMMAND: cp ../screens/" + input_image + " " + output_folder)
        copy_expected = shlex.split("cp ../screens/" + input_image + " " + output_folder)

        self.utils.print_info("Copying the Expected Screen Shot to Results Folder")
        subprocess.Popen(copy_expected, stdout=subprocess.PIPE)
        time.sleep(5)

        # self.utils.print_info("Making PDIFF Executable")
        # command_execute = "chmod 777 ../tools/pdiff/perceptualdiff"
        # args2 = shlex.split(command_execute)
        # subprocess.Popen(args2, stdout=subprocess.PIPE)

        # time.sleep(5)

        self.utils.print_info("Executing the PDIFF")
        if threshold == 'default':
            threshold = 100

        result_file_name = str(int(time.time())) + ".png"

        input_img = input_image

        if scale:
            command_line = "perceptualdiff -threshold " + str(threshold) + " -verbose -scale " + \
                       input_image + " " + output_folder + "/" + on_run + " -output " + result_file_name
        else:
            command_line = "perceptualdiff -threshold " + str(threshold) + " -verbose " + \
                           input_image + " " + output_folder + "/" + on_run + " -output " + result_file_name

        self.utils.print_info("PDiff Command: ", command_line)

        args = shlex.split(command_line)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = p.stdout.read()
        self.utils.print_info("P Diff Result: ", result)
        time.sleep(5)

        self.utils.look_and_feel(input_img, on_run, result_file_name)

        """ Copy the Result PNG To Results Folder """
        # copy_expected = shlex.split("cp result.png" + " " + output_folder)

        time.sleep(5)
        if b'Images are binary identical' in result:
            self.utils.print_info("Both screens are IDENTICAL")
            # print("Executing : cp ../screens/" + input_image + " " + output_folder)
            # copy_expected = shlex.split("cp ../screens/" + input_image + " " + output_folder + "/result.png")
            return 1
        # subprocess.Popen(copy_expected, stdout=subprocess.PIPE)

        if b'Images are visibly different' in result:
            self.utils.print_info("Both screens are DIFFERENT")
            # print("Executing : cp ../screens/" + input_image + " " + output_folder)
            # copy_expected = shlex.split("cp ../screens/" + input_image + " " + output_folder + "/result.png")
            return -1

        if b'Images are perceptually indistinguishable' in result:
            self.utils.print_info("Both screens are DIFFERENT - But within the THRESHOLD")
            return 1
            # subprocess.Popen(copy_expected, stdout=subprocess.PIPE)

    def compare_images(self, input_image1, input_image2, threshold='default'):
        """
        :param input_image:
        :param threshold:
        :return:
        """
        output_folder = BuiltIn().get_variable_value("${OUTPUT DIR}")
        self.utils.print_info("Compare Images Output Folder: ", output_folder)

        #on_run = self.screen.take_screen_shot(self.driver)
        #time.sleep(5)

        self.utils.print_info("COMMAND: cp ../screens/" + input_image1 + " " + output_folder)
        self.utils.print_info("COMMAND: cp ../screens/" + input_image2 + " " + output_folder)
        copy_expected1 = shlex.split("cp ../screens/" + input_image1 + " " + output_folder)
        copy_expected2 = shlex.split("cp ../screens/" + input_image2 + " " + output_folder)
        time.sleep(5)

        self.utils.print_info("Copying the Expected Screen Shot to Results Folder")
        subprocess.Popen(copy_expected1, stdout=subprocess.PIPE)
        time.sleep(5)
        subprocess.Popen(copy_expected2, stdout=subprocess.PIPE)
        time.sleep(5)

        # self.utils.print_info("Making PDIFF Executable")
        # command_execute = "chmod 777 ../tools/pdiff/perceptualdiff"
        # args2 = shlex.split(command_execute)
        # subprocess.Popen(args2, stdout=subprocess.PIPE)

        # time.sleep(5)

        self.utils.print_info("Executing the PDIFF")
        if threshold == 'default':
            threshold = 100

        result_file_name = str(int(time.time())) + ".png"

        #input_img = input_image

        command_line = "perceptualdiff -threshold " + str(threshold) + " -verbose -scale " + \
                       input_image1 + " " + output_folder + "/" + input_image2 + " -output " + result_file_name

        self.utils.print_info("PDiff Command: ", command_line)

        args = shlex.split(command_line)
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        result = p.stdout.read()
        self.utils.print_info("P Diff Result: ", result)
        time.sleep(5)

        self.utils.look_and_feel(input_image1, input_image2, result_file_name)

        """ Copy the Result PNG To Results Folder """
        # copy_expected = shlex.split("cp result.png" + " " + output_folder)

        time.sleep(5)
        if b'Images are binary identical' in result:
            self.utils.print_info("Both screens are identical")
            # print("Executing : cp ../screens/" + input_image + " " + output_folder)
            # copy_expected = shlex.split("cp ../screens/" + input_image + " " + output_folder + "/result.png")
            return 1
        # subprocess.Popen(copy_expected, stdout=subprocess.PIPE)

        if b'Images are visibly different' in result:
            self.utils.print_info("Both screens are DIFFERENT")
            # print("Executing : cp ../screens/" + input_image + " " + output_folder)
            # copy_expected = shlex.split("cp ../screens/" + input_image + " " + output_folder + "/result.png")
            return -1

        if b'Images are perceptually indistinguishable' in result:
            self.utils.print_info("Both screens are DIFFERENT - But within the THRESHOLD")
            return 1
            # subprocess.Popen(copy_expected, stdout=subprocess.PIPE)
