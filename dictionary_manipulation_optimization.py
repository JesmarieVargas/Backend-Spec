# Task 1

def merge_dict(dict_1, dict_2):
    merged_dict = (dict_1 | dict_2)
    return merged_dict

dict_1 = {
'pie': 'apple',
'ice_cream': 'moose tracks',
'cobbler': 'peach',
'cake': None
}

dict_2 = {
    
'dinner': 'turkey',
'ice_cream': 'vanilla',
'appetizer': 'soup',
'cobbler': 'peach'
}

result = merge_dict(dict_1, dict_2)
print(result)

# The time complexity is O(n), where n is the total number of key-value pairs in both input dictionaries. The function iterates through each key-value pair in both dictionaries to merge them into a new dictionary. The space complexity is O(n), where n is the total number of key-value pairs in both input dictionaries. A new dictionary is created to store the merged key-value pairs, which can potentially contain all the key-value pairs from both input dictionaries.

# Task 2

def intersection(dict_1, dict_2):
    intersected = dict(dict_1.items() & dict_2.items())
    print(intersected)

intersection(dict_1, dict_2)

#The time complexity is O(min(n, m)), where n is the number of key-value pairs in dict_1 and m is the number of key-value pairs in dict_2. The function iterates through the smaller of the two dictionaries to find the intersection of key-value pairs.The space complexity is O(min(n, m)), as the intersected dictionary will contain at most min(n, m) key-value pairs.