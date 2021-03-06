#!/usr/bin/env python
# -*- coding: utf-8 -*-
# lsusb to check device name
#dmesg | grep "tty" to find port name

import serial,time
import mqtt

if __name__ == '__main__':
    
    print('Running. Press CTRL-C to exit.')
    with serial.Serial("/dev/ttyUSB0", 115200, timeout=1) as arduino:
        with serial.Serial("/dev/ttyUSB1", 115200, timeout=1) as arduino2:
        #if 1==1:
            time.sleep(0.1) #wait for serial to open
            if arduino.isOpen():
                print("{} connected!".format(arduino.port))
                while True:
                    if arduino.inWaiting()>0:
                        answer=arduino.readline()
                        answer = answer.decode()
                        print(f" res: {answer}")
                        if "F9 14 04 7F" in answer:
                              message = "Porte ouverte par Sophie"
                              answer = "ok"
                              arduino2.write(answer.encode())
                              mqtt.publish(message)
                        elif "Card read previously" in answer:
                            print("nothing to do")
                        else:
                            answer = "nok"
                            message = "Badge Inconnu la porte reste vérouillée"
                            arduino2.write(answer.encode())
                            mqtt.publish(message)
                        arduino2.flushInput() #remove data after reading
                        arduino.flushInput()
