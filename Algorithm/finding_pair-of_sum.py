from datetime import date


no_list=[1,2,3,8,9,9,10]
sum =12
flag=0
dic={}

for i,j in enumerate(no_list):
    keys= dic.keys()
    if j in keys:
         print(dic[j][1],j)
         print(dic[j][0],i)
         flag=1
         break
    else:
        if sum-j in keys:
            continue
        dic[sum-j]=(i,j)
if flag:
    print('answer present in array')
else:
    print('not present')
    
print(dic)
dic[-1]=(1,444)
print(dic[-1])
del dic

def fun(d:list,sum:int):
    d.sort()
    temp_sum=0
    # if sum<d[0]:
    #     return 0
    i,j=-1,len(d)
    while(i<j):
        i+=1
        j-=1
        temp_sum =d[i]+d[j]
        if temp_sum==sum:
            print(d[i],d[j])
            return "possible"
    if len(d)%2==1 and temp_sum<sum:
        j-=1
    elif len(d)%2==1 and temp_sum>sum:
        j+=1
    while(i!=len(d) and temp_sum<sum):
        i+=1
        j+=1
        if d[i]+d[j]==sum:
            print(d[i],d[j])
            return "possible"
    while(i!=-1 and temp_sum>sum):
        i-=1
        j-=1
        if d[i]+d[j]==sum:
            print(d[i],d[j])
            return "possible"
# wrong algorithm

fun([1,2,3,8,7,9,10],12)
1,2,3,7,8,9,10
    
    
        
        
        
    
    
    


    
    
         
    
    
