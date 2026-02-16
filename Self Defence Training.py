# cook your dish here
def func(n,num):
    count = sum(1 for x in num if 10<=x<=60)
    return count
    
t=int(input())
for _ in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    print(func(n,num))
