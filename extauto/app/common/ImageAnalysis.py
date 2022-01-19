import cv2
import os
from common.Utils import Utils
from common.Screen import Screen

class ImageAnalysis:
    def __init__(self):
        self.utils = Utils()
        self.screen = Screen()

    def find_image(self, input_image, test_type):
        scree_shot = self.screen.take_screen_shot()
        IMAGE_FILE = scree_shot
        self.utils.print_info("Screenshot: ", os.path.abspath(IMAGE_FILE))
        CASCADE_FILE = 'channel_utilization.xml'

        CASCADE_ITEM = test_type

        i = -1
        image = cv2.imread(IMAGE_FILE)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(CASCADE_FILE)
        rectangles = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10, minSize=(100, 100))
        for (i, (x, y, w, h)) in enumerate(rectangles):
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(image, CASCADE_ITEM + "#{}".format(i + 1), (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 0, 255), 2)
        opt = "output.png"
        cv2.imwrite(opt, image)
        self.utils.look_and_feel(scree_shot, input_image, opt)

        self.utils.print_info("Number of Image Matches: " + str(i + 1))
        return i + 1
