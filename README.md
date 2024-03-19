# Online Bookstore ORM

This Python module provides an Object-Relational Mapping (ORM) for an online bookstore database using SQLAlchemy. It is designed to interact with a PostgreSQL database, simplifying data operations for users, orders, books, order details, and categories.

## Installation

To use this module, ensure you have SQLAlchemy installed in your environment. If not, you can install it using pip:

```sh
pip install SQLAlchemy
```

## Models

This ORM module defines the following models:

- `User`: Represents users of the online bookstore, including their personal details.
- `Order`: Represents orders placed by users, including order details and status.
- `Book`: Represents books available in the bookstore, including pricing and stock quantity.
- `OrderDetail`: Represents the many-to-many relationship between books and orders.
- `Category`: Represents categories of books.

Each model includes a `to_dict` method for easy serialization to a dictionary.

### Relationships

- A `User` can have many `Order`s.
- An `Order` can contain many `Book`s through `OrderDetail`.
- A `Book` belongs to a `Category` and can be part of many `Order`s through `OrderDetail`.
- A `Category` can include many `Book`s.

## Usage

After configuring the database connection, you can start interacting with the database through the ORM. Here's an example of how to create a new user:

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(
    FirstName='John',
    LastName='Doe',
    HouseNumber='123',
    StreetName='Main St',
    Postcode='A1B 2C3',
    Email='john.doe@example.com',
    PhoneNumber='123-456-7890'
)

session.add(new_user)
session.commit()
```

Replace the attributes with the actual data you wish to insert into the database.
