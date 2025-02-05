'''Определите периметр пересечения фигур, ограниченного заданными алгоритмом
линиями.
'''
from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=25

for i in range(2):
    fd(5*r)
    rt(90)
    fd(15*r)
    rt(90)
up()
fd(-7 * r)
rt(90)
fd(12*r)
lt(90)
down()
for i in range(2):
    fd(65*r)
    rt(90)
    fd(120*r)
    rt(90)
up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#16