from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
k=20
for i in range(2):
    fd(10*k)
    rt(90)
    fd(20*k)
    rt(90)
up()
fd(3*k)
rt(90)
fd(5*k)
lt(90)
down()
for i in range(2):
    fd(70*k)
    rt(90)
    fd(80*k)
    rt(90)

up()
for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,'red')
update()
done()
#128