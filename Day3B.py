#(B) Link (https://www.programiz.com/online-compiler/8XKtgDLbLQU16) 

import re
text = ''
ans = 0
while True:
   try:
       line = input()
       text = text + line
   except EOFError:
       break


pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, text)
skip = 0
for ele in matches:
   index = 4
   first_int = 0
   if(ele == "don't()"):
       skip = 1
       continue
   elif(ele == "do()"):
       skip = 0
       continue
   if skip == 1:
       continue
   while ele[index]!=',':
       first_int = first_int*10 + int(ele[index])
       index +=1
   index +=1
   second_int = 0
   while ele[index]!=')':
       second_int = second_int*10 + int(ele[index])
       index +=1
   ans = ans + (first_int * second_int)
print(ans)
