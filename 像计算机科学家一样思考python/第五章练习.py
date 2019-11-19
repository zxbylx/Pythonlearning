# -*- coding: utf-8 -*-
from swampy.TurtleWorld import *
import math

world=TurtleWorld()
bob=Turtle()
print(bob)
bob.delay=0.01

#def draw(t,length,n):
#    if n==0:
#        return
#    angle=50
#    fd(t,length*n)
#    lt(t,angle)
#    draw(t,length,n-1)
#    rt(t,2*angle)
#    draw(t,length,n-1)
#    lt(t,angle)
#    bk(t,length*n)
#    
#draw(bob,50,4)

def koch(t,x):
    if x<3:
        return
    else:
        fd(t,x/3)
        lt(t,60)
        fd(t,x/3)
        rt(t,120)
        fd(t,x/3)
        lt(t,60)
        fd(t,x/3)
        
def snowflake(t,n):
    for i in range(3):
        koch(t,n)
        rt(t,120)
snowflake(bob,300)