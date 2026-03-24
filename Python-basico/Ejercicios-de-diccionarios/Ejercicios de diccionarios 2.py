list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
person = {}
for i in range(len(list_a)):
    person[list_a[i]] = list_b[i]
print(person)
