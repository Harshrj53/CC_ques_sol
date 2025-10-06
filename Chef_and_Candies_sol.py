def candies(n,x):
    res_can=n-x
    if res_can<=0:
        return 0 
    else:
        if res_can%4==0:
            return res_can//4
        else:
            return (res_can//4)+1
     
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    print(candies(n,x))
