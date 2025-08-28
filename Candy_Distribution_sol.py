t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    ans=n//m
    if n%m==0 and ans %2==0 :
        print("Yes")
    else:
        print("No")
