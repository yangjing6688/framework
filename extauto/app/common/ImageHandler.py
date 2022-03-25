import cv2
import time
from common.CloudDriver import CloudDriver
from selenium.webdriver.common.action_chains import ActionChains


class ImageHandler:
    def __init__(self):
        self.method = cv2.TM_SQDIFF_NORMED
        self.driver = extauto.common.CloudDriver.cloud_driver
        # 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
        # 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'

    def get_position(self, target_icon):
        # Read the images from the file
        small_image = cv2.imread(target_icon)
        self.driver.save_screenshot('screen1.png')
        time.sleep(5)

        large_image = cv2.imread('screen1.png')

        # result = cv2.matchTemplate(small_image, large_image, method)
        result = cv2.matchTemplate(large_image, small_image, self.method)
        # We want the minimum squared difference
        mn, _, _mnLoc, _ = cv2.minMaxLoc(result)

        # Draw the rectangle:
        # Extract the coordinates of our best match
        _MPx, _MPy = _mnLoc

        # Step 2: Get the size of the template. This is the same size as the match.
        trows, tcols = small_image.shape[:2]

        # Step 3: Draw the rectangle on large_image
        cv2.rectangle(large_image, (_MPx, _MPy), (_MPx+tcols, _MPy+trows), (0, 0, 255), 2)
        # print MPx, MPy
        # print MPx+tcols, MPy+trows
        # print (MPx+MPx+tcols)/2, (MPy+MPy+trows)/2
        # Display the original image with the rectangle around the match.
        # cv2.imshow('output', large_image)

        # The image is only displayed if we call this
        # cv2.waitKey(0)
        return (_MPx+_MPx+tcols)/2, (_MPy+_MPy+trows)/2

    def click_image(self, target_icon):
        actions = ActionChains(self.driver)
        x, y = self.get_position(target_icon)
        time.sleep(5)
        actions.move_to_element_with_offset(self.driver.find_element_by_tag_name('body'), 0, 0)
        # print x, y
        time.sleep(5)
        actions.move_by_offset(x, y).click().perform()

