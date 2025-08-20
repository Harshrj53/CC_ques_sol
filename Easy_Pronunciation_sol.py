t=int(input())
for i in range(t):
    n=int(input())
    s=list(input())
    vol={"a","e","i","o","u"}
    found=False
    for i in range(n-3):
        if s[i] not in vol and s[i+1] not in vol and s[i+2] not in vol and s[i+3] not in vol:
            found=True
            break
    if found:
        print("No")
    else:
        print("Yes")
    
            
            
        
