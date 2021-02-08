# Panel
Setup a HTTP API to write notifications to your LED matrix panel on Raspberry Pi.

## Hardware Setup
What you will need:
 - Raspberry Pi
 - MAX7219 Dot Matrix Module 4-in-1 LED Display Module - e.g - https://www.banggood.com/MAX7219-Dot-Matrix-Module-4-in-1-LED-Display-Module-p-1072083.html can be found on eBay and Aliexpress as well.

### Connecting the panel to your Raspberry Pi 
Please follow - https://max7219.readthedocs.io/en/0.2.3/#gpio-pin-outs - on how to connect the board to your device.

## Software Setup
What you will need:
 - Docker & docker-compose
 - A cloudflare account (& preferably a domain)

### Enable SPI on Raspberry Pi
https://max7219.readthedocs.io/en/0.2.3/#pre-requisites

### Setup Cloudflare Tunnel
On your Raspberry Pi you first need to set up a tunnel to the panel named `panel` through cloudflare:
```
docker run -v ~/.cloudflared:/.cloudflared/ erisamoe/cloudflared:2021.11.0 tunnel login
docker run -v ~/.cloudflared:/etc/cloudflared/ erisamoe/cloudflared:2021.11.0 tunnel create panel
```
and add a domain to the panel route (e.g):
```bash
docker run -v ~/.cloudflared:/etc/cloudflared/ erisamoe/cloudflared:2021.11.0 tunnel route dns panel panel.example.com
```
where `example.com` is the domain you have hosted on cloudflare.

### Running
After cloning this repo simply run:
```
$ docker-compose up -d panel
```


## Sending Messages
To send a message to the board simply make a POST request to `https://panel.example.com/`

| Parameter | Type   | Description                   | Default  |
|-----------|--------|-------------------------------|----------|
| text      | string | The message you want to send. | Required |
| font      | string |                               | LCD_FONT |
| priority  | enum   | low, default, high            | default  |
