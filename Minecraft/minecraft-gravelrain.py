import random,time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)  #Waits for 3 seconds.

gravel=13   #Saves minecraft's gravel block ID as 'gravel' for easy of use.

while True:   #Loops infinitely
    x,y,z=mc.player.getPos() #Finds players position
    mc.setBlock(float(x+random.randint(-10,10)),float(y+50),float(z+random.randint(-10,10)),random.randint(12,13)) #Uses players position to randomly place blocks of sand above the player in a certain radius. The blocks fall, making it appear like it's raining sand.
    time.sleep(0.2)   #Slows loop by adding a sleep for 0.2, so the program doesn't use to much processing power.
