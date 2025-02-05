from turtle import*
tracer(0)
lt(90)
screensize(10000,10000)
r=20

for i in range(70):
    fd(8*r)
    rt(30)

up()
for x in range(-40,40):
    for y in range(-40,40):
        goto(x*r,y*r)
        dot(3,'red')
update()
done()
#8*12==96