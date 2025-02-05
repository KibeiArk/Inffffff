'''Определите площадь области пересечения фигур, ограниченных заданными
алгоритмом линиями.
'''
from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=25

for i in range(4):
    fd(19*r)
    rt(90)
    fd(30*r)
    rt(90)
up()
fd(2*r)
rt(90)
fd(8*r)
lt(90)
down()
for i in range(4):
    fd(93*r)
    rt(90)
    fd(97*r)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#374