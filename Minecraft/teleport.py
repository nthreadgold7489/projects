import random,time,mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()

def teleport():
	mc.player.setPos(random.randint(-128,128),random.randint(-128,0),random.randint(-128,128))
	time.sleep(5)
	

def new_location(x):
	
	while x>0:
		teleport()
		x-=1
	else:
		mc.postToChat('Teleportation Complete')

def countdown(x):
	
	while x>=1:
		mc.postToChat(str(x))
		time.sleep(1)
		x-=1
	else:
		pass

	
time.sleep(3)


countdown(3)

new_location(3)

