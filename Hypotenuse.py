import math
x,y=map(int,input().split())
z = math.pow(x, 2)+math.pow(y, 2)
m = math.sqrt(z)
print('{:.2f}'.format(m))
