
import time
import random

start_time = time.time()


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


a = [random.randrange(1, 1000000) for _ in range(0, 1000000)]
print(averagePivot(a))
print("--- %s seconds ---" % (time.time() - start_time))
