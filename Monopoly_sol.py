def func(p,q,r,s):
    if p>q+r+s:
        return "YES"
    elif q>p+r+s:
        return "YES"
    elif r>p+q+s:
        return "YES"
    elif s>p+q+r:
        return "YES"
    else:
        return "NO"
    
    
t=int(input())
for i in range(t):
    p,q,r,s=map(int,input().split())
    print(func(p,q,r,s))
