h=input()
m=input()
d={'1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','21':'twenty one','22':'twenty two','23':'twenty three','24':'twenty four','25':'twenty five','26':'twenty six','27':'twenty seven','28':'twenty eight','29':'twenty nine'}
if(m=="00"):
    print(d[h],"o' clock")
elif(m=="15"):
    print("quarter past",d[h])
elif(m=="30"):
    print("half past",d[h])
elif(m=="1"):
    print("one minute past",d[h])
elif(int(m)<30):
    print(d[m],"minutes past",d[h])   
else:
    x=str(60-int(m))
    y=str(int(h)+1)
    if(x=='15'):
        print("quarter to",d[y])
    else:
        print(d[x],"minutes to",d[y])