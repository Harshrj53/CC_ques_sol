t=int(input())
for i in range(t):
    n,k,m=map(int,input().split())
    total=k*m
    if n%total==0:
        print(n//total)
    else:
        print((n//total)+1)
