import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)
x,y,z=mc.player.getPos()



while True:
    x,y,z=mc.player.getPos()
    mc.setBlocks(x+12,y+12,z+12,x-12,y,z-12,0)
    
