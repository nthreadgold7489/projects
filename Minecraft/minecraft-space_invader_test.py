import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando
mc=minecraft.Minecraft.create() #Connects to open minecraft world

time.sleep(2) #Sleeps for 2 seconds to allow user to switch from IDLE to Minecraft
def spaceinvader(i,xloc,y,z,block,colour): #Defines function which takes parameters referring to coordinates of where to set the blocks, coordinates of where the space invader is in relevance to the world and the block type and state the SI is built with.
    for each in i:  #For every line of blocks being set the y coordinate is subracted by 1` so that the space invader isn't built on top of itself
        y-=1
        for x in each:  #loops through coordinates of blocks being set and sets necessary blocks
            x+=xloc
            mc.setBlock(x,y,z,block,colour)
            
def makethendeletewithflash():#Defines function that builds space invader near player, and when the player moves, deletes  previous SI and builds a new one,hanging colour by selecting random variable.
    x,y,z=mc.player.getPos() #Finds players pos so the SI is built relative to the player
    y+=4 #Increases y coordinate by 4 to make the SI at eye level for player.
    spaceinvader(all_lines,x+10,y,z+10,35,random.randint(0,15))#Builds SI in random colour
    time.sleep(0.2) #Pauses for 0.2 seconds so that when function is looped it doesn't use too much processing power.
    spaceinvader(all_lines,x+10,y,z+10,0,0) #Deletes SI by setting all previous space invader blocks to air.


all_lines=((2,8),(3,7),range(2,9),(0,2,4,5,6,8,10),range(11),(0,2,3,4,5,6,7,8,10),(0,2,8,10),(3,4,6,7)) #Coordinatess for where blocks need to be built.

while True: #Infitely runs code to make a flashing spaceinvader follow the player
    makethendeletewithflash()
