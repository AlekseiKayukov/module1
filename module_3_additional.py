def calculate_structure_sum(data_structure):
    total_sum = 0
    for element in data_structure:
        if isinstance(element, (int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (list,tuple,set)):
            total_sum += calculate_structure_sum(element)
        elif isinstance(element, dict):
            for key, value in element.items():
                total_sum += calculate_structure_sum([key,value])
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}]) #48
]

print(calculate_structure_sum(data_structure))