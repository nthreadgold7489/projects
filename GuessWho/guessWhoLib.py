
#Library for GuessWho by NT


hairColors = ["brown","blonde","ginger","grey","white","red"]
eyeColors = ["grey","brown","green","blue"]
genders = ["f","female","m","male"]

def getPicture(name):
    try:
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture("{0}.jpeg".format(name))
            camera.stop_preview()
    except picamera.exc.PicameraMMALError:
        print('Could not detect camera')


def validate(question,possAnswers):  #Defines function that check if input (inp) for the question (question) has been entered.
    inp=""
    while inp not in possAnswers:
            inp=input(str(question))
            inp=inp.lower()
    

def getCharProfile():   #Defines function to get characteristics of user, asking them each question until a valid input is given.
    name=input('What is your name?')
    hairColor=validate('What is your hair color?',hairColors)
    hat=validate('Do you have a hat?',['y','n','yes','no'])
    eyes=validate('What color are your eyes?',eyeColors)
    gender=validate('What gender are you?',genders)
    facialHair=validate('Do you have any facial hair?',['y','n','yes','no'])
    glasses=('Do you wear glasses?',['y','n','yes','no'])

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
    
    charProfile=(hairColor,hat,name,eyes,gender,facialHair,glasses)
    return charProfile
