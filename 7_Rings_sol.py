t = int(input())

while t > 0:
    n, x = map(int, input().split())
    ans = str(n*x)
    l=len(ans)
    if l==5 and ans[0]!='0':
        print("Yes")
    else:
        print("No")
    
    t -= 1
