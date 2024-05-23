# Modules
# Author: Justin
# 11 marcj 2024

import random

# demonstarte some parts of the random module

def coin_flip():

    # return head , tails or other
    # heads = 0 - 0.5
    # tails = 0.5 - 0.99999999
    # other - the est
    result = random.random()

    if result < 0.5:
        return "heads"
    elif result < 0.999999:
        return "tails"
    else:
        return "other"
    
def main():
    heads, tails, other = 0, 0, 0

    result = coin_flip()

    for _ in range(1_000_000):
        result = coin_flip()
        if result == "heads":
            heads = heads + 1 
        elif result == "tails":
            tails += 1
        else:
            other += 1

    print(f"Heads: {heads}")
    print(f"Tails: {tails}")
    print(f"others: {other}")

    city_list = ["Vancouver", "Richmond", "Shanghai", "Beijing"]

    # Randomly choose city from the list
    chosen_city = random.choice(city_list)
    print(chosen_city)



main()