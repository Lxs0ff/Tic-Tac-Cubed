import turtle
import math
import random

#sub layers:
# 1- Normal Tic Tac Toe (Yellow Lines)
# 2- Smallest Tic Tac Toe (Blue Lines)

#Regions Dict:
# sub layer -> square (x-y) -> x range & y range

REGIONS = {
        "1-1":{
            "x":[1,3],
            "y":[1,3],
            "sublayer":{

            }
        },
        "2-1":{
            "x":[4,6],
            "y":[1,3],
            "sublayer":{

            }
        },
        "3-1":{
            "x":[7,9],
            "y":[1,3],
            "sublayer":{

            }
        },
        "1-2":{
            "x":[1,3],
            "y":[4,6],
            "sublayer":{

            }
        },
        "2-2":{
            "x":[4,6],
            "y":[4,6],
            "sublayer":{

            }
        },
        "3-2":{
            "x":[7,9],
            "y":[4,6],
            "sublayer":{

            }
        },
        "1-3":{
            "x":[1,3],
            "y":[7,9],
            "sublayer":{

            }
        },
        "2-3":{
            "x":[4,6],
            "y":[7,9],
            "sublayer":{

            }
        },
        "3-3":{
            "x":[7,9],
            "y":[7,9],
            "sublayer":{

        }
    },
}

map = [
    [],[],[],
    [],[],[],
    [],[],[],
]

SQUARES = 27
SCREEN_SIZE = 540
SQUARE_SIZE = SCREEN_SIZE/SQUARES


screen = turtle.Screen() 
screen.setup(SCREEN_SIZE,SCREEN_SIZE)

p1 = random.choice(["X","O"])
p2 = "X" if p1 == "O" else "O"

print(f"Player 1 is {p1}")
print(f"Player 2 is {p2}")

screen.title(f"Tic-Tac-Cubed (Turn of Player 1: {p1})")
screen.tracer(0,0)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed(100)

def map_(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def drawLine(pos1,pos2,x,y):
    #print(pos1)
    #print(pos2)
    turtle.penup()
    turtle.pencolor('blue')
    turtle.pensize(1)

    if pos1[0] == pos2[0]: #Horizontal     
        if x in [2,5,11,14,20,23]:
            turtle.pencolor('yellow')
            turtle.pensize(3)
        elif x in [8,17]:
            turtle.pencolor('orange')
            turtle.pensize(4)
        y = (pos1[1] * int(SQUARE_SIZE))
        y_ =(pos2[1] * int(SQUARE_SIZE))
        turtle.goto(pos1[0] - 250,y)
        turtle.pendown()
        turtle.goto(pos1[0] - 250,y_)
        turtle.penup()
    elif pos1[1] == pos2[1]: #Vertical
        if y in [2,5,11,14,20,23]:
            turtle.pencolor('yellow')
            turtle.pensize(3)
        elif y in [8,17]:
            turtle.pencolor('orange')
            turtle.pensize(4)
        x = (pos1[0] * int(SQUARE_SIZE))
        x_ = (pos2[0] * int(SQUARE_SIZE))
        turtle.goto(x,pos1[1]-250)
        turtle.pendown()
        turtle.goto(x_,pos1[1]-250)
        turtle.penup()
    turtle.pencolor('black')
    turtle.pensize(1)
    
def clickDetect(x,y):    
    row = math.ceil(map_(y,(-SQUARE_SIZE * SQUARES / 2,SQUARE_SIZE * SQUARES / 2),(27,0)))
    collumn = math.ceil(map_(x,(-SQUARE_SIZE * SQUARES / 2,SQUARE_SIZE * SQUARES / 2),(0,27)))
    print(f"Row: {row}")
    print(f"Collumn: {collumn}")

screen.onclick(clickDetect,1)
screen.cv._rootwindow.resizable(False, False)

def drawMap():
    for x in range(SQUARES):
        for y in range(SQUARES):
            drawLine((x*SQUARE_SIZE,250),(x*SQUARE_SIZE,-250),x,y)
    
    for y in range(SQUARES):
        for x in range(SQUARES):
            drawLine((-250,y*SQUARE_SIZE),(250,y*SQUARE_SIZE),x,y)

drawMap()
screen.mainloop()