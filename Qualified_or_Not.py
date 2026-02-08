def func(n,x,y):
    if n>=2*x and n>=2*y:
        return "YES"
    else:
        return "NO"
    

n,x,y=map(int,input().split())
print(func(n,x,y))    
    
