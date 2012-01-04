import serial
import threading
import time
import copy
import math

PORT = "/dev/ttyUSB1"
BAUDRATE = 115200
TARGET = ['\xf0', '\x55', '\xaa']

serial_port = serial.Serial(PORT, BAUDRATE)

_times = []

lock = threading.Lock()

reading = True

def watch_serial():
    global serial_port, reading, times, lock
    serial_data = []
    while reading:
        a_byte = serial_port.read(1)
        if len(TARGET) == len(serial_data):
            serial_data.pop(0)
        serial_data.append(a_byte)
        #print serial_data, TARGET
        if TARGET == serial_data:
            with lock:
                _times.append(time.time())

serial_thread = threading.Thread(target=watch_serial)
serial_thread.start()

try:
    while True:
        inchar = raw_input()
        if inchar == 'q':
            break
        elif inchar == 'd':
            # Make a copy for thread safety
            this_times = None
            with lock:
                this_times = copy.copy(_times)
            # Make sure we have at least two data points to get delta times
            if len(this_times) <= 1:
                print "Need more data to report."
                continue
            # Iterate through the times and find the change from the last step
            times = copy.copy(this_times)
            for index in range(len(this_times)):
                if index == 0:
                    continue
                times[index] -= this_times[index-1]
            # Burn the first element (couldn't subtract it)
            times.pop(0)
            # Calculate and print stats
            print "Statistics with %d measurements:"%len(this_times)
            print "Mean:", sum(times)/len(times), "(seconds)"
            print "Max:", max(times), "(seconds)"
            print "Min:", min(times), "(seconds)"
            mean = sum(times)/len(times)
            deviations = [(x-mean)**2 for x in times]
            stdev = math.sqrt(sum(deviations)/(len(deviations)-1))
            print "STD:", stdev, "(seconds)"
            print "Rate:", 1.0/mean, "(Hz)"
        elif inchar == 'c':
            with lock:
                _times = []
finally:
    reading = False
    serial_thread.join()




