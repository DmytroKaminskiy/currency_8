import sqlite3

conn = sqlite3.connect('./examples/chinook.db')
conn.row_factory = sqlite3.Row

cur = conn.cursor()

sql = '''
SELECT CustomerId, LastName, FirstName FROM customers;
'''

cur.execute(sql)
customers = cur.fetchall()

conn.close()

###################################
class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

customer_objects = []
for customer in customers:
    customer_obj = Customer(
        customer_id=customer["CustomerId"],
        first_name=customer["FirstName"],
        last_name=customer["LastName"],
    )
    customer_objects.append(customer_obj)

breakpoint()
for customer in customer_objects:
    # print(f'Full Name: {customer[1]} {customer[2]}')
    # print(f'Full Name: {customer["FirstName"]} {customer["LastName"]}')
    # print(f'Full Name: {customer.first_name} {customer.last_name}')
    print(f'Full Name: {customer.get_full_name()}')

# for customer in customer_objects:
#     print(f'Full Name: {customer.get_full_name()}')

'''
ORM
O - object (class Customer)
R - relation (sql table)
M - mapping (join)

Customers.objects.all()

Django ORM
SqlAlchemy
'''