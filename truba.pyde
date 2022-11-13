x = 1000
def setup():
    size(600,400)
def draw():
    global x,c,v,b
    ellipse(300,200,x,x)
    x -=1
    
