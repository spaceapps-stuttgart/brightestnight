#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import color
import sys

__author__ = 'momo'
bdata = []
gdata = []
rdata = []

avgB = 0
avgG = 0
avgR = 0

def usage():
    print 'It looks like something went wrong!\n'
    print "Usage:\t"+sys.argv[0]+" [imagename]"

#opening the file from guvcview
def open_file(filename):
    f = open(filename, 'r')
    raw_data = f.read()
    return raw_data

try:
    data = open_file(sys.argv[1])
except IndexError:
    usage()
    exit(0)
    
step = 96 #modify this value to get a faster but therefore more unprecise result NOTE! this value must be a multiple of 3!

#Blue Data
for i in range(0, len(data), step): 
    value = data[i]
    value = ord(value)
    bdata.append(data[value])
    avgB += value

#Green Data
for i in range (1, len(data), step):    
    value = data[i]
    value = ord(value)
    gdata.append(value)
    avgG += value

#Red Data
for i in range(2, len(data), step):
    value = data[i]
    value = ord(value)
    rdata.append(value)
    avgR += value 

#calculating averages
avgB = avgB / len(bdata)
avgG = avgG / len(gdata)
avgR = avgR / len(rdata)


#outputs for each channel
cl = color.Color()
print 'Average Blue:\t ['+cl.foreground_color('blue')+('|'*(avgB/10))+(' '*((255-avgB)/10))+cl.foreground_color('default')+']  '+str(avgB)+'/255'
print 'Average Green:\t ['+cl.foreground_color('green')+('|'*(avgG/10))+(' '*((255-avgG)/10))+cl.foreground_color('default')+']  '+str(avgG)+'/255'
print 'Average Red:\t ['+cl.foreground_color('red')+('|'*(avgR/10))+(' '*((255-avgR)/10))+cl.foreground_color('default')+']  '+str(avgR)+'/255'

#overall output

total = avgB+avgG+avgR
percent = round(1.0*total/765*100, 2)
print 'Total: \t\t'+str(total)+'/765 ('+str(percent)+'%)'


