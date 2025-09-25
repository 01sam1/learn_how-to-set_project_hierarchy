'''
* / 
+ -
**
()
'''

IP ='1+2*(4**2)+1'
priority ={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '**':3,
    '(':4,
    ')':4
}
operator =[]
digit=[]
for i in IP:
    if(i<'0' or i>'9'):
        operator.append(priority[i])
(operator.sort(reverse=False))
print(operator)
one =operator.pop()
for i in range(0,len(IP)):
    if(IP[i]==priority[one]):
        one =operator.pop()
        pass
    else:
        digit.append(IP[i])


