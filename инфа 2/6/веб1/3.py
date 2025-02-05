'''Определите, сколько точек с целочисленными координатами будут находиться внутри пересечения фигур, 
ограниченных заданными алгоритмом линиями, не включая точки на границах этого пересечения.'''
from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r =40
for i in range(2):
    fd(7*r)
    rt(60)
    fd(12 *r)
    rt(120)
up()
fd(7*r)
rt(60)
down()
for i in range(2):
    fd(5*r)
    rt(120)
    fd(10 *r)
    rt(60)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#28