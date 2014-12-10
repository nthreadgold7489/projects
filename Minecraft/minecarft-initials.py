import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando
mc=minecraft.Minecraft.create()

def make(i,block,colour):
    n_x,n_y,n_z=mc.player.getPos()
    n_x+=2
    n_y+=7
    n_z+=2
    for each in i:
            n_y-=1
            for x in each:
                n_x+=x
                mc.setBlock(n_x,n_y,n_z,block,colour)

n=((0,4),(0,4),(0,1,4),(0,2,4),(0,3,4),(0,4),(0,4))
t=(range(5),(2),(2),(2),(2),(2),(2))
a=((1,2,3),(0,4),range(5),(0,4),(0,4),(0,4))


make(a,35,9)
