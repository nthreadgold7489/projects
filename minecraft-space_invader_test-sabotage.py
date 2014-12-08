
import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando
mc=minecraft.Minecraft.create() #Connects to open minecraft world

time.sleep(2) #Sleeps for 2 seconds to allow user to switch from IDLE to Minecraft
def spaceinvader(i,xloc,y,z,block,colour): #Defines function which takes parameters referring to coordinates of where to set the blocks, coordinates of where the space invader is in relevance to the world and the block type and state the SI is built with.
    for each in i:  #For every line of blocks being set the y coordinate is subracted by 1` so that the space invader isn't byuilt on top of itself
        y-=1
        for x in each:  #loops through coordinates of blocks being set and sets necessary blocks
            x+=xloc
            mc.setBlock(x,y,z,block,colour)
            
def spaceinvaderdelete(i,xloc,y,z): #Defines function to delete  a space invader for use later on in the code 
    for each in i:
        y-=1
        for x in each:
            x+=xloc
            mc.setBlock(x,y,z,0)
        

def makethendelete(): #Defines function that builds space invader near player, and when the player moves, deletes  previous SI and builds a new one.
    x,y,z=mc.player.getPos()
    spaceinvader(all_lines,x+5,y,z+5,35,9)
    time.sleep(0.1)
    nx,ny,nz=mc.player.getPos()
    while True:
        if nx!=x or ny!=y or nz!=z:
            spaceinvaderdelete(all_lines,x+5,y,z+5)
            makethendelete()
        else:
            makethendelete()
        
def makethendeletewithflash():
    x,y,z=mc.player.getPos()
    spaceinvader(all_lines,x+5,y,z+5,35,random.randint(0,15))
    time.sleep(5)
    nx,ny,nz=mc.player.getPos()
    if nx!=x or ny!=y or nz!=z:
        spaceinvaderdelete(all_lines,x+5,y,z+5)
        makethendeletewithflash()
    else:
        makethendeletewithflash()
        
mc.setBlocks(-30,0,-30,30,30,30,0)
all_lines=((2,8),(3,7),range(2,9),(0,2,4,5,6,8,10),range(11),(0,2,3,4,5,6,7,8,10),(0,2,8,10),(3,4,6,7)) #Coordinatess for where blocks need to be built


while True:
    makethendeletewithflash()
