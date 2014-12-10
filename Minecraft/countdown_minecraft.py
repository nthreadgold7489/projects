import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)
def countdown(x):
    if x==0:
        mc.postToChat("goodbye world")
    else:
        mc.postToChat(str(x))
        time.sleep(1)
        x-=1
        countdown(x)

countdown(5)
