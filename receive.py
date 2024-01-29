#OK test run 

import serial 
import time 


ser = serial.Serial(
    # Serial Port to read the data from
    port='/dev/ttyJ44',
 
    #Rate at which the information is shared to the communication channel
    baudrate = 115200,
   
    #Applying Parity Checking (none in this case)
    parity=serial.PARITY_NONE,
 
    # Pattern of Bits to be read
    stopbits=serial.STOPBITS_ONE,
     
    # Total number of bits to be read
    bytesize=serial.EIGHTBITS,
 
    # Number of serial commands to accept before timing out
    timeout=1
)

ser.flushInput()

while True: 
    try: 
        if ser.in_waiting > 0: 
            serial_data = ser.readline().decode('').rstrip()
            print('Receieved Data:' + serial_data)

        time.sleep(0.01)
    
    except KeyboardInterrupt: 
        print("Exiting Program")
        break 
    except Exception as e: 
        print("An error occurred: ", e)
        break 
ser.close()
