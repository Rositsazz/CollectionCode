def selection(lst):

    for i in range(len(lst)):
        mini = min(lst[i:])
        min_index = lst[i:].index(mini)
        lst[i + min_index] = lst[i]
        lst[i] = mini
    return lst

a = [7, 3, 9, 11, 2, 5]
selection(a)
print(a)
