#Validating a photograph by NT

import time,picamera #imports necessary modules

name=""
while name == "":
    name=input('Photo name:') #Gets file name and makes sure it is longer than one character

def capture(name): #Defines function for capturing image
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(2)
        camera.capture(str(name))
        camera.stop_preview()

check=""

def validate_capture(x):  #Defines function for capturing image, validating if it is okay input and retaking photo if the user dislikes it.
    capture(x)
    while check != 'yes' or check!='no':
        check=input('Is it okay?')
        check=check.lower()
    if check== 'yes':
        print('Saved')
    elif check == 'no':
        capture(str(name))
    
        
validate_capture(name)
