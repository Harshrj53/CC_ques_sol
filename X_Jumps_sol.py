t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    curr=0
    if x%y==0:
        print(x//y)
    else:
        a=x%y
        ans=x//y+a 
        print(ans)
