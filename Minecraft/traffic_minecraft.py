import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)


black=7

def red(x,y,z): #Function to turn lights at certain coordinates (as defined by the parameters) to red
    mc.setBlock(x,float(y+5),z,35,14)

def amber(x,y,z):#Function to turn lights at certain coordinates (as defined by the parameters) to amber
    mc.setBlock(x,float(y+4),z,35,1)

def green(x,y,z):#Function to turn lights at certain coordinates (as defined by the parameters) to green
    mc.setBlock(x,float(y+3),z,35,5)
    
def reset(x,y,z):#Function to turn lights at certain coordinates (as defined by the parameters) back to ordinary towers of black blocks
    for i in range(0,6):
        mc.setBlock(x,y+i,z,35,black)
   
    
#Create trafic lights and keep rotating through pattern of light changes automatically with specified waiting periods in between
def traffic(x,y,z):
    while True: #Constant looping 
        reset(x,y,z)
        red(x,y,z)
        time.sleep(5)
        reset(x,y,z)
        red(x,y,z)
        amber(x,y,z)
        time.sleep(2)
        reset(x,y,z)
        green(x,y,z)
        time.sleep(5)
        reset(x,y,z)
        amber(x,y,z)
        time.sleep(3.5)
        reset(x,y,z)
    else:
        mc.postToChat('Issue with traffic lights.') #Alert user is there is a problem




x,y,z=mc.player.getPos() 
traffic(x,y,z) #Calls traffic function on players coordinates.

    
    
    



