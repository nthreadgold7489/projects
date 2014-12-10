import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)

def place_flower():
    while True:
        x,y,z=mc.player.getPos()
        mc.setBlock(x,y,z,38)
        time.sleep(0.2)

def place_gold():
    while True:
        x,y,z=mc.player.getPos()
        mc.setBlock(x,float(y-0.2),z,41)
        time.sleep(0.05)


place_gold()
