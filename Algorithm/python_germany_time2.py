# with open('temp.txt','w') as f:
#     f.write('hello my name is vatsal')

# with open('temp.txt','a') as f:
#     print(f.tell())
#     f.write('\n\nhello my name is sam')

for i in range(0,7):
    temp=''
    for k in range(0,i):
        temp+='  '
    print(temp,end='')
    for j in range(0,7):
        
            
        print('*',end=' ')
    print('')

li=[]
import math
# k,j=0,7
n=7
for i in range(0,n):
    if i>math.floor(n/2):
        print(li.pop())
        continue
        
    str=''
    # for k in range(0,i):
    #         str+=' '
    for j in range(0,n):
        if i==0:
            str+='* '
            continue
        if i!=0 and j<i:
            str+='  '
            continue
        if j==i or j==n-1-i:
            str+='* '
            continue
        else:
            str+='  '
    print(str)
    if i!=math.floor(n/2):
        li.append(str)
    
  
    
