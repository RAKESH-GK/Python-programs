import math
x1=int(input("enter the value for x1:"))
x2=int(input("enter the value for x2:"))
y1=int(input("enter the value for y1:"))
y2=int(input("enter the value for y2:"))

distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print("distance between",(x1,y1),"and",(x2,y2),"is",distance)