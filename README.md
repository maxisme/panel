# Panel
[![push](https://github.com/maxisme/panel/actions/workflows/push.yml/badge.svg?branch=master)](https://github.com/maxisme/panel/actions/workflows/push.yml) 

[![Code style: black](https://img.shields.io/badge/black-000000.svg)](https://github.com/psf/black)
[![Code style: mypy](https://img.shields.io/badge/mypy-000000.svg)](https://readthedocs.org/projects/mypy/)
[![Code style: mypy](https://img.shields.io/badge/flake8-000000.svg)](https://flake8.pycqa.org/en/latest/)


Setup a HTTP API to write notifications to your LED matrix panel connected to a Raspberry Pi.

![](https://user-images.githubusercontent.com/16902919/142736756-118a5ae4-cbf7-43c8-b1f8-93c1ff9b3c98.gif)

## Hardware Setup
What you will need:
 - Raspberry Pi
 - MAX7219 Dot Matrix Module 4-in-1 LED Display Module - e.g - https://www.banggood.com/MAX7219-Dot-Matrix-Module-4-in-1-LED-Display-Module-p-1072083.html can be found on eBay and Aliexpress as well.
 - Female to female jumper GPIO cables (if not already included)

### Connecting the panel to your Raspberry Pi 
Please follow - https://max7219.readthedocs.io/en/0.2.3/#gpio-pin-outs - on how to connect the MAX7219 Panel to your 
Raspberry Pi with your GPIO jumper cables.

## Software Setup
What you will need:
 - [Docker](https://get.docker.com/) & [docker-compose](https://pypi.org/project/docker-compose/)
 - A cloudflare account (& preferably a domain)

### Enable SPI on Raspberry Pi
https://max7219.readthedocs.io/en/0.2.3/#pre-requisites

### Setup Cloudflare Tunnel
So that you can run behind a firewall and not go through the pain of exposing ports you can simply create a 
cloudflare tunnel (feel free to remove `cloudflared` from the `docker-compose` if you don't want to expose) 

To setup cloudflared you first need to set up a tunnel to the panel named `panel` through cloudflare:
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
After cloning this repo on your Raspberry Pi simply run:
```
$ docker-compose up -d --build panel
```

## Sending Messages
To send a message to the board simply make a POST request to `https://panel.example.com/`

| Parameter | Type   | Description                   | Default  |
|-----------|--------|-------------------------------|----------|
| text      | string | The message you want to send. | N/A - Required |
| font      | string |                               | LCD_FONT |
| priority  | enum   | low, default, high            | default  |
| display_time   | enum   | Number of seconds to show message (only if message doesn't wrap)            | 4  |

e.g with `curl`:
```
$ curl -X POST -d 'text=hello world' https://panel.example.com/
```

## Development
### Lint
```
docker-compose up --build format
```
