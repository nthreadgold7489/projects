import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus random
mc=minecraft.Minecraft.create() #Create game and connect to it

def make(i,block,colour): #Function with initial, block and color parameters
    n_x,n_y,n_z=mc.player.getPos() #Finds out players position
    n_x+=2 #increments x coordinate so initial isn't built on top of player
    n_y+=7 #increments y coordinate so initial isn't built on top of player
    n_z+=2 #increments z coordinate so initial isn't built on top of player
    for each in i: #Loops through parameter 'i' which is a string of letter(s). Each letter is related to the coorndinates list below.
            n_y-=1  
            for x in each: #Loop through coordinates and place block at respective coordinates
                n_x+=x
                mc.setBlock(n_x,n_y,n_z,block,colour)

n=((0,4),(0,4),(0,1,4),(0,2,4),(0,3,4),(0,4),(0,4)) #List of lists. Each small list shows the x coordinates for one horizonatal line of the initial when placed onto a grid system
t=(range(5),(2),(2),(2),(2),(2),(2))
a=((1,2,3),(0,4),range(5),(0,4),(0,4),(0,4))


make(a,35,9)
