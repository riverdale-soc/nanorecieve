"""
Author: Sophia Ventresca
ESP32 Submersion Handler UART Listener
Opens USB-Serial Port and waits for Wake String, then constructs MOB Wake Dict
"""

import serial
import time
import enum

# Define exceptions for MOB Parser, Invalid state, invalid format, etc.
class MOBParserException(Exception):
    pass


# Enum of valid MOB States
class MOB_STATE(enum.Enum):
    MOB_WAKE = "WAKE"
    MOB_RESET = "RESET"
    MOB_NONE = "NONE"

class DCCListener:
    def __init__(self):

        self.mob_wake_dict = {
            'MOB_STATE' : MOB_STATE.MOB_NONE, 
            'Altitude' : "",
            'Longitude' : "",
            'Latitude' : "",
        }

        self.mob_time = None

    def init_port(self) -> bool:
        """
          Open Serial Port to ESP32. 
          UART Configs: 115200 Baud, 8N1, XON/XOFF, PARITY NONE, RTS/CTS, 
        """
        self.port = serial.Serial('/dev/ttyUSB0', baudrate=115200, xonxoff=True)
        if self.port.is_open is not True:
            self.port.open()


    # Read all lines from serial port, and parse for MOB Wake String
    def listen(self):
        while True:
            line = self.port.readline().decode('utf-8')
            if self.parse_line(line) is True:
                # Implement wake up logic here
                print("MOB Wake String Received")
            print(line)

    # Parse line for MOB Wake String
    # We will assume it will come in a single line like: 
    # MOB indicates MOB Wake String, MOB State, Altitude, Longitude, Latitude
    #        "MOB: OK, 12345.12345, 12345.12345, 12345.12345"
    def parse_line(self, line: str) -> bool:
        # Read line from serial port
        # Parse line for MOB Wake String, if true, update MOB Wake Dict
        # if it is not a MOB Wake String, return false
        # if the state is invalid, raise exception


        # Store timestamp of MOB Wake String found 
        self.mob_time = time.time()
        return False
 
    def close_port(self) -> bool:
        self.port.close()
        return 0

if __name__ == '__main__':
    dcclisten = DCCListener()
    #dcclisten.listen()
