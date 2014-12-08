import random,time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)


water=9

while True:
    x,y,z=mc.player.getPos() #Finds players position
    n_x=float(x+random.randint(-5,5)
    n_y= float(y+50)
    n_z=float(z+random.randint(-5,5)
    blockID= mc.getBlock(n_x,float(y-1),n_z)
    while blockID=0:
        
        mc.setBlock(n_x,n_y),n_z),water)
        n_y-=1
        mc.setBlock(n_x,n_y,n_z,0)
    

    
