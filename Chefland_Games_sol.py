t=int(input())
for i in range(t):
    arr=list(map(int,input().split()))
    r1,r2,r3,r4=arr
    ans="IN"
    for i in range(len(arr)):
        if arr[i]==1:
            ans="OUT"
            break
    print(ans)        
    
