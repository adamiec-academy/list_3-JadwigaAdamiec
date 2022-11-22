from turtle import forward, left, right, penup, pendown, speed

speed ='fastest'

def one_thing(n): 
  for j in range(5):
    for i in range(4):
      forward(n)
      left(90)
    left(90)
    forward(n)
    right(90)
    forward(n/10)
    n=n-2*(n/10)


def all_things(n):
  for k in range(6):
    one_thing(n)
    penup()
    right(90)
    forward(168)
    left(90)
    forward(33)
    right(60)
    pendown()
  
  

all_things(50)
