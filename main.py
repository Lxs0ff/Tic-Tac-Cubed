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
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
        [
            [
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],

                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
                [
                    [
                    "","","",
                    "","","",
                    "","",""
                    ],
                    ""
                ],
            ],
            ""
    ],
]

SQUARES = 27
SCREEN_SIZE = 540
SQUARE_SIZE = SCREEN_SIZE/SQUARES

FONT1 = ('Arial', 15, 'bold')
FONT2 = ('Arial', 30, 'bold')
FONT3 = ('Arial', 40, 'bold')

screen = turtle.Screen() 
screen.setup(SCREEN_SIZE,SCREEN_SIZE)
screen.bgcolor(0,0,0)

p1 = random.choice(["X","O"])
p2 = "X" if p1 == "O" else "O"

turn = p1
freechose = True
freechose2 = False
freechose3 = False
rest = [0,0]

print(f"Player 1 is {p1}")
print(f"Player 2 is {p2}")

screen.title(f"Tic-Tac-Cubed (Turn of Player 1: {p1})")
screen.tracer(0,0)

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed(10)

def map_(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def drawLine(pos1,pos2,x,y):
    #print(pos1)
    #print(pos2)
    turtle.penup()
    turtle.pencolor('gray')
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

def getInfo(x,y):
    address=[0,0,0]
    bx = 0;by = 0
    if x in range(1,10) and y in range(1,10):address[0] = 1;bx=1;by=1
    elif x in range(10,19) and y in range(1,10):address[0] = 2;bx=2;by=1
    elif x in range(19,28) and y in range(1,10):address[0] = 3;bx=3;by=1
    elif x in range(1,10) and y in range(10,19):address[0] = 4;bx=1;by=2
    elif x in range(10,19) and y in range(10,19):address[0] = 5;bx=2;by=2
    elif x in range(19,28) and y in range(10,19):address[0] = 6;bx=3;by=2
    elif x in range(1,10) and y in range(19,28):address[0] = 7;bx=1;by=3
    elif x in range(10,19) and y in range(19,28):address[0] = 8;bx=2;by=3
    elif x in range(19,28) and y in range(19,28):address[0] = 9;bx=3;by=3
    mnx = ((bx-1)*9) if ((bx-1)*9) != 0 else 1
    mny = ((by-1)*9) if ((by-1)*9) != 0 else 1
    #print(f"Mod X: {mnx} \n bx: {bx}")
    #print(f"Mod Y: {mny} \n by: {by}")
    if mnx == mny == 1:
        if x in range(1,4) and y in range(1,4):address[1] = 1
        elif x in range(4,7) and y in range(1,4):address[1] = 2
        elif x in range(7,10) and y in range(1,4):address[1] = 3
        elif x in range(1,4) and y in range(4,7):address[1] = 4
        elif x in range(4,7) and y in range(4,7):address[1] = 5
        elif x in range(7,10) and y in range(4,7):address[1] = 6
        elif x in range(1,4) and y in range(7,10):address[1] = 7
        elif x in range(4,7) and y in range(7,10):address[1] = 8
        elif x in range(7,10) and y in range(7,10):address[1] = 9
    elif mny == 1:
        if x in range(1+mnx,4+mnx) and y in range(1,4):address[1] = 1
        elif x in range(4+mnx,7+mnx) and y in range(1,4):address[1] = 2
        elif x in range(7+mnx,10+mnx) and y in range(1,4):address[1] = 3
        elif x in range(1+mnx,3+mnx) and y in range(4,7):address[1] = 4
        elif x in range(4+mnx,7+mnx) and y in range(4,7):address[1] = 5
        elif x in range(7+mnx,10+mnx) and y in range(4,7):address[1] = 6
        elif x in range(1+mnx,3+mnx) and y in range(7,10):address[1] = 7
        elif x in range(4+mnx,7+mnx) and y in range(7,10):address[1] = 8
        elif x in range(7+mnx,10+mnx) and y in range(7,10):address[1] = 9
    elif mnx == 1:
        if x in range(1,4) and y in range(1+mny,4+mny):address[1] = 1
        elif x in range(4,7) and y in range(1+mny,4+mny):address[1] = 2
        elif x in range(7,10) and y in range(1+mny,4+mny):address[1] = 3
        elif x in range(1,4) and y in range(4+mny,7+mny):address[1] = 4
        elif x in range(4,7) and y in range(4+mny,7+mny):address[1] = 5
        elif x in range(7,10) and y in range(4+mny,7+mny):address[1] = 6
        elif x in range(1,4) and y in range(7+mny,10+mny):address[1] = 7
        elif x in range(4,7) and y in range(7+mny,10+mny):address[1] = 8
        elif x in range(7,10) and y in range(7+mny,10+mny):address[1] = 9
    else:
        if x in range(1+mnx,4+mnx) and y in range(1+mny,4+mny):address[1] = 1
        elif x in range(4+mnx,7+mnx) and y in range(1+mny,4+mny):address[1] = 2
        elif x in range(7+mnx,10+mnx) and y in range(1+mny,4+mny):address[1] = 3
        elif x in range(1+mnx,4+mnx) and y in range(4+mny,7+mny):address[1] = 4
        elif x in range(4+mnx,7+mnx) and y in range(4+mny,7+mny):address[1] = 5
        elif x in range(7+mnx,10+mnx) and y in range(4+mny,7+mny):address[1] = 6
        elif x in range(1+mnx,4+mnx) and y in range(7+mny,10+mny):address[1] = 7
        elif x in range(4+mnx,7+mnx) and y in range(7+mny,10+mny):address[1] = 8
        elif x in range(7+mnx,10+mnx) and y in range(7+mny,10+mny):address[1] = 9
    

    if x in [1,4,7,10,13,16,19,22,25] and y in [1,4,7,10,13,16,19,22,25]:
        address[2] = 1
    elif x in [2,5,8,11,14,17,20,23,26] and y in [1,4,7,10,13,16,19,22,25]:
        address[2] = 2
    elif x in [3,6,9,12,15,18,21,24,27] and y in [1,4,7,10,13,16,19,22,25]:
        address[2] = 3
    elif x in [1,4,7,10,13,16,19,22,25] and y in [2,5,8,11,14,17,20,23,26]:
        address[2] = 4
    elif x in [2,5,8,11,14,17,20,23,26] and y in [2,5,8,11,14,17,20,23,26]:
        address[2] = 5
    elif x in [3,6,9,12,15,18,21,24,27] and y in [2,5,8,11,14,17,20,23,26]:
        address[2] = 6
    elif x in [1,4,7,10,13,16,19,22,25] and y in [3,6,9,12,15,18,21,24,27]:
        address[2] = 7
    elif x in [2,5,8,11,14,17,20,23,26] and y in [3,6,9,12,15,18,21,24,27]:
        address[2] = 8
    elif x in [3,6,9,12,15,18,21,24,27] and y in [3,6,9,12,15,18,21,24,27]:
        address[2] = 9
    address[0] = address[0]-1
    address[1] = address[1]-1
    address[2] = address[2]-1
    return address

def TextAt(row,collumn,text:str,color,layer):
    x=y=0
    if layer == 1:
        x = -250+(collumn * int(SQUARE_SIZE)-36)
        y = 250-(row * int(SQUARE_SIZE)-17)
    elif layer == 2:
        row+=1
        collumn+=1
        if row in [1,2,3]:
            if collumn in range(1,4):y=30;x=(collumn*60) - 60
            elif collumn in range(4,7):y=90;x=((collumn-3)*60) - 60
            elif collumn in range(7,10):y=150;x=((collumn-6)*60) - 60
        elif row in [4,5,6]:
            if collumn in range(1,4):y=240;x=(collumn*60) - 60
            elif collumn in range(4,7):y=300;x=((collumn-3)*60) - 60
            elif collumn in range(7,10):y=360;x=((collumn-6)*60) - 60
        elif row in [7,8,9]:
            if collumn in range(1,4):y=420;x=(collumn*60) - 60
            elif collumn in range(4,7):y=480;x=((collumn-3)*60) - 60
            elif collumn in range(7,10):y=540;x=((collumn-6)*60) - 60
        x = -250+x
        y = 250-y
        print(f"Text Pos : ({x},{y})")
    elif layer == 3:
        x = y = 1.5*SQUARE_SIZE
        print(f"Text Pos : ({x},{y})")
    elif layer == 4:
        x = collumn
        y = row
    turtle.teleport(x,y,fill_gap=False)
    turtle.pencolor(color)
    if layer == 4:
        turtle.write(text,font=FONT3)
    if layer == 3:
        turtle.write(text,font=FONT3)
    elif layer == 2:
        turtle.write(text,font=FONT2)
    else:
        turtle.write(text,font=FONT1)

def checkWin(addr,layer):
    board = []
    for i in range(9):
        if layer == 3:
            board.append(map[i][1])
        elif layer == 2:
            board.append(map[addr[0]][0][i][1])
        elif layer == 1:
            board.append(map[addr[0]][0][addr[1]][0][i])
    for i in range(3):
        if board[0+(i)] == board[3+i] == board[6+i] and board[0+i] in ["X","O"]:
            if layer == 3:
                screen.clear()
                TextAt(0,0,f"{board[0+i]} won the game!","White",4)
                screen.exitonclick()
            elif layer == 2:
                print(f"Layer 2 win by {board[0+i]}")
                map[addr[0]][1] = board[0+i]
                TextAt(addr[0],addr[1],board[0+i],"blue",3)
                checkWin(addr,3)
            elif layer == 1:
                print(f"Layer 1 win by {board[0+i]}")
                map[addr[0]][0][addr[1]][1] = board[0+i]
                TextAt(addr[0],addr[1],board[0+i],"red",2)
                checkWin(addr,2)
        i = i*3
        if board[0+i] == board[1+i] == board[2+i] and board[0+i] in ["X","O"]:
            if layer == 3:
                screen.clear()
                TextAt(0,0,f"{board[0+i]} won the game!","White",4)
                screen.exitonclick()
            elif layer == 2:
                print(f"Layer 2 win by {board[0+i]}")
                map[addr[0]][1] = board[0+i]
                TextAt(addr[0],addr[1],board[0+i],"blue",3)
                checkWin(addr,3)
            elif layer == 1:
                print(f"Layer 1 win by {board[0+i]}")
                map[addr[0]][0][addr[1]][1] = board[0+i]
                TextAt(addr[0],addr[1],board[0+i],"red",2)
                checkWin(addr,2)
    if board[0] == board[4] == board[8] and board[0] in ["X","O"]:
            if layer == 3:
                screen.clear()
                TextAt(0,0,f"{board[0]} won the game!","White",4)
                screen.exitonclick()
            elif layer == 2:
                print(f"Layer 2 win by {board[0]}")
                map[addr[0]][1] = board[0]
                TextAt(addr[0],addr[1],board[0],"blue",3)
                checkWin(addr,3)
            elif layer == 1:
                print(f"Layer 1 win by {board[0]}")
                map[addr[0]][0][addr[1]][1] = board[0]
                TextAt(addr[0],addr[1],board[0],"red",2)
                checkWin(addr,2)
    elif board[2] == board[4] == board[6] and board[2] in ["X","O"]:
            if layer == 3:
                screen.clear()
                TextAt(0,0,f"{board[2]} won the game!","White",4)
                screen.exitonclick()
            elif layer == 2:
                print(f"Layer 2 win by {board[2]}")
                map[addr[0]][1] = board[2]
                TextAt(addr[0],addr[1],board[2],"blue",3)
                checkWin(addr,3)
            elif layer == 1:
                print(f"Layer 1 win by {board[2]}")
                map[addr[0]][0][addr[1]][1] = board[2]
                TextAt(addr[0],addr[1],board[2],"red",2)
                checkWin(addr,2)

def clickDetect(x,y):
    global turn,p1,p2,freechose,rest
    y_ = math.ceil(map_(y,(-SQUARE_SIZE * SQUARES / 2,SQUARE_SIZE * SQUARES / 2),(27,0)))
    x_ = math.ceil(map_(x,(-SQUARE_SIZE * SQUARES / 2,SQUARE_SIZE * SQUARES / 2),(0,27)))
    print(f"X: {x_}")
    print(f"Y: {y_}")
    addr = getInfo(x_,y_)
    print(f"Layer 3: {addr[0]}")
    print(f"Layer 2: {addr[1]}")
    print(f"Layer 1: {addr[2]}")
    #print(map[addr[0]][0][addr[1]][0][addr[2]])
    if map[addr[0]][0][addr[1]][0][addr[2]] == "" and map[addr[0]][0][addr[1]][1] == "" and map[addr[0]][1] == "":
        if addr[0] == rest[0] and addr[1] == rest[1] or freechose:
            map[addr[0]][0][addr[1]][0][addr[2]] = turn
            checkWin(addr,1)
            if freechose:
                freechose = False
                rest[0] = addr[0]
            if map[addr[0]][0][addr[2]][1] == "":
                rest[1] = addr[2]
            else: 
                print("You need to play in the same square, because this one is occupied!")
            TextAt(y_,x_,turn,"white",1)
            turn = p2 if turn == p1 else p1
            if turn == p2:screen.title(f"Tic-Tac-Cubed (Turn of Player 2: {p2})")
            else:screen.title(f"Tic-Tac-Cubed (Turn of Player 1: {p1})")
            turtle.clear()
            drawMap()
            drawBoard()
        else:      
            print(f"Not within restrictions!")
    else:
        print(f"You can't place your {turn} here!")

screen.onclick(clickDetect,1)
screen.cv._rootwindow.resizable(False, False)
def drawSquare(x,y,width,color):
    turtle.penup()
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+width,y)
    turtle.goto(x+width,y-width)
    turtle.goto(x,y-width)
    turtle.goto(x,y)
    turtle.end_fill()

def drawMap():
    if rest != [0,0]:
        if rest[0] in range(1,4):
            print("Showing region")
            drawSquare(rest[0]*180,0,180,"red")
    for x in range(SQUARES):
        for y in range(SQUARES):
            drawLine((x*SQUARE_SIZE,250),(x*SQUARE_SIZE,-250),x,y)
    for y in range(SQUARES):
        for x in range(SQUARES):
            drawLine((-250,y*SQUARE_SIZE),(250,y*SQUARE_SIZE),x,y)

def drawBoard():
    for x in range(0,28):
        for y in range(0,28):
            addr = getInfo(x,y)
            TextAt(y,x,map[addr[0]][0][addr[1]][0][addr[2]],"white",1)
drawMap()
while True:
    screen.update()
