import random
"""
Authors:
Marcus Carlsson
Aron Strandberg
Robin Vernström Persson
"""
def pickMedianPivot(lst):
    if (len(lst) <= 1):
        return lst

    first = lst[0]
    middle = lst[len(lst)/2]
    last = lst[len(lst)-1]

    if(first<=last<=middle or middle<=last<=first):
        pivot = len(lst)-1      #last

    elif(middle<=first<=last or last<=first<=middle):
        pivot = 0                   #first

    elif(last<=middle<=first or first<=middle<=last):
        pivot = len(lst)/2      #middle

    elif(first == middle and middle == last):
        pivot = len(lst)/2

    return lst[pivot]

def pickAveragePivot(lst):
    tot = 0

    for i in range(len(lst)):
        tot += lst[i]

    avg = tot / len(lst)
    closest = 0
    diff = abs(lst[0] - avg)

    for j in range(len(lst)):
        #check if equal to finish quicker
        if(lst[j] == avg):
            return(lst[j])

        currentDiff = abs(lst[j] - avg)

        #check if current element is closer to average
        if currentDiff <= diff:
            diff = currentDiff
            closest = lst[j]
    return(closest)

def pickRandomPivot(lst):
    return (lst[random.randint(0, len(lst)-1)])


def quickSort(lst, pickPivot):
    left = []
    right = []
    pivots = []
    if(len(lst) <= 1):
        return(lst)
    else:
        pivot = pickPivot(lst)
        for n in range(len(lst)):
            if lst[n] < pivot:
                left.append(lst[n])
            elif lst[n] > pivot:
                right.append(lst[n])
            else:
                pivots.append(lst[n])
    return (quickSort(left, pickPivot) + pivots + quickSort(right, pickPivot))
