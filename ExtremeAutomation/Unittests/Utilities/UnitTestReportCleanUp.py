import os
import sys
import time
import logging


def get_removal_time(interval):
    return interval * 24 * 60 * 60  # Interval times number of seconds in a day (86400).


def remove_reports(report_dir, cleanup_int):
    logging.basicConfig(level=logging.INFO)
    if os.path.exists(report_dir):
        for report in os.listdir(report_dir):
            report_path = os.path.join(report_dir, report)

            if time.time() - os.path.getmtime(report_path) > get_removal_time(cleanup_int):
                logging.info("Current time: " + str(time.time()))
                logging.info("Modified date: " + str(os.path.getmtime(report_path)))
                logging.info("Attempting to delete file/folder: \n" + str(report_path))
                os.remove(report_path)


if __name__ == '__main__':
    _report_dir = sys.argv[1:][0]
    _cleanup_int = int(sys.argv[1:][1])
    remove_reports(_report_dir, _cleanup_int)
