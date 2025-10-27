def func(x,y,z):
    tp=10*x 
    if tp>y:
        return y*z 
    else:
        return tp*z
    
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    print(func(x,y,z))
