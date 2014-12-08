import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)


black=7

def red(x,y,z):
    mc.setBlock(x,float(y+5),z,35,14)

def amber(x,y,z):
    mc.setBlock(x,float(y+4),z,35,1)

def green(x,y,z):
    mc.setBlock(x,float(y+3),z,35,5)
    
def reset(x,y,z):
    for i in range(0,6):
        mc.setBlock(x,y+i,z,35,black)
   
    

def traffic(x,y,z):
    while True:
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
        mc.postToChat('Issue with traffic lights.')




x,y,z=mc.player.getPos()
traffic(x,y,z)
time.sleep(2)
x1,y1,z1=mc.player.getPos()
traffic(x1,y1,z1)
time.sleep(2)
x2,y2,z2=mc.player.getPos()
traffic(x2,y2,z2)
time.sleep(2)

    
    
    



