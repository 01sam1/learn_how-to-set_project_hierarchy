def findSum(data:list[int]):
    return sum(data,0)

# data =[-2,3,4,5,-10,-4,21,45,6]
data =[-2,1,-3,4,-1,2,1,-5,4]
print(sum(data))
length =len(data)

def main(d,i):
    if(i==length-1):
        return sum(d)
    i+=1 
    # sum1 =findSum(d+[data[i]])
    sum2=0
    sum1 =main(d+[data[i]],i)
    if(d==[]):
        # sum2 =findSum(d)
        sum2=main(d,i)
    # sum1 =findSum(sum1)
    # sum2 =findSum(sum2)
    temp=max(sum1,sum2)
    # print(sum1)
    return temp
    # if temp==sum1:
    #     return d+[data[i]]
    # return d
    
print(main([],-1))