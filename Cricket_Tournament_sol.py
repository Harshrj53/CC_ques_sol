t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    if n-1>=m:
        print("Yes")
    else:
        print("No")
