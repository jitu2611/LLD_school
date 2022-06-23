from address import Address


class Person:
    def __init__(self, firstName, lastName, dateOfBirth, address):
        self.firstName = firstName
        self.lastName = lastName
        self.dateOfBirth = dateOfBirth
        if isinstance(address, Address):
            self.address = address
        else:
            raise TypeError("Invalid Address Type")
