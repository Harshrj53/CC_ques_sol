t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    x=arr[0]
    count=0
    for i in range(n):
        if arr[i]>=x:
            count+=1 
    print(count)        
    
        
