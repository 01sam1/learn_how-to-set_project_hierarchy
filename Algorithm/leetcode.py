pattern='DDD'
# ans='123456789'

ans=[i+1 for i in range(0,len(pattern)+1)] #contains numbers
print(ans)

def fun(i):
    if i<0:
        return 1
    var=pattern[i]
    if var=='I':
        if ans[i]<=ans[i+1]:
            return
        else:
            temp =ans[i+1]
            ans[i+1]=ans[i]
            ans[i]=temp
            fun(i-1)
    else :
        if ans[i]>ans[i+1]:
            return
        else:
            temp =ans[i+1]
            ans[i+1]=ans[i]
            ans[i]=temp
            fun(i-1)
for i in range(0,len(pattern)):
    fun(i)
print(ans)
    
    
    