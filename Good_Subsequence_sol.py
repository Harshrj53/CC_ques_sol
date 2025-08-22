t=int(input())
for i in range(t):
    n=int(input())
    num=list(map(int,input().split()))
    l=[]
    for i in range(len(num)-1):
        if num[i] %2==0 and num[i+1]%2==0:
            i+=1
        elif num[i] %2!=0 and num[i+1]%2!=0:
            i+=1
        else:
            l.append(num[i])    
    print(len(l)+1)        
    
            
