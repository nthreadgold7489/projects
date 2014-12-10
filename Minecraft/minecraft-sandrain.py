import random,time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)

sand=12
water=9
while True:
    x,y,z=mc.player.getPos() #Finds players position
    mc.setBlock(float(x+random.randint(-50,50)),float(y+random.randint(20,50)),float(z+random.randint(-50,50)),sand) #Uses players position to randomly place blocks of sand above the player in a certain radius. The blocks fall, making it appear like it's raining sand.
