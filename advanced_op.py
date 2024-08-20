#Advanced Operations on Python Lists

# Task1

def list_squares(n):
    return [i**2 for i in range(1, n+1)]

print(list_squares(10))


# Task2

def mergeList():
    list1 = [2, 4, 6, 8, 10]
    list2 = [12, 14, 16, 18, 20]
    list3 = list1 + list2

    print(list3)

mergeList()

