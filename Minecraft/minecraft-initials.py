import mcpi.minecraft as minecraft,time,random #Imports necessary modules plus rando
mc=minecraft.Minecraft.create()

def make(i,xloc,y,z,block,colour,d):
    xloc+=d
    y+=5
    for each in i:
        y-=1
        for x in each:
            x+=xloc
            mc.setBlock(x,y,z,block,colour)

def message(message,xloc,y,z):
    dist=10
    for letter in message:
        dist+=10
        if letter == 'a':
            make(a,xloc,y,z,35,9,dist)
        if letter == 'b':
            make(b,xloc,y,z,35,9,dist)
        if letter == 'c':
            make(c,xloc,y,z,35,9,dist)
        if letter == 'd':
            make(d,xloc,y,z,35,9,dist)
        if letter == 'e':
            make(e,xloc,y,z,35,9,dist)
        if letter == 'f':
            make(f,xloc,y,z,35,9,dist)
        if letter == 'g':
            make(g,xloc,y,z,35,9,dist)
        if letter == 'h':
            make(h,xloc,y,z,35,9,dist)
        if letter == 'i':
            make(i,xloc,y,z,35,9,dist)
        if letter == 'j':
            make(j,xloc,y,z,35,9,dist)
        if letter == 'k':
            make(k,xloc,y,z,35,9,dist)
        if letter == 'l':
            make(l,xloc,y,z,35,9,dist)
        if letter == 'm':
            make(m,xloc,y,z,35,9,dist)
        if letter == 'n':
            make(n,xloc,y,z,35,9,dist)
        if letter == 'o':
            make(o,xloc,y,z,35,9,dist)
        if letter == 'p':
            make(p,xloc,y,z,35,9,dist)
        if letter == 'q':
            make(q,xloc,y,z,35,9,dist)
        if letter == 'r':
            make(r,xloc,y,z,35,9,dist)
        if letter == 's':
            make(s,xloc,y,z,35,9,dist)
        if letter == 't':
            make(t,xloc,y,z,35,9,dist)
        if letter == 'u':
            make(u,xloc,y,z,35,9,dist)
        if letter == 'v':
            make(v,xloc,y,z,35,9,dist)
        if letter == 'w':
            make(w,xloc,y,z,35,9,dist)
        if letter == 'x':
            make(x,xloc,y,z,35,9,dist)
        if letter == 'y':
            make(y,xloc,y,z,35,9,dist)
        if letter == 'z':
            make(z,xloc,y,z,35,9,dist)
        else:
            mc.postToChat("Couldn't convert"+str(i))
         
end=(0,4)        


a=((1,2,3),end,range(5),end,end,end)
b=(range(4),end,end,range(4),end,end,range(4))
c=(range(1,4),end,(0,0),(0,0),(0,0),end,range(1,4))
d=(range(4),end,end,end,end,end,range(4))
e=(range(5),(0,0),(0,0),range(4),(0,0),(0,0),range(5))
f=(range(5),(0,0),(0,0),range(4),(0,0),(0,0),(0,0))
g=(range(1,4),end,(0,0),(0,0),(0,3,4),end,range(1,4))
h=(end,end,end,range(5),end,end,end)
i=(range(1,4),(2,2),(2,2),(2,2),(2,2),(2,2),range(1,4))
j=(range(2,5),(3,3),(3,3),(3,3),(3,3),(0,3),(1,2))
k=(end,(0,3),(0,2),(0,1),(0,2),(0,3),end)
l=((0,0),(0,0),(0,0),(0,0),(0,0),(0,0),range(5))
m=(end,(0,1,3,4),(0,2,4),(0,2,4),end,end,end)
n=(end,end,(0,1,4),(0,2,4),(0,3,4),end,end)
o=((1,2,3),end,end,end,end,end,(1,2,3))
p=(range(4),end,end,range(4),(0,0),(0,0),(0,0))
q=((1,2,3),end,end,end,(0,2,4),(0,3),(12,4))
r=(range(4),end,end,range(4),(0,2),(0,3),end)
s=(range(1,5),(0,0),(0,0),(1,2,3),(4,4),(4,4),range(4))
t=(range(5),(2,2),(2,2),(2,2),(2,2),(2,2),(2,2))
u=(end,end,end,end,end,end,(1,2,3))
v=(end,end,end,end,(1,3),(1,3),(2,2))
w=(end,end,end,(0,2,4),(0,2,4),(0,2,4),(1,3))
x=(end,end,(1,3),(2,2),(1,3),end,end)
y=(end,end,(1,3),(2,2),(2,2),(2,2),(2,2))
z=(range(5),(4,4),(3,3),(2,2),(1,1),(0,0),range(5))







x1,y1,z1=mc.player.getPos()

message('how are you',x1,y1,z1)
