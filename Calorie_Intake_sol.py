x,y,z=map(int,input().split())
tc=y*z
if tc>x:
    print(-1)
else:
    print(x-tc)
