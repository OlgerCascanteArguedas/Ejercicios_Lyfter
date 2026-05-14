def bubble_sort_steps(list_to_sort):
    iterations = 0
    swaps = 0

    n = len(list_to_sort)

    for i in range(n - 1):
        iterations += 1

        for j in range(n - 1 - i):

            if list_to_sort[j] > list_to_sort[j + 1]:

                # Intercambiar elementos
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp

                swaps += 1

    print("Sorted list:", list_to_sort)
    print("Iterations:", iterations)
    print("Swaps:", swaps)


# Ejemplo
numbers = [5, 1, 4, 2, 3]

bubble_sort_steps(numbers)
