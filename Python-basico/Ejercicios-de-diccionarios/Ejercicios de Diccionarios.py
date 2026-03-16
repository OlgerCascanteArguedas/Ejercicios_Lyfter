hotel = {
    "nombre": "Hotel Paradise",
    "numero_de_estrellas": 5,
    "habitaciones": [
        {
            "numero": 101,
            "piso": 1,
            "precio_por_noche": 120.0
        },
        {
            "numero": 202,
            "piso": 2,
            "precio_por_noche": 150.0
        },
        {
            "numero": 305,
            "piso": 3,
            "precio_por_noche": 200.0
        }
    ]
}
print(hotel)
#####################
list_a = ['first_name', 'last_name', 'role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
person = {}
for i in range(len(list_a)):
    person[list_a[i]] = list_b[i]
print(person)
####################
list_of_keys = ['access_level', 'age']
employee = {
    'name': 'John',
    'email': 'john@ecorp.com',
    'access_level': 5,
    'age': 28
}
for key in list_of_keys:
    employee.pop(key, None)
print(employee)
##########
