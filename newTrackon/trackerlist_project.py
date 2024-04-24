from time import sleep

import requests

from newTrackon import trackon

tracker_list = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt"
]


def main():
    while True:
        for tl in tracker_list:
            tlist = requests.get(tl)
            trackon.enqueue_new_trackers(tlist.text)
        sleep(86400)
