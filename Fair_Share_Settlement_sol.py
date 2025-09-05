t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    ans1=n//(k +1)
    total_back=k*ans1
    ans2=(n-total_back)
    print(ans2)
