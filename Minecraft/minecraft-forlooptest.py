#Demonstration of for loops in python
import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando

mc=minecraft.Minecraft.create() 

mc.setBlocks(-30,-5,-30,30,30,30,0) #Sets blocks in those coordinates to air

for b in range(30):  #loops through parameters and sets wool block at different colours relative to each number in the parameters.
    for b2 in range(30):
        mc.postToChat(b)  #posts to the mc Chat the number in the list so you can see what is happening as it happens. (bug decoder)
        mc.setBlock(b,b2,0,35,b)
        time.sleep(0.05)  #waits to seconds before reiterating through the list.
