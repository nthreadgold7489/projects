import picamera,time

x= int(raw_input('Time:'))

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    for filename in camera.capture_continuous('img{counter:03d}.jpg'):
        print('Captured %s'%filename)
        time.sleep(x)
