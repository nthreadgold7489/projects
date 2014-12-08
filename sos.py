# sos flasher by Nick Theadgold
import RPi.GPIO as GPIO

import time

#sets numbering format for GPIO holes
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)


def dot():
        print('.')
        GPIO.output(11,False)
        time.sleep(0.5)
        GPIO.output(11,True)
        time.sleep(0.5)
	

def dash():
        print('-')
        GPIO.output(11,False)
        time.sleep(2)
        GPIO.output(11,True)
        time.sleep(0.5)
	
	
	

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
                
                


def translate(x):
        for i in x:
                if i.isalpha()==True:
                        morse_letter(i)
                else:
                     pass



def text_input():
        x=input("Enter text:")
        x=x.lower()
        translate(x)

text_input()
                     
























