def maxi_height(n,height):
    return max(height)
    
t=int(input())
for i in range(t):
    n=int(input())
    height=list(map(int,input().split())) 
    print(maxi_height(n,height))
