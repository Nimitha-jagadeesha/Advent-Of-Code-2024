#Link:  [https://www.programiz.com/online-compiler/6ZzqHjBpAcjJr]

ans = 0
n = 1000


def is_listValid(list):
   w = 0
   l = 0
   x = 0
   y = -1
   for j in list:
       x = j
       if(y!=-1):
           if(abs(x-y)>3 or abs(x-y)<1):
               w=1
               break
           if(l==0 and x<y):
               l=-1
           elif(l==0 and x>y):
               l=1
           if((l==1 and x<y) or (l==-1 and x>y)):
               w=1
               break
       y = x
   if(w==0):
       return True
   else:
       return False
      
for i in range(0,n):
   input1 = input()
   list = input1.split(' ')
   list = [int(x) for x in list]
   if is_listValid(list):
       ans+=1
       continue
   for x in range(0,len(list)):
       if(is_listValid(list[:x] + list[x+1:])):
           ans+=1
           break
print(ans)
