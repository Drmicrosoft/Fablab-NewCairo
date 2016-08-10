Client.py




#!/usr/bin/python

import pygst
pygst.require("0.10")
import gst
import pygtk
import gtk
import socket

class Main:
    def __init__(self):
     
        player = gst.parse_launch("  udpsrc port=5201 !  application/x-rtp, encoding-name=JPEG,payload=26 !  rtpjpegdepay !  jpegdec !  autovideosink")
        player.set_state(gst.STATE_PLAYING)
       


       

start=Main()
gtk.main()
#print (player.v4l2src_device_fd)


