def func(n,a,b,attraction):
    min_dist=float('inf')
    for x , y in attraction:
        dist=abs(a-x) + abs(b-y)
        if dist<min_dist:
            min_dist=dist 
    return min_dist        
        
    
    
    
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    attraction=[tuple(map(int,input().split())) for _ in range(n)]
    print(func(n,a,b,attraction))
