#Validating a photograph by NT

import time,picamera #imports necessary modules

name=""
while name == "": #Starts potentially infinite loop
    name=input('Photo name:') #Make sure file name is longer than one character (loops until it is)

def capture(name): #Defines function for capturing image
    with picamera.PiCamera() as camera: #Change name of camera module and use with keyword for safe shutdown after camera module has been used
        camera.start_preview() #Begin preview to allow camera time to adjust to surroundings
        time.sleep(2) #Allow camera time to adjust to surroundings
        camera.capture('{0}.jpg'.format(name))  #Capture photo and save it as given name
        camera.stop_preview() #End capturing process



def validate_capture(x):  #Defines function for capturing image, validating if it is okay input and retaking photo if the user dislikes it.
    capture(x)
    while check != 'yes' or check!='no': #Loop until user says the photo is either okay or not.
        check=input('Is it okay?') #Get user input
        check=check.lower() #make it lower case so only have to compare it to 'yes' rather than 'yes' and 'YES'.
    if check== 'yes': # Compare input to yes
        print('Saved') # If the user is happy, don't overwrite photo
    elif check == 'no':
        capture(str(name)) # Take another photo and overwrite previous one if user doesn't like it
    
        
validate_capture(name) #Test photo and validation check
