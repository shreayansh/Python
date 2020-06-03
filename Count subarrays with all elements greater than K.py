n=int(input())
a=list(map(int, input().split()))
k=int(input())
b=0
s=0
a.append(0)
for i in range(n+1):
    if(a[i]>k):
        b+=1
    else:
        r=b*(b+1)//2
        s+=r
        b=0
print(s)