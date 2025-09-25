def make_structure(profit_list:list,weight_list:list):
    if profit_list.__len__()==weight_list.__len__():
        object_array=[{},]
        for index in enumerate(profit_list):
            temp_obj = obj_return(index[0]+1,weight_list[index[0]],index[1])
            object_array.append(temp_obj)  
        return object_array
    else:
        print('something went wrong')
        exit(0)
def obj_return(no,weight,profit):
    return {
        'no':no,
        'weight':weight,
        'profit':profit    
    }
def object_access(data:int):
    if data<1:
        print('something wrong at object_access function')
        exit(0)
    else:
        data_dict=object_array[data]
        return [*data_dict.values()]
        
def knapsack(no,weight):
    if(no<1 or weight<1):
        return 0
    object_entity=object_access(no)
    if(object_entity[1]>weight):
        knapsack(no-1,weight)
    else:
        temp=max(object_entity[2] +knapsack(no-1,weight-object_entity[1]),
        knapsack(no-1,weight))
        return temp
        
    
def main():
    profit_list=[10,12]
    weight_list=[1,12]

    object_array=make_structure(profit_list,weight_list)
    length=object_array.__len__()-1
    capacity=12
    print(knapsack(length,capacity))
    
list1=[1,2,3,4]
a,*b= list1
print(a,b)

a=10
b=20
a=(a,b)
print(a)
b,a=a
print(a,b)
def square(num):
    return num**2
list0=[i if i>6  else square(i) for i in range(0,10,2) ]
print(list0)

print('akshit' if 20>3 else "vatsal")












