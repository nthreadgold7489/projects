import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando
mc=minecraft.Minecraft.create()

time.sleep(2)
def spaceinvader(i,y,z,block,colour):
    for each in i:
            y-=1
            y-=1
            for x in each:
                mc.setBlock(x,y,z,block,colour)

def spaceinvaderflashing():
    number=10
    while number>0:
        spaceinvader(all_lines,8,10,35,random.randint(0,20))
        time.sleep(8)
        number-=1

mc.setBlocks(-30,0,-30,30,30,30,0)
all_lines=((2,8),(3,7),range(2,9),(0,2,4,5,6,8,10),range(11),(0,2,3,4,5,6,7,8,10),(0,2,8,10),(3,4,6,7))


spaceinvaderflashing()
