def func(n,arr):
    if '1' not in arr:
        return 0
    
    first=arr.index('1')
    last=arr.rindex('1')
    
    count=arr[first:last+1].count('0')
    return count
            
    
t=int(input())
for i in range(t):
    n=int(input())
    arr=input().strip() 
    print(func(n,arr))
