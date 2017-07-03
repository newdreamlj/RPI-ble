#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2017-07-03 by new dream
#

from bluepy import btle
from bluepy.btle import Scanner, DefaultDelegate
import binascii

class ScanDelegate(DefaultDelegate): 
    def __init__(self): 
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData): 
        if isNewDev: 
            print "Discovered device", dev.addr 
        elif isNewData: 
            print "Received new data from", dev.addr
            print binascii.b2a_hex(dev.rawData).decode('utf-8')
            print dev.getScanData()

address = "5c:f8:21:df:91:fc"

scanner = Scanner().withDelegate(ScanDelegate()) 
devices = scanner.scan(10.0)
# for dev in devices: 
#     print "Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi) 
#     for (adtype, desc, value) in dev.getScanData(): 
#         print "  %s = %s" % (desc, value)




