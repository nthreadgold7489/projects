import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.
from random import randint


def teleport():
    x=randint(0,128)
    y=randint(0,128)
    z=randint(0,128)
    mc.player.setPos(x,y,z)
    
    

def follow_random(a,b,c):
    d=a/b               #Divides time between teleports by frequency of block follow, to work out how many blocks should be made in block follow before teleporting again. Assigns this to variable 'd'.
    while d>0:
        randomnum=randint(1,110)
        if randomnum!=10 or randomnum!=11:
            x,y,z=mc.player.getPos()
            mc.setBlock(x,y,z,randomnum)
            time.sleep(b)
            d-=1
            
        else:
            follow_random(a,b,c)
    
def follow_random_teleport(a,b,c): #a= how many seconds between teleport, b=how often block follow is made, c=num. of teleports
    while c>0:
        teleport()
        follow_random(a,b,c)
        c-=1
    else:
        mc.postToChat('Finished')
    

time.sleep(3)
mc.postToChat('Starting teleport and follow...')

follow_random_teleport(30,0.5,3)
        
