import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3) #Wait to allow pi time to connect to minecraft instance

def place_flower(): #Function to constantly find out players position and place a block relative to this position
    while True:
        x,y,z=mc.player.getPos() #Find position of player
        mc.setBlock(x,y,z,38) #Set block next to this position
        time.sleep(0.2) #Slow down loop to avoid using too much processing power

def place_gold(): #Function to constantly place gold block near to players position
    while True:
        x,y,z=mc.player.getPos() #Find position
        mc.setBlock(x,float(y-0.2),z,41) #Place glod block next to player
        time.sleep(0.05)


place_gold() #Run place _gold function to check it functions properly
