import argparse
import logging
import sys
import time
import datetime
import requests
import zeroconf
import pychromecast
from pychromecast.controllers.media import MediaStatusListener

class MyMediaStatusListener(MediaStatusListener):
    def __init__(self, name, cast, host, api_url):
        self.name = name
        self.cast = cast
        self.host = host
        self.api_url = api_url

    def new_media_status(self, status):
        print("\n[", time.ctime(), " - ", self.name, "] --", status.player_state,
              "-- status media change:")
        print(status)

        status_dict = {key: value.isoformat() if isinstance(value, datetime.datetime) else value
                       for key, value in status.__dict__.items()}
        
        payload = {
            'chromecast_name': self.name,
            'chromecast_host': self.host,
            'media_status': status_dict
        }

        requests.post(self.api_url, json=payload)

    def load_media_failed(self, item, error_code):
        print("[", time.ctime(), " - ", self.name, "] load media failed for item: ", item, " with code: ", error_code)

parser = argparse.ArgumentParser(description="Listen for Chromecasts and log media status events.")
parser.add_argument("--known-host", help="Add known host (IP), can be used multiple times", action="append")
parser.add_argument("--show-debug", help="Enable debug log", action="store_true")
parser.add_argument("--show-zeroconf-debug", help="Enable zeroconf debug log", action="store_true")
parser.add_argument("--api-url", help="API URL to send chromecast events", default="http://localhost:3002/chromecastEvents")
args = parser.parse_args()

if args.show_debug:
    logging.basicConfig(level=logging.DEBUG)
if args.show_zeroconf_debug:
    print("Zeroconf version: " + zeroconf.__version__)
    logging.getLogger("zeroconf").setLevel(logging.DEBUG)

casts, browser = pychromecast.get_chromecasts(known_hosts=args.known_host)

if len(casts) == 0:
    print("No Devices Found")
    sys.exit(1)

for cast in casts:
    host = cast.cast_info.host
    print(f'Found: "{cast.name}" - host: {host}')
    cast.wait()
    listenerMedia = MyMediaStatusListener(cast.name, cast, host, args.api_url)
    cast.media_controller.register_status_listener(listenerMedia)

input("Listening for Chromecast events...\n\n")
