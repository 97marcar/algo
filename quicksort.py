import time
import random


def averagePivot(lista):
    tot = 0

    for i in range(len(lista)):
        tot += lista[i]

    avg = tot / len(lista)
    closest = 0
    diff = abs(lista[0] - avg)

    for j in range(len(lista)):
        #check if equal to finish quicker
        if(lista[j] == avg):
            return(lista[j])

        currentDiff = abs(lista[j] - avg)

        #check if current element is closer to average
        if currentDiff <= diff:
            diff = currentDiff
            closest = lista[j]
    return(closest)


def quickSort(lista):
    left = []
    right = []
    pivots = []
    if(len(lista) <= 1):
        return(lista)
    else:
        pivot = averagePivot(lista)
        for n in range(len(lista)):
            if lista[n] < pivot:
                left.append(lista[n])
            elif lista[n] > pivot:
                right.append(lista[n])
            else:
                pivots.append(lista[n])
    return (quickSort(left) + pivots + quickSort(right))



size = 20000000
#b = [2,7,3,8,1,6,4,7,3,8]
#b = list(range(1,size))
#b = [random.randrange(1, 10) for _ in range(0, size)]+[250,100000000]
b = [random.randrange(1, size) for _ in range(0, size)]
print("boom")

start_time = time.time()
b = quickSort(b)
#c = quickSort(b)
print("--- %s seconds ---" % (time.time() - start_time))
#print(b)
