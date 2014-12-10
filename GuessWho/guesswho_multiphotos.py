import picamera,time

x=5
names=()
def checkname():
    name=input('Name:')
    if name not in names:
        names.append(name)

    else:
        print('Someone else has that name')
        checkname()

with picamera.PiCamera() as camera:
     for i in range(x-1):
        checkname()
        camera.start_preview()
        time.sleep(1.5)
        camera.capture('%s.jpg'%name)
    
