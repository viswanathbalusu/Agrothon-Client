<div align="center">
<h1>Agrothon Client</h1>
<h3>A Client for Agrothon Running in Raspberry Pi</h3>
<a href="https://pypi.org/project/AgroClient"><img alt="PyPI" src="https://img.shields.io/pypi/v/AgroClient?style=for-the-badge"></a>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/AgroClient?style=for-the-badge">
<img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/AgroClient?style=for-the-badge">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/AgroClient?style=for-the-badge">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/AgroClient?style=for-the-badge">
<a href="https://github.com/viswanathbalusu/Agrothon-Client/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/Agrothon-Client/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/Agrothon-Client/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/Agrothon-Client/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>

</div>

## Installation
- First Install the dependencies
    ```
    sudo apt-get update
    sudo apt-get install python3-opencv python3-rpi.gpio
    ```
- from Pypi

    ```
    pip3 install AgroClient
    ```
- From git

  ```
  pip3 install git+https://github.com/viswanathbalusu/Agrothon-Client
  ```
## Usage

```
usage: AgroClient [-h] [-y HOSTNAME] [-a APIKEY] [-u USB]

optional arguments:
  -h, --help  show this help message and exit
  -y, --hostname HOSTNAME API Server host name
  -a, --apikey APIKEY API Key of host
  -u, --usb USB     USB Port of Arduino
```

## Circuit Diagram

![Circuit](.github/CircuitDiagram.jpg)

## Pin Configuration

- **Raspberry Pi**

    | GPIO | Device | Use | Mode |
    | :---: | :---: | :---: | :---: |
    | `12` | Relay | To Switch on/off Relay | OUT |
    | `25` | PIR1 | Motion Detection | IN |
    | `8` | PIR2 | Motion Detection | IN |
    | `7` | PIR3 | Motion Detection | IN |
    | `1` | PIR3 | Motion Detection | IN |

- **Arduino nano**

    | Pin | Device | Device pin | Mode |
    | :---: | :---: | :---: | :---: |
    | `A0` | Moisture Sensor* | Analog Out | IN |
    | `D12` | DHT11 | Signal | IN |
  
    ```* For multiple sensors use differnet Analog pins```

- Connect the Pi camera accordingly
- Use SSH to access the terminal and run the Python Code
- Connect all the `Vdd's` and `GND's` Accordingly

## Note
- To get the USB Device ID, Use
    ```
    ls /dev/tty*
    ```
    Most Probably the Value will be `/dev/ttyUSB0`

- Sensor data should be sent in the following pattern
  
    ```
    mositure1,moisture2,moisture3, .... ,moistureN, Temperature,Humidity 
    ```
