import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)


while True:
    x,y,z=mc.player.getPos()
    if y<-20:
        mc.player.setPos(x,y+50,z+5)
    else:
        pass
