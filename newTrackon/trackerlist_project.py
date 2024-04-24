from time import sleep
import logging

import requests

from newTrackon import trackon

logger = logging.getLogger("newtrackon")

tracker_list = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/best.txt"
]


def main():
    while True:
        trackers = ''
        for url in tracker_list:
            logger.info(f"Download new trackers from: {url}")
            try:
                tlist = requests.get(url)
                if tlist.status_code == 200:
                    trackers += tlist.text
                else:
                    logger.warn(f"Download fail: {tlist.status_code}")
            except Exception as e:
                logger.warn(f"Download fail: {e}")
        tracker_count = len(trackers.split())
        logger.info(f"Enqueue {tracker_count} new trackers")
        trackon.enqueue_new_trackers(trackers)
        sleep(86400)
