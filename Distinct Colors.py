def func(n,num):
    return max(num)

t=int(input())
for _ in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    print(func(n,num))
