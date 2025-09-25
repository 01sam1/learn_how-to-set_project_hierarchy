import numpy.random as np
def generate_random_array():
    generator =np.default_rng()
    data =generator.integers(0,250,10)
    # print(data)
    return (data,data.size)
def insertion(array,size):
    for idx in range(1,size):
        j=idx-1
        ele =array[idx]
        # print(ele)
        while(j>-1 and ele<array[j]):
            array[j+1] =array[j]
            j-=1
        j+=1
        array[j] =ele
        # print(array)
    return array
for _ in range(0,10):
    data = generate_random_array()
    # print(data)
    ans =insertion(data[0],data[1])
    print(ans)