 #Conditionals
 # sAuthor: Justin
# 15 February 2024
 
favourite_book = input("Harry Potter")
# print(f"Oh, Thats a nice book")

# implement flow chart from notes
x = 1_000_000
y = -5.7 

# if x is less then y say so
# if x is greater then way say so
# if way is equal to y say so

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
    

if x< y:
    print("x is less than y")
elif x > y:
    print ("x is greater than y")
else:
    print("x is equal to y")

foo = int(input("enter a number"))# string

if foo < -1  or foo == 0:
    print("Foo is less than 1")
    print("or it's equal to zero")

    # check if foo is inside a range
    # greater than one and less than 1000
    if foo > 1 and foo < 1000:
        print("foo is in the range 2 - 999")
else:
    print("foo is outside the range 2 - 999")




