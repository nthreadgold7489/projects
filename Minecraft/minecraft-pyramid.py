#Demonstration of for loops in python
import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando

mc=minecraft.Minecraft.create() 
time.sleep(4)
mc.setBlocks(-30,0,-30,30,30,30,0) #Sets blocks in those coordinates to air
def make_pyramid_loc(r):
    x,y,z=mc.player.getPos()
    x+=10
    z+=10
    for base in range(r):  #loops through parameters and sets wool block at different colours relative to each number in the parameters.
        mc.postToChat(base+1)
        mc.setBlocks(x-base,y-base+r-1,z-base,x+base,y-base+r-1,z+base,35,4)
        time.sleep(1)  #waits 0.05 seconds before reiterating through the list.

def make_pyramid(r):
    for base in range(r):  #loops through parameters and sets wool block at different colours relative to each number in the parameters.
        mc.postToChat(base+1)
        mc.setBlocks(-base,-base+r-1,-base,base,-base+r-1,base,35,4)
        time.sleep(1)  #waits 0.05 seconds before reiterating through the list.


make_pyramid_loc(8)
make_pyramid(8)

