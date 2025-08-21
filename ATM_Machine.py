t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    num=list(map(int,input().split()))
    ans=[]
    for m in range(len(num)):
        if k>=num[m]:
            k=k-num[m]
            ans.append(1)
        else:
            ans.append(0)
    print(*ans,sep="")        
