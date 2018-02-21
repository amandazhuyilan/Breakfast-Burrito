#!/usr/bin/python

import sys
import os
import math
from decimal import *


def sensorComp():
    # check for command line arguments
    if len(sys.argv) < 2:
        print "No input file name!\n"
        sys.exit(0)

    text_file_name = sys.argv[1]
    try:
        with open(text_file_name, 'r') as input_file:
            lines = input_file.readlines()
            encode_calibrate = []
            poten_calibrate = []

            for i in range(len(lines) - 1):
                curr_time = float(lines[i].split()[0])

                # get the potentiometer offset value at t=0
                # make lists of the encoder and potentiometer in the first 0.5 secs for callibration
                if curr_time <= 0.50:
                    curr_encode = lines[i].split()[1]
                    poten = lines[i].split()[2]
                    encode_calibrate.append(int(curr_encode))
                    poten_calibrate.append(int(poten))

                # set the min/max of the list from previous calibration and set as the starting value for 
                # calculated potentiometer min/max 
                if curr_time == 0.50 and encode_calibrate is not None:
                    cal_poten_min = min(poten_calibrate)
                    cal_poten_max = max(poten_calibrate)

                if curr_time > 0.50:
                    curr_encode = int(lines[i].split()[1])
                    next_encode = int(lines[i + 1].split()[1])
                    poten = int(lines[i].split()[2])

                    # calculating the min and max for the potentiometer
                    # take the difference between the current encoder value and sum up with the 
                    # previously calculated potentiometer value 

                    # when calculating min potemtiometer value, minus the smallest callibration encoder data 
                    # to accomondate for the smallest possible encoder data 
                    cal_poten_min = (next_encode - curr_encode - abs(min(encode_calibrate))) / 2048.0 / 30.0 * 256 + cal_poten_min
                    # when calculating max potemtiometer value, add the largest callibration encoder data 
                    # to accomondate for the smallest possible encoder data 
                    cal_poten_max = (abs(max(encode_calibrate)) + next_encode -
                                   curr_encode) / 2048.0 / 30.0 * 256 + cal_poten_max

                    # error and exit if the potentiometer reading falls outside of the calculated potentiometer range
                    if poten > cal_poten_max or poten < cal_poten_min:
                        print "Error detected at time:", curr_time
                        sys.exit(0)

        print "No errors detected!\n"

    # handles exception if cannot read/find file
    except IOError as e:
        print "Cannot read text file!\n"
        sys.exit(0)


if __name__ == '__main__':
    try:
        sensorComp()
    except:
        sys.exit(0)
