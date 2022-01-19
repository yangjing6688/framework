import datetime
import subprocess
from time import sleep


class Recording(object):
    def __init__(self):
        self.videoRecording = -1
        _time_stamp = datetime.datetime.now()
        print(str(_time_stamp.strftime("%Y%m%d%H%M%S%f")))

    def start_video_recording(self, _file_name):
        """
        Starts video recording for test execution and saves recoding in file
        :param _file_name: File name where recording has to be stored
        :return:
        """
        _time_stamp = datetime.datetime.now()

        file_name = str(_file_name) + "_" + str(_time_stamp.strftime("%Y%m%d%H%M%S%f")) + ".avi"
        cmd = "ffmpeg -f gdigrab -t 180 -framerate 60 -i desktop -c:v libx264rgb -crf 0 " + \
              "-pix_fmt bgra -preset ultrafast recordings\\" + file_name
        self.videoRecording = subprocess.Popen(cmd, shell=True)  # start recording
        sleep(10)
        print("Done!" + str(self.videoRecording.pid))
        return "recording started..."

    def stop_video_recording(self):
        """
        Stops video recording
        """
        print("======================================")
        print(str(self.videoRecording.pid))
        print("======================================")
        subprocess.call('taskkill  /T /F /PID ' + str(self.videoRecording.pid))
        return "recording stopped"


if __name__ == "__main__":
    obj = Recording()
    obj.start_video_recording("delet_policy")