list_of_numbers = [1, 3, 2, 5, 4]

def findMaxInList(list_of_numbers):
    Max = list_of_numbers[0]
    for i in list_of_numbers:
        if i > Max:
            Max = i
    return Max

print(findMaxInList(list_of_numbers))
    