def insertionsort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while temp <= list[j] and j >= 0:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = temp
    return list
list=eval(raw_input('Enter a list:'))
print insertionsort(list)
