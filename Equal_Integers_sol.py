def func(x,y):
    if x<=y:
        return y-x
    d=x-y
    if d%2==0:
        return d//2
    else:
        return d//2+2
        
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(func(x,y))
    
    
