""" this module contains a class for inventory """
# Inventory class


class Inventory:
    """
    class methods and attributes for inventory
    """
    def __init__(self, productcode, description, marketprice, rentalprice):
        self.productcode = productcode
        self.description = description
        self.marketprice = marketprice
        self.rentalprice = rentalprice

    def returnasdictionary(self):
        """
        converts to dictionary
        """
        outputdict = {'productcode': self.productcode,
                      'description': self.description,
                      'marketprice': self.marketprice,
                      'rentalprice': self.rentalprice}

        return outputdict
