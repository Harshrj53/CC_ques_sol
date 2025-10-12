def dna(n,s):
    for i in range(n):
        if s[i]=='A':
            s[i]='T'
        elif s[i]=='T':
            s[i]='A'
        elif s[i]=='C':
            s[i]='G'
        elif s[i]=='G':
            s[i]='C'
    return "".join(s)  
            
t=int(input())
for i in range(t):
    n=int(input())
    s=list(input().strip())
    print(dna(n,s))
