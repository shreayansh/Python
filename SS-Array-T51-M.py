def factors(n):
    r=0
    for i in range(1,n+1):
        if(n%i==0):
            r+=1
    return r
t=int(input())
while(t):
    n=int(input())
    sum=1
    s=list(map(int, input().split()))
    for i in range(0,n):
        sum*=s[i]
    print(factors(sum))
    t=t-1