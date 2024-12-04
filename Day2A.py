# Link: [https://www.programiz.com/online-compiler/0iJCQuM1APWxo]
ans = 0
n = 1000
for i in range(0,n):
    input1 = input()
    list = input1.split(' ')
    list = [int(x) for x in list]
    w = 0
    l = 0
    x = 0
    y = -1
    for j in list:
        x = j
        if(y!=-1):
            if(abs(x-y)>3 or abs(x-y)<1):
                w=1
            if(l==0 and x<y):
                l=-1
            elif(l==0 and x>y):
                l=1
            if((l==1 and x<y) or (l==-1 and x>y)):
                w=1
        y = x
    if(w==0):
        ans +=1
print(ans)
