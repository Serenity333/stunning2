#code to create a fun pattern with a Turtle via Python

from turtle import *
color('black', 'red')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
