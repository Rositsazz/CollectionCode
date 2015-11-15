def take(n, list):
    new_list = []
    i = 0
    while i < n:
        new_list.append(list[i])
        i += 1
    return new_list


def sublist(list1, list2):
    if list1 == []:
        return True
    i = 0
    while i < len(list2):
        if take(len(list1), list2) == list1:
            return True
        i += 1
        list2 = list2[i:len(list2)]

    return False


print(sublist(["Python"], ["Python", "Django"]))
print(sublist(["Django", "Python"], ["Python", "Django"]))
print(sublist([], [1, 2, 3, 4]))
