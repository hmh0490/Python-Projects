import pandas
# Abstract Base Class
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})

class Hotel:
    # class variables are coded outside the method of a class
    # access it two ways:
    # (1) Hotel.watermark, (2) hotel1 = Hotel(), hotel1.watermark
    watermark = "The Real Estate Company"

    # instance method is applied to instances
    # it has self in the declaration
    # instance variables and instance methods are instance attributes
    def __init__(self, hotel_id):
        # self.hotel_id and self.name are instance variables
        # coded inside a method
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        # same as : df.loc[df["id"] == hotel_id]["available"].squeeze()
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    # class methods have cls in declaration
    # class methods have @classmethod decorator
    # access it two ways:
    # (1) Hotel.get_hotel_count(), (2) hotel1.get_hotel_count()
    # these are not related to a particular instance
    # class variables and class methods are class attributes
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

    # add magic methods at the end
    # this are overwriting the built-in methods
    def __eq__(self, other):
        if self.hotel_id == other.hotel_id:
            return True
        else:
            return False


# Ticket is a child of an abstract class
class Ticket(ABC):
"""Abstract classes are not for creating instances,
they are to show the required structure, eg. all class inheriting from the
Ticket abstract class should have a generate method, otherwise error will occur
"""

    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    # property: special instance method, behaves like a variable (line 54)
    # it's usually a noun, not a verb
    # needs a property decorator
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name

    # function with no reference to the class or instance (no self, no cls)
    # eg. want to convert EUR to USD
    # distinction between static method and class method is blurred;
    # for conversion usually static method is used
    @staticmethod
    def convert(amount):
        return amount * 1.2

    class DigitalTicket(Ticket):
        def generate(self):
            return "Hello this is your digital ticket"

        def download(self):
            pass

    # hotel1 = Hotel(hotel_id="188")
    #
    # print(hotel1.available())
    # print(hotel1.name)
    #
    # print(hotel1.watermark)
    # print(Hotel.watermark)
    #
    # print(Hotel.get_hotel_count(data=df))
    # print(hotel1.get_hotel_count(data=df))
    #
    # ticket = ReservationTicket(customer_name="john smith ", hotel_object=hotel1)
    # print(ticket.the_customer_name)
    # print(ticket.generate())
    #
    # converted = ReservationTicket.convert(10)
    # print(converted)
    #
    # # syntactic sugar, simplified syntax: "hello" == "hi"
    # # it is the same as "hello"__eq__("hi")
    # # or 1 + 2 = 1 .__add(2) = 3