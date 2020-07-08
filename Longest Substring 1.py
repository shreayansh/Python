for i in range(int(input())):
    a,b=list(map(int,input().split()))
    s=input()
    h=set()
    a=[]
    ma=0
    for i in s:
        h.add(i)
        a.append(i)
        if(len(h)==b):
            if(ma<len(a)):
                ma=len(a)
            
    mx = ma
    h=set()
    a=[]
    ma=0
    for i in s[::-1]:
        h.add(i)
        a.append(i)
        if(len(h)==b):
            ma=len(a)
            if(ma>mx):
                mx=ma
    print(mx)