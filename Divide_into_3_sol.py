n=int(input())
d=n%3
if d==0:
    print(0)
else:
    min=n//3
    max=min+1
    print(max-min)    
    
