def func(x):
    r=x%10
    if r==0:
        return 100-x
    elif r>=5:
        l=10-r 
        return 100-(x+l) 
    elif r<5:
        return 100-(x-r)
    
t=int(input())
for i in range(t):
    x=int(input())
    print(func(x))
