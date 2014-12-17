
#Library for GuessWho by NT

hairColors = ["brown","blonde","ginger","grey","white","red"] #List of possible answers when validating hair color answers
eyeColors = ["grey","brown","green","blue"] #List of possible answers for eye colors
genders = ["f","female","m","male"] #Options for gender validation

import json,time,picamera #Imports modules for writing/reading/appending to file, waiting between functions and the camera module

#Create function to take picture and save it to a given name
def getPicture(name): 
    try:
        with picamera.PiCamera() as camera: #Renames camera module for ease of use
            camera.start_preview() #Begin photo preview to allow camera to adjust settings
            time.sleep(1.5) #Give cameras time to adjust
            camera.capture("{0}.jpeg".format(name)) #Take photo and save to the given filename
            camera.stop_preview() #End process
    except picamera.exc.PiCameraMMALError: #Catch error, then output error message
        print('Could not detect camera') 



#Defines function that check if input (inp) for the question (question) has been entered.
def validate(question,possAnswers):  
    inp=""
    while inp not in possAnswers: #Loop until input is valid
            inp=input(str(question))
            inp=inp.lower()
    
#Defines function to get characteristics of user, asking them each question until a valid input is given.
def getCharProfile():
    #Get user input for variety of features, doing basic validation for each feature
    name=input('What is your name?') 
    hairColor=validate('What is your hair color?',hairColors)
    hat=validate('Do you have a hat?',['y','n','yes','no'])
    eyes=validate('What color are your eyes?',eyeColors)
    gender=validate('What gender are you?',genders)
    facialHair=validate('Do you have any facial hair?',['y','n','yes','no'])
    glasses=('Do you wear glasses?',['y','n','yes','no'])

    #Validate whether user is happy with photo by comparing input to 'y' and looping until they say they are happy (input == 'y')
    user='' 
    while user.lower() != 'y':
        getPicture(name)
        user=input('Are you happy? (y/n)')

    #Change 'yes/no' answers to booleans for ease of use later on
    if hat == 'y' or hat=='yes':
        hat=True
    elif hat =='n' or hat == 'no':
        hat=False

    if facialHair == 'y' or facialHair =='yes':
        facialHair=True
    elif facialHair =='n' or facialHair == 'no':
        facialHair=False

    if glasses == 'y' or glasses=='yes':
        glasses =True
    elif glasses =='n' or glasses == 'no':
        glasses=False

    #Put all features into a list
    charProfile=(hairColor,hat,name,eyes,gender,facialHair,glasses)
    return charProfile #Return list so it can be used by other functions

def saveProfile(x): #Defines function to add new profile to list and save to txt file
    profile = getCharProfile() #Make new profile
    x.append(profile) #Adds profile to existing list
    with open('profiles.txt',mode='w',encoding='utf-8') as p: #Dump info to file using json
        json.dump(x,p)

def loadProfile(): #Defines function to read file
    try: #Attempt to run following code
        with open('profiles.txt',mode='r',encoding='utf-8') as p: #Use json to open and load specified file
            json.load(p)
    except IOError: #if it receives IOError (file not found), run below code
        print('No profiles.') #Output string to tell user
        time.sleep(1)
        print('Making new profiles...') #Then tell them new profiles are being made
        profileList = [] #Make mpty list so profiles can be added
        for i in range(5):
            saveProfile(profileList)

loadProfile()
