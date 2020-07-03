""" this module contains a class for furniture inventory """
# Furniture class
from inventory_class import Inventory


class Furniture(Inventory):
    """
    class methods and attributes for furniture
    """
    def __init__(self, productcode, description, marketprice, rentalprice, material, size):
        Inventory.__init__(self, productcode, description, marketprice, rentalprice)
        # Creates common instance variables from the parent class

        self.material = material
        self.size = size

    def returnasdictionary(self):
        outputdict = {'productcode': self.productcode,
                      'description': self.description,
                      'marketprice': self.marketprice,
                      'rentalprice': self.rentalprice,
                      'material': self.material,
                      'size': self.size}

        return outputdict
