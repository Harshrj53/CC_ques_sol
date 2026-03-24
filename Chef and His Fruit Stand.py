# def func(a,b):
#     x=a//2
#     if x>b:
#         return b 
#     else:
#         return a

# t=int(input())
# for _ in range(t):
#     a,b=map(int,input().split())
#     print(func(a,b))

def func(a,b):
    return min(a//2,b)
    
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    print(func(a,b))
