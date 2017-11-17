

import random, time


def quickSort2(array):
    less = []
    equal = []
    greater= []

    if not array:   # Basecase
        return array

    pivot = array[random.randint(0, len(array)-1)]
    for i in array:
        if i < pivot:
            less.append(i)
        if i == pivot:
            equal.append(i)
        if i > pivot:
            greater.append(i)

    return quickSort2(less) + equal + quickSort2(greater) # Recursive call, sort the stacks

size = 20000000

#array = [2,7,3,8,1,6,4,7,3,8]
array = [random.randrange(1, size) for _ in range(0, size)]
#array = list(range(1,size))
#array = [random.randrange(1, 10) for _ in range(0, size)]+[250,100000000]
print("boom")

start_time=time.time()
a = quickSort2(array)
#quickSort2(a)
print("--- %s seconds ---" % (time.time() - start_time))
