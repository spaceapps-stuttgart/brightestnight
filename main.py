#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import re

bdata = []
gdata = []
rdata = []

avgB = 0
avgG = 0
avgR = 0
def open_file():
    f = open('Image_bgr.raw', 'r')
    raw_data = f.read()
    return raw_data
    
data = open_file()
for i in range(0, len(data), 3):
    value = data[i]
    value = ord(value)
    bdata.append(data[value])
    avgB += value
for i in range (1, len(data), 3):    
    value = data[i]
    value = ord(value)
    gdata.append(value)
    avgG += value
for i in range(2, len(data), 3):
    value = data[i]
    value = ord(value)
    rdata.append(value)
    avgR += value 
#print 'bdata:'
#for i in bdata:
#    print chr(i)
#print  bdata
#print len(bdata)
#print 'gdata:'
#print len(gdata)
#print 'rdata:'
#print len(rdata)

avgB = avgB / len(bdata)
avgG = avgG / len(gdata)
avgR = avgR / len(rdata)


print avgB, avgG, avgR



