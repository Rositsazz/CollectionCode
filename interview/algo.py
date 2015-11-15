def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp


a = [1, 4, 2, 8, 66, 3]
bubble(a)
print(a)


arr = [2, 5, 1, 8, 4, 9, 2, 8]


def merge(array):

    if len(array) < 2:
        return array

    result = []
    middle = len(array)//2

    left = merge(array[:middle])
    right = merge(array[middle:])

    while (len(left) > 0) and (len(right) > 0):
            if left[0] < right[0]:
                number = left.pop(0)
                result.append(number)
            else:
                number = right.pop(0)
                result.append(number)

    result.extend(left+right)
    return result

print(merge(arr))
