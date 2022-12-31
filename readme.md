# Raspberry Pi Ambient TV Lighting with pi camera and LEDs
## Introduction


## Hardware
Items needed:
* Raspberry Pi (I'm using RPi 3)
* Pi camera
* RGB LED strip with 3 pins for RGB and 1 pin for 12v DC power. I'm using [this](https://www.amazon.co.uk/gp/product/B07QPN985K/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&th=1) 5m LED strip.
* 3x N-channel MOSFETs. I'm using [these](https://www.amazon.co.uk/gp/product/B0893WBH6H/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1).
* Power supply for the LED strip. I'm using [this](https://www.amazon.co.uk/gp/product/B09H4NQNSL/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&th=1) 12V 2A power supply.
* Male to female jack adapter connectors. I'm using [this](https://www.amazon.co.uk/gp/product/B0106GV3SU/ref=ppx_od_dt_b_asin_title_s00?ie=UTF8&psc=1) 5.5mm x 2.1mm connector.
* Breadboard
* Jumper wires (male-to-male, male-to-female)

## Hardware setup
Connect the LED strip to the Raspberry Pi as shown in the diagram below. The LED strip has 4 pins, 3 for RGB and 1 for 12v DC power. The 3 RGB pins are connected to the 3 MOSFETs, which are connected to the Raspberry Pi GPIO pins. The 12v DC power jack is connected to the 12v DC power supply.

![Circuit diagram](https://i.imgur.com/pBzsmGk.png)

Also connect the Pi camera to the Raspberry Pi.

## Software setup
### Install required packages
Install the required packages with the following commands:
```bash
sudo pip install -r requirements.txt
```
### Enable the camera
Enable the camera with the following command:
```bash
sudo raspi-config
```
Select `Interfacing Options`, then `P1 Camera`, then `Yes` and `Finish`. Reboot the Raspberry Pi with
```bash
sudo reboot
```
### Enable the pigpio daemon
The pigpio daemon is required to control the MOSFETs. Enable it with the following command:
```bash
sudo pigpiod
```
### Run the script
Run the script with the following command:
```bash
python lights.py
```

## Create launch script
Create a new file called `launch.sh` 
```bash
nano launch.sh
```
and add the following, replacing the path to the `lights.py` script with the correct path on your system.
```bash
#!/bin/bash

# Start the pigpio daemon
sudo pigpiod

# Run the lights.py script
python /home/pi/lights.py
```
Save and exit the file with `Ctrl+X`, `Y` and `Enter`. Now make the file executable with
```bash
chmod +x launch.sh
```
To run the script on startup, we need to add it to the `rc.local` file. Open it with
```bash
sudo nano /etc/rc.local
```
Add the following line before the `exit 0` line, replacing the path to the `launch.sh` script with the correct path on your system. . The `&` at the end of the line will run the script in the background.
```bash
/home/pi/launch.sh &
```
Save and exit the file with `Ctrl+X`, `Y` and `Enter`. Now reboot the Raspberry Pi with
```bash
sudo reboot
```
Now `launch.sh` will run on startup and start the pigpio daemon and the `lights.py` script. 
