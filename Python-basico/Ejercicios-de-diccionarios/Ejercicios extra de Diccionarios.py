sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name': 'Iron', 'upc': 'ITEM-324', 'unit_price': 32.45},
            {'name': 'Basketball', 'upc': 'ITEM-432', 'unit_price': 12.54},
        ]
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {'name': 'Lava Lamp', 'upc': 'ITEM-453', 'unit_price': 65.76},
            {'name': 'Key Holder', 'upc': 'ITEM-23', 'unit_price': 5.42},
        ]
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {'name': 'Key Holder', 'upc': 'ITEM-23', 'unit_price': 3.42},
            {'name': 'Basketball', 'upc': 'ITEM-432', 'unit_price': 17.54},
        ]
    }
]
result = {}
for sale in sales:
    for item in sale['items']:
        upc = item['upc']
        price = item['unit_price']
        if upc in result:
            result[upc] += price
        else:
            result[upc] = price
print(result)
#############
employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
grouped_employees = {}
for employee in employees:
    department = employee["department"]

    if department in grouped_employees:
        grouped_employees[department].append(employee)
    else:
        grouped_employees[department] = [employee]
print(grouped_employees)
###############
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
totals_by_category = {}
for product in products:
    category = product["category"]
    price = product["price"]
    if category in totals_by_category:
        totals_by_category[category] += price
    else:
        totals_by_category[category] = price
print(totals_by_category)
