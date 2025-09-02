t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x%3==0:
        if x > 3:
            print(x*y+(z*((x//3)-1)))
        else:
            print(x*y)
    else:
        print(x*y+(z*(x//3)))
