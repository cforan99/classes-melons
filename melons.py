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
