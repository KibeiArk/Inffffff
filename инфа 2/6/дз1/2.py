from turtle import*

tracer(0)
lt(90)
screensize(10000,10000)
r=45

for i in range(2):
    rt(120)
    fd(7*r)
rt(300)
for i in range(2):
    rt(120)
    fd(7*r)
up()

for x in range(-50,50):
    for y in range(-50,50):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#42