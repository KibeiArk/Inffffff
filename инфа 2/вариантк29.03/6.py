from turtle import*
tracer(0)
lt(90)
screensize(10000,10000)
r = 20
for i in range(9):
    fd(22*r)
    rt(90)
    fd(6*r)
    rt(90)
up()
fd(1*r)
rt(90)
fd(5*r)
lt(90)
down()
for i in range(9):
    fd(53*r)
    rt(90)
    fd(75*r)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
done()