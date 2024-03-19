from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

base = declarative_base()
engine = create_engine('onlinebookstore-db.czaqm04u8dyv.eu-west-2.rds.amazonaws.com')

class Users(base):
    __table_name__ = 'Users'

    UserID = Column(Integer, primary_key=True)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    HouseNumber = Column(String(50))
    StreetName = Column(String(50))
    Postcode = Column(String(50))
    Email = Column(String(50))
    PhoneNumber = Column(String(50))

    def to_dict(self):
        return {
            "UserID": self.UserID,
            "FirstName": self.FirstName,
            "LastName": self.LastName,
            "HouseNumber": self.HouseNumber,
            "StreetName": self.StreetName,
            "Postcode": self.Postcode,
            "Email": self.Email,
            "PhoneNumber": self.PhoneNumber
        }
class Order(base):
    __tablename__ = 'Orders'

    OrderID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('Users.UserID'))
    TotalPrice = Column(Numeric)
    OrderStatus = Column(String(50))
    OrderDate = Column(DateTime)
    ShippingDate = Column(DateTime)
    user = relationship('User', back_populates='orders')
    order_details = relationship('OrderDetail', back_populates='order')

    def to_dict(self):
        return {
            "OrderID": self.OrderID,
            "UserID": self.UserID,
            "TotalPrice": self.TotalPrice,
            "OrderStatus": self.OrderStatus,
            "OrderDate": self.OrderDate,
            "ShippingDate": self.ShippingDate,
        }

class Book(base):
    __tablename__ = 'Books'

    BookID = Column(Integer, primary_key=True)
    BookTitle = Column(String(50))
    AuthorName = Column(String(50))
    Price = Column(Numeric)
    ISBN = Column(String(100))
    StockQuantity = Column(Integer)
    CategoryID = Column(Integer, ForeignKey('Categories.CategoryID'))
    category = relationship('Category', back_populates='books')
    order_details = relationship('OrderDetail', back_populates='book')

    def to_dict(self):
        return {
            "BookID": self.BookID,
            "BookTitle": self.BookTitle,
            "AuthorName": self.AuthorName,
            "Price": self.Price,
            "ISBN": self.ISBN,
            "StockQuantity": self.StockQuantity,
            "CategoryID": self.CategoryID,
        }

class OrderDetail(base):
    __tablename__ = 'OrderDetails'

    OrderDetailID = Column(Integer, primary_key=True)
    OrderID = Column(Integer, ForeignKey('Orders.OrderID'))
    BookID = Column(Integer, ForeignKey('Books.BookID'))
    Quantity = Column(Integer)
    order = relationship('Order', back_populates='order_details')
    book = relationship('Book', back_populates='order_details')

    def to_dict(self):
        return {
            "OrderDetailID": self.OrderID,
            "OrderID": self.OrderID,
            "BookID": self.BookID,
            "Quantity": self.Quantity
        }

class Category(base):
    __tablename__ = 'Categories'

    CategoryID = Column(Integer, primary_key=True)
    CategoryName = Column(String(50))
    books = relationship('Book', back_populates='category')

    def to_dict(self):
        return {
            "CategoryID": self.CategoryID,
            "CategoryName": self.CategoryName
        }

