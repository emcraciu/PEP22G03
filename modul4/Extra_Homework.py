"""
Create a function that takes in a dictionary with user provided shopping list ("cart") and a dictionary of shops with
information on available product and prices ("shops") and returns the name of the shop where user can buy the items with
the quantity specified in the cart at the best price
"""

shop1 = {'mere': 10, 'pere': 15, 'prune': 6, 'ananas': 20}  # e.g. mere cost 10 RON/KG
shop2 = {'mere': 11, 'pere': 15, 'prune': 6}
shop3 = {'mere': 10, 'pere': 16, 'prune': 7, 'papaya': 25}

cart = {'mere': 2, 'pere': 3, 'prune': 6}  # e.g. buy 2 KG mere

shops = {'PShop': shop1, 'KShop': shop2, 'LShop': shop3}
