def commonElements (list1, list2):
    finalList = []
    for i in list1:
        if i in list2 and i not in finalList:
            list2.append(i)
    return finalList

def binaryRepresent (num):
    binary = 0
    while(num/2 != 1):
        binary = num / 2 * 10
        num = num / 2
    if num % 2 = 1:
        binary = binary + 1
    return binary