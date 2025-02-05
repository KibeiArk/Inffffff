from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=34

rt(315)
for i in range(7):
    fd(16*r)
    rt(45)
    fd(8*r)
    rt(135)

up()
for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#77