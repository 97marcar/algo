import random, time


def quickSort2(array): 
    less = []
    equal = []
    greater= []

    if not array:   # Basecase
        return array
    
    pivot = array[random.randint(0, len(array)-1)] # Choose random pivot
    for i in array: # Place each element in resp. stack
        if i < pivot:
            less.append(i)
        if i == pivot:
            equal.append(i)
        if i > pivot:
            greater.append(i)

    return quickSort2(less) + equal + quickSort2(greater) # Recursive call, sort the stacks

# Mackes Testelito
array = [2,7,3,8,1,6,4,7,3,8]
size = 1000000
array = [random.randrange(1, size) for _ in range(0, size)]
start_time=time.time()
print(quickSort2(array))

print("--- %s seconds ---" % (time.time() - start_time))
