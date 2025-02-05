'''Определите длину замкнутой ломаной, которая является границей объединения
фигур, очерченных заданными алгоритмом линиями. В ответе укажите только
число. Единицы измерения указывать не нужно'''
from turtle import*
tracer(0)
lt(90)
screensize(10000,10000)
r =20
for i in range(3):
    down()
    for j in range(2):
        fd(7*r)
        rt(90)
        fd(7*r)
        rt(90)
    up()
    fd(6*r)
    rt(90)
    fd(6*r)
    lt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#76