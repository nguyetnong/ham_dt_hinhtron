import turtle
import math

def hinhtron(r:float):
    turtle.circle(r)
    turtle.done()
    
    
def chuvi_hinhtron(r:float,goc:float)->float:
    chuvi= 2 * math.pi * r
    chuvigoc=chuvi*goc/360
    return chuvigoc
def tinhdientich(r:float,goc:float)->float:
    dientich=math.pi * r * r
    return dientich
               
r=float(input("nhap bankinh: "))
hinhtron(r)
s=tinhdientich(r,360)
print(s)

    
    
    
    