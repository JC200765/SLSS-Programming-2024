# more functions
# author: justin
# 4/4/24
def stars(Num_stars: int) -> str:
    """Returns given number of stars"""
    value = ""

    # if value is 1 or 0 star ill be 1
    # if value > 1 "*" * num_star
    # else neg # is error
    if Num_stars == 0 or Num_stars == 1:
        value = "*"
    elif Num_stars > 1:
        value = "*" * Num_stars 
    




    return "*" * Num_stars


s




# multipy strings
# greeting = "hello"

# print(greeting * 100)

# print("The quick brown fox jumps over the lazy dog." * )


print(stars(1))
print(stars(100))
print(stars(0))
print(stars(-1))

def pyramid(base_width: int):
    """Prints a pyamid of stars of given base width

    Params:
    base_width - bottom row of stars"""
    
    for i in range(base_width):
        print(i + 1)





pyramid(1)
pyramid(5)
pyramid(20)
