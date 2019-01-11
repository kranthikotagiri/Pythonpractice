from turtle import Turtle
t = Turtle()
t.speed(0)

b = 180
for c in range(5):
    a = 100
    for i in range(143):
        t.circle(i, a)
        t.right(b)
        t.circle(i, a)
        t.right(b)
        t.circle(i, a)
        t.right(b)
        t.circle(i, a)
        t.right(b)
input('Press any key to continue...')