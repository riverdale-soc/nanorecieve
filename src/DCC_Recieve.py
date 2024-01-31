

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
        mob_pattern = [x.strip() for x in line.split(', ')]
        print(mob_pattern)
        if mob_pattern[0] != "MOB":
            return False
        if len(mob_pattern) != 5:
            raise MOBParserException("Invalid MOB Wake String Format")

        #Finding and storing MOB State
        if mob_pattern[1] == "WAKE":
            self.mob_wake_dict['MOB_STATE'] = MOB_STATE.MOB_WAKE
        elif mob_pattern[1] == "RESET":
            self.mob_wake_dict['MOB_STATE'] = MOB_STATE.MOB_RESET
        elif mob_pattern[1] == "NONE":
            self.mob_wake_dict['MOB_STATE'] = MOB_STATE.MOB_NONE
        else:
            raise MOBParserException("Invalid MOB State")

    # Parse and validate altitude, longitude, and latitude
        try:
            altitude = float(mob_pattern[2])
            self.mob_wake_dict["Altitude"] = mob_pattern[2]
        except ValueError:
            raise MOBParserException("Invalid Altitude")
        try:
            longitude = float(mob_pattern[3])
            self.mob_wake_dict["Longitude"] = mob_pattern[3]
        except ValueError:
            raise MOBParserException("Invalid Longitude")
        try:
            latitude = float(mob_pattern[4])
            self.mob_wake_dict["Latitude"] = mob_pattern[4]
        except ValueError:
            raise MOBParserException("Invalid Latitude")

        self.mob_time = time.time()
        return True

    def close_port(self) -> bool:
        self.port.close()
        return

if __name__ == '__main__':
    dcclisten = DCCListener()
    dcclisten.init_port()
    dcclisten.listen()
