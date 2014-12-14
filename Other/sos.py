# sos flasher by Nick Theadgold
import RPi.GPIO as GPIO,time #Imports necesary modules

#sets numbering format for GPIO holes
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def dot(): #Function to make light flash quickly, and print a dot
        print('.')
        GPIO.output(11,False) #Turn light on
        time.sleep(0.5) #Wait 
        GPIO.output(11,True) #Turn light off
        time.sleep(0.5) #Wait (this is the interval between dots and dashs)
	

def dash(): #Function to make light flash for longer period of time
        print('-')
        GPIO.output(11,False) #Turn light on
        time.sleep(2) #Wait for longer
        GPIO.output(11,True) #Turn off
        time.sleep(0.5) #Wait for gap between end of this dash and start of next dot/dash
	
	
	
#Function for outputting necessary dots and dashs based on given letter (parameter 'x')
def morse_letter(x):
        if x=='a':
                dot()
                dash()
        elif x=='b':
                dash()
                dot()
                dot()
                dot()
        elif x=='c':
                dash()
                dot()
                dash()
                dot()
        elif x=='d':
                dash()
                dot()
                dot()
        elif x=='e':
                dot()
        elif x=='f':
                dot()
                dot()
                dash()
                dot()
        elif x=='g':
                dash()
                dash()
                dot()
        elif x=='h':
                dot()
                dot()
                dot()
                dot()
        elif x=='i':
                dot()
                dot()
        elif x=='j':
                dot()
                dash()
                dash()
                dash()
        elif x=='k':
                dash()
                dot()
                dash()
        elif x=='l':
                dot()
                dash()
                dot()
                dot()
        elif x=='m':
                dash()
                dash()
        elif x=='n':
                dash()
                dot()
        elif x=='o':
                dash()
                dash()
                dash()
        elif x=='p':
                dot()
                dash()
                dash()
                dot()
        elif x=='q':
                dash()
                dash()
                dot()
                dash()
        elif x=='r':
                dot()
                dash()
                dot()
        elif x=='s':
                dot()
                dot()
                dot()
        elif x=='t':
                dash()
        elif x=='u':
                dot()
                dot()
                dash()
        elif x=='v':
                dot()
                dot()
                dot()
                dash()
        elif x=='w':
                dot()
                dash()
                dash()
        elif x=='x':
                dash()
                dot()
                dot()
                dash()
        elif x=='y':
                dash()
                dot()
                dash()
                dash()
        elif x=='z':
                dash()
                dash()
                dot()
                dot()
        elif x=='':
                pass
        else:
                print('Could not translate '+ x)
                
                

#Function that loops through each letter in a string and translates to morse
def translate(x):
        for i in x:
                if i.isalpha()==True:
                        morse_letter(i) #Use above function to output that letter as a morse signal
                else:
                     pass



def text_input(): #Allow user to input text, convert to lower case so the morse_letter() function can understand and then translatethe string
        x=input("Enter text:")
        x=x.lower()
        translate(x)

text_input() #Test run of program
                     
























