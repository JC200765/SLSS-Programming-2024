# author: justin
# 22 feb 2024
# method: string

# ask user what is weather like?
weather = input("what the weather is it")
# if reply rainy 
    # nring an umbrella
if weather.lower().strip("!.?, ") == "rainy":
    print("you need an umbrella")
else:
    print(f"i dont understand")

