def func(n,k,p,num):
    tallest=max(num)
    ved=k+tallest
    varun=p+(sum(num)-tallest)
    
    if ved>varun:
        return "Ved"
    elif varun>ved:
        return "Varun"
    else:
        return "Equal"
    

t=int(input())
for _ in range(t):
    n,k,p=map(int,input().split())
    num=list(map(int,input().split()))
    print(func(n,k,p,num))    
