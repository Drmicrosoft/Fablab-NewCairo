import os
os.system("gst-launch-1.0 v4l2src device = /dev/video0 !  video/x-raw,width=640,height=480 ! \ jpegenc ! \ rtpjpegpay ! \ udpsink host=127.0.0.1 port=5201")
