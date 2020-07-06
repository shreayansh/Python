n=int(input())
s=input()
d=dict()
for i in range(1,n):
    b=s[i-1]+s[i]
    if(b not in d):
        d[b]=1
    else:
        d[b]=d.get(b)+1
m=""
c=0
for i in d.items():
    if(i[1]>c):
        m=i[0]
        c=i[1]
print(m)