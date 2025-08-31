t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    
    even_card=n//2
    odd_card=n-even_card
    
    if x%2==0:
        print(even_card-1)
    else:
        print(odd_card-1)
