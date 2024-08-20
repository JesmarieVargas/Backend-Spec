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

# Task 2

def intersection(dict_1, dict_2):
    intersected = dict(dict_1.items() & dict_2.items())
    print(intersected)

intersection(dict_1, dict_2)

