import random

# Task 1

list1 = [1, 3, 4, 8, 14, 17, 32, 41, 44, 45]
list2 = [6, 13, 15, 17, 18, 34, 41, 40, 44, 46]
list3 = [18, 22, 23, 26, 27, 34, 36, 37, 44, 47]
list4 = [3, 7, 8, 16, 45, 31, 20, 22, 14, 23]

def ascendingOrder(num):
    list5 = num.copy()
    list6 = num.copy()

    n = len(list5)
    for i in range(n):
        for j in range(n - 1):
            if list5[j] > list5[i]:
                list5[j], list5[i] = list5[i], list5[j]
    if list6 == list5:
        print("This list is in ascending order.")
    else:
        print("This list is not in ascending order.")

ascendingOrder(list1)
ascendingOrder(list2)
ascendingOrder(list3)
ascendingOrder(list4)


# Task 2

list1 = [9, 6, 3, 25, 21, 8, 23, 1, 17, 14]
list2 = [37, 39, 41, 29, 9, 25, 43, 21, 3, 42]
list3 = [24, 8, 10, 22, 45, 34, 28, 39, 3, 32]
list4 = [15, 21, 8, 32, 46, 44, 37, 20, 27, 22]
list5 = [11, 38, 4, 28, 24, 41, 15, 10, 45, 14]


def listSorter(num):
    list = num

    n = len(list)
    for i in range(n):
        for j in range(n - 1):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
    print(list)

listSorter(list1)
listSorter(list2)
listSorter(list3)
listSorter(list4)
listSorter(list5)