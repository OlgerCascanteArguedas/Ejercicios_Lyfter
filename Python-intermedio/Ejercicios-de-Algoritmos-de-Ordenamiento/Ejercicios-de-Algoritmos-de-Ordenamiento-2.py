def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) - 1):
        has_made_changes = False
        for index in range(len(list_to_sort) - 1, outer_index, -1):
            current_element = list_to_sort[index]
            previous_element = list_to_sort[index - 1]
            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Elemento anterior: {previous_element}')
            if current_element < previous_element:
                print('El elemento actual es menor al anterior. Intercambiandolos...')
                list_to_sort[index] = previous_element
                list_to_sort[index - 1] = current_element
                has_made_changes = True
        if not has_made_changes:
            return list_to_sort
    return list_to_sort
numbers = [5, 2, 8, 1, 9]
print(bubble_sort(numbers))
