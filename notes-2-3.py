# loops and iteration
# author: Justin
# 4/5/24

# print "something" 10 times
# print("something?")
# print("something")
# print("something")
# print("something")
# print("something")
# print("something")
# print("something")
# print("something")
# print("something")
# print("something")

# for _ in range(10):
#     print("something")


# create a grocery list

grocery_list = [
    "blueberry muffin"
    "potato chips"
    "steak"
    "apple juice"
    "RTX 4090 Super"
]

# for every item in the list:
#       * {grocery itm}
#       * {grocery itm}
#       * {grocery itm}
for item in grocery_list:

    if item == "RTX 4090 Super":
        print("to expensive maybe next time")
        break


    # skip the rest of the list 
    # before the RTX

    print(f"* {item}")



for i in range(100):
    print(i + 1)