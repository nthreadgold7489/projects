#Demonstration of for loops in python

#Using for loops to create pyramids in minecraft. Made by NT.

import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus random

#Create new mc game and connect to it
mc=minecraft.Minecraft.create() 

#Wait to allow pi time to connect properly
time.sleep(4)

mc.setBlocks(-30,0,-30,30,30,30,0) #Sets blocks in those coordinates to air.
def make_pyramid_loc(r):
    x,y,z=mc.player.getPos() 
    x+=10 #Changes x coordinate so pyramid isn't built around the player.
    z+=10 #Changes z coordinate for same reasons as x.
    for base in range(r):  #loops through parameters and sets wool block at different colours relative to each number in the parameters.
        mc.postToChat(base+1)
        mc.setBlocks(x-base,y-base+r-1,z-base,x+base,y-base+r-1,z+base,35,4) #Changes height and size of layer of pyramid with each iteration of for loop. 
                                                                            # For example, the first loop creates a 1x1 layer high up, but the second loop
                                                                            #creates a 3x3 block just below the first block. Pattern is repeated until pyramid 
                                                                            # is complete.
        time.sleep(1)  #waits 0.05 seconds before reiterating through the list.

def make_pyramid(r):
    for base in range(r):  #loops through parameters and sets wool block at different colours relative to each number in the parameters.
        mc.postToChat(base+1)
        mc.setBlocks(-base,-base+r-1,-base,base,-base+r-1,base,35,4)
        time.sleep(1)  #waits 0.05 seconds before reiterating through the list.


make_pyramid_loc(8) #Calls function to build pyramid near player
make_pyramid(8)

