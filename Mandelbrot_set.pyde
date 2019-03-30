X=1000
Y=1000

def setup():
    size(X,Y)
    background(0)

    for x in range(width):
        for y in range(height):
            
            a=map(x,0,width,-2,2)
            b=map(y,0,height,-2,2)
            c=complex(a,b)
            C=c
            n=0            
            while(n<100):
               c=f(c,C)
               n+=1
               if abs(c)>16:
                   break            
            if n==100:
                stroke(255)
                point(x,y)
            else:
                stroke(map(n,0,100,0,255))
                point(x,y)
    stroke(255)
    line(0,height/2,width,height/2)
    line(width/2,0,width/2,height)
def f(z,c):
    return z**2+c
    
def draw():
    point(0,0)
