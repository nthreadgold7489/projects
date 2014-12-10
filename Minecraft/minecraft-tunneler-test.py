import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)

while True:
    x,y,z=mc.player.getPos()
    mc.setBlocks(float(x+2),float(y+1),float(z+2),float(x-2),y,float(z-2),0)
    mc.setBlock(y+3,13)
    time.sleep(0.1)
    
        
    
