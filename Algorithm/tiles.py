# str='aab'
# str =str.upper()

# s =set()
# def fun(i,ans):
#     if i<0:
#         return
#     temp_str=ans
#     ans+=str[i]
#     if str.isalpha():
#         # print(ans)
#         s.add(ans)
#     if len(ans)>1:
#         fun(i-1,ans[::-1])
#     if len(temp_str)>1:
#         fun(i-1,temp_str[::-1])
#     fun(i-1,ans)
#     fun(i-1,temp_str)
# fun(len(str)-1,'')
    
# str='aab'
# str =str.upper()
# s=set()


# for i in range(0,len(str)):
#     st=str[i]
#     for j in range(0,i):
#         for k in range(0,len(str)-i):
#             z=st
#             z+=str[(k+1)%len(str)]
#             s.add(z)
#     s.add(st)
    
str='*'*3
print(str)

