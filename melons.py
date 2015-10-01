"""This file should have our melon-type classes in it."""

BASE_COST = 5.00

# from data import melons as melons_data

# print melons_data

# for melon_tup in melons_data:
#     class_name = 

class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = BASE_COST * float(qty)
        if qty >= 3:
            total *= 0.75

        return total

    def print_price(self, qty):
        """Prints get_price"""

        price = self.get_price(qty)

        print "${:.2f}".format(price)







class CantaloupeOrder(object): 
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate the price of the cantaloupe order based on quantity."""
        total = BASE_COST * float(qty)
        if qty >= 5:
            total /= 2
        return total

    def print_price(self, qty):
        """Prints get_price"""
        price = self.get_price(qty)
        print "${:.2f}".format(price)










class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self, qty):
        """Calulates a total cost of Casaba for qty Casaba."""
        
        total = (BASE_COST + 1.00) * qty * 1.5
        return total

    def print_price(self, qty):
        """Passes qty to get_price and prints pretty version of what's returned"""

        price = self.get_price(qty)
        print "${:.2f}".format(price)













































