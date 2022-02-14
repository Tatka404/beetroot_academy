stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for key in prices:
    if key in stock:
        prices[key] = prices[key] + stock[key]

total = {**stock, **prices}
print(total)
