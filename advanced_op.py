#Advanced Operations on Python Lists

# Task1

def list_squares(n):
    return [i**2 for i in range(1, n+1)]

print(list_squares(10))

#The time complexity is O(n) because it iterates through the range from 1 to n and calculates the square of each number. The space complexity is also O(n) because it creates a list of size n to store the squared values.


# Task2

def mergeList():
    list1 = [2, 4, 6, 8, 10]
    list2 = [12, 14, 16, 18, 20]
    list3 = list1 + list2

    print(list3)

mergeList()

#The time complexity is O(n), where n is the total number of elements in both lists. The function concatenates the two lists together, requiring it to iterate through each element in both lists once.The space complexity is O(n), as the new merged list will contain all the elements from both lists, resulting in a new list of size n.

