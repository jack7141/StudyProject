"""python 3.9 이상부터 가능"""
# 출처 - https://www.youtube.com/shorts/VLBERpAEzew
from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    email: str
    active: bool
    
# Customer 데이터클래스를 사용하여, object를 찾는 방법
CUSTOMERS: dict[str, Customer] = {}


def add_customer(name: str, email: str, active: bool):
    CUSTOMERS[email] = Customer(name, email, active)

def find_by_email(email: str) -> Customer:
    return CUSTOMERS[email]

def main():
    add_customer('test', 'test@email.com', True)
    add_customer('test1', 'test1@email.com', True)
    add_customer('test2', 'test2@email.com', True)

    print(find_by_email('test@email.com'))

if __name__ == '__main__':
    main()

"""
CODE SMELL
@dataclass
class Customer:
    name: str
    email: str
    active: bool

CUSTOMERS: list[Customer] = []


def add_customer(name: str, email: str, active: bool):
    CUSTOMERS.append(Customer(name, email, active))

def find_by_email(email: str) -> Customer:
    for customer in CUSTOMERS:
        if customer.email == email:
            return customer
    raise ValueError('No customer with email')

def main():
    add_customer('test', 'test@email.com', True)
    add_customer('test1', 'test1@email.com', True)
    add_customer('test2', 'test2@email.com', True)

    print(find_by_email('test@email.com'))

if __name__ == '__main__':
    main()
"""
