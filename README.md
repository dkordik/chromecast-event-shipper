# chromecast-event-shipper

Listen for media status events (play/pause) from Chromecast devices on the local network, and ship them along to a local REST service

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