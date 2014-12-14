import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)
def countdown(x):
    if x==0: #When countdown is finished, say goodbye
        mc.postToChat("goodbye world")
    else: #Otherwise, output how many seconds are left
        mc.postToChat(str(x))
        time.sleep(1) #Wait one second between outputting of 'x' to give impression of countdown
        x-=1
        countdown(x) #Recursive loop calling countdown() on new value of 'x'

countdown(5) #Test run of code
