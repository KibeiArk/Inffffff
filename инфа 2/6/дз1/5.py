from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=20

for i in range(6):
    fd(25*r)
    rt(120)
up()
fd(20*r)
lt(90)
backward(5*r)
down()
for i in range(2):
    fd(20*r)
    lt(90)
    fd(10*r)
    lt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#66