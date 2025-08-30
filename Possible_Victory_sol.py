r,o,c=map(int,input().split())
ro=20-o
mr=ro*6*6
if c+mr>r:
    print("Yes")
else:
    print("No")
