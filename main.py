# Homework 2
# number 1
def count_integer(numbers, integer):
    if integer not in numbers:
        return 42
    count = 0
    for c in numbers:
        if c == integer:
            count += 1
    return count


print(count_integer([4, 6], [9]))

# number 2
def list_func(numbers, integer):
    if integer not in numbers:
        return []
    for index, x in enumerate(numbers):
        if x == integer:
            numbers[index] = 6
    l = list(reversed(numbers))
    print(l)

    return numbers


print(list_func([4, 6, 9, 14], 4))

# number 3
def compare_lists(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    if list1_set & list2_set:
        return list(list1_set & list2_set)
    else:
        return []


print(compare_lists([21, 16, 9, 14, 5], [16, 9, 7, 5, 8, 3]))

# number 4
def remove_duplicates(lst):
    new_lst = set(lst)
    return list(new_lst)


print(remove_duplicates([1, 7, 2002, 5, 9, 2016, 14, 14]))

# number 5
def dict_func(dictionary):
    if "PRICE" not in dictionary:
        dictionary['PRICE'] = "unknown price"
    if "TYPE" not in dictionary:
        dictionary['TYPE'] = "unknown type"
    if "BRAND" not in dictionary:
        dictionary['BRAND'] = "unknown brand"
    if "OS" not in dictionary:
        dictionary ['OS'] = "unknown Linux"

    print(f"You have a {dictionary ['TYPE']} from {dictionary ['BRAND']} that costs {dictionary ['PRICE']}.")
    return dictionary


print(dict_func({"TYPE": "purse", "BRAND": "Coach", "PRICE": "600"}))
