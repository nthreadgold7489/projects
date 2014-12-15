#Timelapse by NT

import picamera,time #Imports necessary modules

def timelapse(t,n,name): #Defines function with parameters 't' for time between photos,'n' for total number of photos and 'name' for filename to be saved as.
    start=time.time()
    n+=1
    with picamera.PiCamera() as camera:  #Runs timelapse code, calling picamera.PiCamera as camera instead.
        length = t*n #Works out in seconds how long timelapse will take.
        print("Starting timelapse.It will take {0} seconds to capture your timelapse called {1}.".format(str(length),str(name))#Informs user that timelapse is starting, how long it will take and what it will be saved as.
        x=1 #Sets number of pictures taken to 1.
        while n!=x:  #Keeps running (Loops) below code until pictures taken == n.
            camera.resolution=(1024,768) #Sets camera resolution to 1024x768.
            camera.start_preview() #Begins capturing process calling preview which allows camera time to focus the aperture. 
            time.sleep(t) #Waits for 't' amount of seconds to allow focusing to take place.
            camera.capture(str(name + str(x))+ '.jpeg') #Takes photo and saves it as requested name plus which picture number it is. For example the 100th picture would be saved as 'name100.jpeg'.
            x+=1 #Increments 'x' (number of pictures taken so far) by one so the while loop is finite.
            print("Photos taken: %s" % x) #Running total of photos taken
        else:
            end=time.time()- start #Work out time diff. between start and end.
            print('Ending timelapse. It took ' + str(end)) #Tell user how long timelapse actually took.


timelapse(4,25,'h') #Example of timelaspse called h, taking 25 photos in total, with a 4 second interval between capturs=es
