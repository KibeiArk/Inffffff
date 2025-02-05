'''Определите площадь получившейся фигуры в квадратных единицах.
'''
from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=20

for i in range(8):
    for k in range(4):
        fd(5*r)
        rt(30)
        fd(6*r)
        rt(150)
    rt(60)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#90