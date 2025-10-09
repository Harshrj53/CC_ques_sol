def func(x,y):
    return min(x,y)
    
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    print(func(x,y)) 
