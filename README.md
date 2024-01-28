# DCC Receive
UART port listener to receive incoming MOB (Man-Overboard) Packets from ESP32 Submersion Handler. 


![Drawing27](https://github.com/riverdale-soc/nanorecieve/assets/68623356/34ebe1ff-c3ad-4df4-9e06-9ed761819c43)

## Setup 
Guide for deploying this project on a local Jetson Nano. Assumes core dependencies already exist (python3, git)
### Installation
```
git clone https://github.com/riverdale-soc/nanorecieve.git
cd nanoreceive
git submodule init -update
pip3 install -e .
```
### HW Setup
* ESP32 Module connected over USB to Jetson Nano
Ensure USB device shows up as device
```
ls /dev
```
Should appear as '/dev/ttyUSB0'

## Running
```
sudo python3 src/DCC_Receive.py
```

## Testing
```
python3 src/Test_DCC_Receive.py
```
