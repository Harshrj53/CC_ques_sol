def best_movie(n):
    l=[]
    for _ in range(n):
        a,b=map(int,input().split())
        
        if a>=7:
            l.append(b)
    if (l):
        return min(l)
        
    else:
        return -1

t=int(input())
for i in range(t):
    n=int(input())
    
    print(best_movie(n))
