from turtle import*
tracer(0)
lt(90)
screensize(10000,10000)
r =35
for i in range(5):
    fd(8*r)
    rt(90)
    fd(11*r)
    rt(90)
up()
for x in range(-15,15):
    for y in range(-15,15):
        goto(x*r,y*r)
        dot(3,'red')
done()
#108