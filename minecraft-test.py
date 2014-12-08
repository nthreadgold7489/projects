import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)
block=mc.getBlockWithData(10,-27,18)
mc.postToChat(block.id)
       
def place_stone():
    x,y,z=mc.player.getPos()
    mc.setBlock(x,y+3,z,1)
    time.sleep(0.5)
    place_stone()

def place_flower():
    while True:
        x,y,z=mc.player.getPos()
        mc.setBlock(x,y,z,38)
        time.sleep(0.2)

