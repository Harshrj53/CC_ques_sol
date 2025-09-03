t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    ans=-1
    for c in range(1,11):
        if a+b+c==21:
            ans=c
            break
    print(ans)            
       
