# t=int(input())
# for i in range(t):
#     n,x=map(int,input().split())
#     if n%6==0:
#         l=n//6
#         print(l*x)
#     else:
#         l=(n//6)+1
#         print(l*x)
        
def subs(n,x):
    if n%6==0:
        l=n//6
        return l*x 
    else:
        l=(n//6)+1
        return l*x 
t=int(input()) 
for i in range(t):
    n,x=map(int,input().split())
    print(subs(n,x))
