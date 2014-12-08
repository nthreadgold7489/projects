userName = ""
password="nick"
guess=""
x=1
#while userName=="" :
   # print("Please enter your name using only letters.")
   # userName = input("What is your name?")
    
while guess!=password :
    guess = input("What is the password?")
    x+=1
else:
    print ("it took you {0} guesses.".format(x))
#print("Good morning {0}".format(userName))

