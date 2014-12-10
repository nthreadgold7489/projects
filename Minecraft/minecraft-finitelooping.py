#Demo of for loops

import time,mcpi.minecraft as minecraft #imports necessary modules and renames one as minecraft for easy of use
mc=minecraft.Minecraft.create() # Creates game and connects to it.

time.sleep(3)

for block in (0,2,4,6,8,10):
    mc.setBlock(0,10,block,22)
    time.sleep(0.6)
    
for name in ('Harry','Bethany','Jo','Katie'):
    mc.postToChat(name)
    time.sleep(0.2)
