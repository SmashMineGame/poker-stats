import random

values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"]
suits = ["C", "H", "S", "D"]

deck = []

for s in suits:
    for v in values:
        deck.append(v + s)

random.shuffle(deck)

decksFile = open("./decks.txt", 'a')
decksFile.write(",".join(deck) + "\n")
