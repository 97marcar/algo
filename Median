def pickMedianPivot(anArray):
    if (len(anArray) <= 1):
        return anArray

    first = anArray[0]
    middle = anArray[len(anArray)/2]
    last = anArray[len(anArray)-1]
    
    if(first<=last<=middle or middle<=last<=first):
        pivot = len(anArray)-1      #last

    elif(middle<=first<=last or last<=first<=middle):
        pivot = 0                   #first

    elif(last<=middle<=first or first<=middle<=last):
        pivot = len(anArray)/2      #middle

    elif(first == middle and middle == last):
        pivot = len(anArray)/2

    return anArray[pivot]
