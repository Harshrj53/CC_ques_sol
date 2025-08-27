t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    tw=y*2
    if x//tw > 0:
        print(x//tw)
    else:
        print(0)
