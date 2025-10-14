def func(s1,s2,e1,e2):
    if s1!=e1 and s2 !=e2:
        return 1 
    else:
        return 2
    
t=int(input())
for i in range(t):
    s1,s2,e1,e2=map(int,input().split())
    print(func(s1,s2,e1,e2))
    
