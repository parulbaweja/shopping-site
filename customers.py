"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self,
                 first_name,
                 last_name,
                 email,
                 password
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Customer: {name}, {email}, {password}'.format(
            name=self.first_name + self.last_name, email=self.email,
            password=self.password)


def read_customers_from_file(filename):

    customers = {}

    for line in open(filename):
        line = line.strip()
        (first_name,
         last_name,
         email,
         password) = line.split('|')

        customers[email] = Customer(first_name,
                                    last_name,
                                    email,
                                    password)

    return customers


def get_by_email(email):
    return customers[email]


customers = read_customers_from_file('customers.txt')
