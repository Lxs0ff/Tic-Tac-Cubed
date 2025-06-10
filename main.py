import turtle


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

def map_(val,src,dst):
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

def clickDetect(x,y):    
    row = map_(y,(-BOX_SIZE * BOXES / 2,BOX_SIZE * BOXES / 2),(0,10))
    collumn = map_(x,(-BOX_SIZE * BOXES / 2,BOX_SIZE * BOXES / 2),(0,10))