def bubble_sort(list_to_sort):

    n = len(list_to_sort)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if list_to_sort[j] > list_to_sort[j + 1]:

                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp

    return list_to_sort


def validated_bubble_sort(list_to_sort):

    if len(list_to_sort) == 0:
        return "Error: The list is empty"

    for element in list_to_sort:

        if not isinstance(element, (int, float)):
            return "Error: The list contains non-numeric elements"

    return bubble_sort(list_to_sort)

print(validated_bubble_sort([5, 3, 1, 4, 2]))

print(validated_bubble_sort([5, "hello", 2]))

print(validated_bubble_sort([]))
