def cal(x,y):
    ans = x*2+y*2 
    if ans>=1000:
        return "Yes"
    else:
        return "No"
x,y=map(int,input().split())
print(cal(x,y))
