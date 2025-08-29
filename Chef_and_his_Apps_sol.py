t=int(input())
for i in range(t):
    s,x,y,z=map(int,input().split())
    ans1=z+x
    ans2=z+y
    ans3=z+x+y
    ans4=z
    if ans3 <=s:
        print(0)
    elif ans1 <=s:
        print(1)
    elif ans2 <=s:
        print(1)
    elif ans4 <=s:
        print(2)
    
