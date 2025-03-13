from turtle import*
tracer(0)
lt(90)
screensize(10000,10000)
r =30

for i in range(2):
    fd(13*r)
    rt(90)
    fd(18*r)
    rt(90)
up()
fd(5*r)
rt(90)
fd(9*r)
lt(90)
down()
for i in range(2):
    fd(11*r)
    rt(90)
    fd(7*r)
    rt(90)
up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
done()
#72