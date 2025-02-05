from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=20

for i in range(2):
    fd(24*r)
    rt(90)
    fd(16*r)
    rt(90)
up()
fd(10*r)
rt(90)
fd(8*r)
lt(90)
down()
for i in range(2):
    fd(15*r)
    rt(90)
    fd(28*r)
    rt(90)
up()
for x in range(-70,70):
    for y in range(-70,70):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#91