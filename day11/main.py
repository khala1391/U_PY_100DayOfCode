# import random

# def deal_card():
#     """ random card from the deck"""
#     cards = [11,1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 10, 10]
#     card = random.choice(cards)
#     return card

# user_cards =[]
# computer_cards = []

# for _ in range(2):
#     new_card = deal_card()
#     # ! user_cards +=  new_card
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card())
    
    


lst = [1, 2, 3]
lst.append([4, 5])  # Appends the list [4, 5] as a single element
print(lst)


lst2 = [1, 2, 3]
lst2.extend([4, 5])  # Extends the list by adding each element of [4, 5]
print(lst2)
