# chromecast-event-shipper

Listen for media status events (play/pause) from Chromecast devices on the local network, and ship them along to a local REST service

Uses the excellent [pychromecast](https://github.com/home-assistant-libs/pychromecast) library from the folks at https://www.home-assistant.io/

## Setup

```
./install.sh
```

## Usage

```
./run.sh
```
or update [run.sh](./run.sh) with your preferred host to ship events to:
```
python3 main.py --api-url=http://localhost:3002/chromecastEvents
```

### Example REST payload:

```json

{
  "chromecast_name": "Dan's office speakers",
  "media_status": {
    "current_time": 158.81,
    "content_id": "2U91ELKMNlE",
    "content_type": "x-youtube/video",
    "duration": 208,
    "stream_type": "BUFFERED",
    "idle_reason": null,
    "media_session_id": 1238987123,
    "playback_rate": 1,
    "player_state": "PAUSED",
    "supported_media_commands": 311363,
    "volume_level": 0.2410106658935547,
    "volume_muted": false,
    "media_custom_data": {
      "listId": "RDATgCX",
      "currentIndex": 0
    },
    "media_metadata": {
      "albumName": "Exodus",
      "artist": "Bob Marley & The Wailers",
      "images": [
        {
          "height": 544,
          "url": "https://lh3.googleusercontent.com/3KWS7wikbpENJgZ_gtnn6GK3_knhJhD-jMwZuof81gA4qVl1PFY0u9htiu_PWlh1W3IRszdwIhzHBAWj=w544-h544-l90-rj",
          "width": 544
        },
        ...
      ],
      "metadataType": 3,
      "title": "Natural Mystic"
    },
    "subtitle_tracks": {},
    "current_subtitle_tracks": [],
    "last_updated": "2023-10-22T05:26:44.850947"
  }
}
```