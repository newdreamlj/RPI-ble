#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2017-07-03 by new dream
#

from  bluepy import btle

class notificationdelegate(btle.defaultdelegate):
    def __init__(self, params):
        btle.defaultdelegate.__init__(self)
        print "initialized delegate"
        # ... initialise here

    def handlenotification(self, chandle, data):
        # ... perhaps check chandle
        # ... process 'data'
        print "handle notification"
        print data
# initialisation  -------

address = "5c:f8:21:df:91:fc"
p = btle.peripheral( address )  # .withdelegate( notificationdelegate )
params = []
p.setdelegate( notificationdelegate(params) )

print p.delegate

# setup to turn notifications on, e.g.
#   svc = p.getservicebyuuid( service_uuid )
#   ch = svc.getcharacteristics( char_uuid )[0]
#   ch.write( setup_data )

# main loop --------

while true:
    if p.waitfornotifications(1.0):
        # handlenotification() was called
        continue

    print "waiting..."
    # perhaps do something else here


