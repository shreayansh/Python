from collections import Counter
n=int(input())
for i in range(0,n):
    s=list(input().split(" "))
    a=Counter(s[0])
    b=Counter(s[1])
    if a==b:
        print("YES")
    else:
        print("NO")