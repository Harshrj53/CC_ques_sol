t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    chocolate=x*2
    candy=y*5
    if chocolate>candy:
        print("Chocolate")
    elif candy > chocolate:
        print("Candy")
    else:
        print("Either")
    
