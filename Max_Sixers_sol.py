x=int(input())
if x%6==0:
    print(x//6)
else:
    a=x%6
    x=x-a
    print(x//6)
