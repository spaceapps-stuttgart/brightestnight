#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
bdata = []
gdata = []
rdata = []

avgB = 0
avgG = 0
avgR = 0

#opening the file from guvcview
def open_file(filename):
    f = open(filename, 'r')
    raw_data = f.read()
    return raw_data


data = open_file('Image_black.raw')

#Blue Data
for i in range(0, len(data), 96):
    value = data[i]
    value = ord(value)
    bdata.append(data[value])
    avgB += value

#Green Data
for i in range (1, len(data), 96):    
    value = data[i]
    value = ord(value)
    gdata.append(value)
    avgG += value

#Red Data
for i in range(2, len(data), 96):
    value = data[i]
    value = ord(value)
    rdata.append(value)
    avgR += value 

#calculating averages
avgB = avgB / len(bdata)
avgG = avgG / len(gdata)
avgR = avgR / len(rdata)


print avgB, avgG, avgR



