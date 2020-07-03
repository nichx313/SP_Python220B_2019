""" this module contains a class for electric appliances inventory """
# Electric appliances class
from inventory_class import Inventory


class ElectricAppliances(Inventory):
    """
    class methods and attributes for electric appliances
    """
    def __init__(self, productcode, description, marketprice, rentalprice, brand, voltage):
        Inventory.__init__(self, productcode, description, marketprice, rentalprice)
        # Creates common instance variables from the parent class

        self.brand = brand
        self.voltage = voltage

    def returnasdictionary(self):
        outputdict = {'productcode': self.productcode,
                      'description': self.description,
                      'marketprice': self.marketprice,
                      'rentalprice': self.rentalprice,
                      'brand': self.brand,
                      'voltage': self.voltage}

        return outputdict
