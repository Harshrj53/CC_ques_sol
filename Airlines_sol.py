t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    curr=n-100*x
    need = 0 if curr <=0 else (curr+99)//100
    print(need)
        
