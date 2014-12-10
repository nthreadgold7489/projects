#Demonstration of for loops in python
import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando
mc=minecraft.Minecraft.create()


def make_house(x,y,z):
    mc.setBlocks(x,y,z,x+5,y+6,z+7,45)
    mc.setBlocks(x+1,y,z+1,x+4,y+5,z+6,0)
    mc.setBlock(x,y,z+2,0)
    mc.setBlock(x,y+1,z+2,0)

mc.setBlocks(-60,0,-60,60,10,60,0)
for x in range(-51,51,10):
    for z in range(-51,51,10):
        make_house(x,0,z)
