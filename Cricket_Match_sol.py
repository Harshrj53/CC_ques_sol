def match(N,M):
    if M*6*6>=N:
        return "YES"
    else:
        return "NO"
    
t=int(input())
for i in range(t):
    N,M =map(int,input().split())
    print(match(N,M))
