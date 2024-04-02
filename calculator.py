print("Hello world")

# value is + - / *
def calculate():
    
    while(True):
        value = input("Enter operator: ")
        match value:
            case "+":
                print("You want to do addition")
                break
            case "-":
                print("You want to do subtraction")
                break

            case "/":
                print("You want to do division")
                break

            case "*":
                print("You want to do multiplication")
                break

            case _:
                print("Enter valid operator pleasee.")
                continue

    first_value = int(input("Enter 1st number: "))
    second_value = int(input("Enter 2nd number: "))

    match value:
        case "+":
            return str(first_value + second_value)
        case "-":
            return str(first_value - second_value)
        case "/":
            return str(first_value / second_value)
        case "*":
            return str(first_value * second_value)
            



            
answer = calculate()
print(answer)
        


