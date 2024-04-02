# functins
# author: justin
# feb 26 20024

# create saying hellow_world
# going to sy hello world

# def say_hello():
#     print("hello")

# say_hello()

# create function called say_hello_params
# print "hello {oarameter}!"
# ---> e.g. say_helloparams{"jim"}
# >> hello jim


# def say_hello_params(name):
#     print(f"hello{name}!")


# create a function how_big
# returns how big a digit is
    
def how_big(num):
    if num < 0:
        return "very small"
    if num < 10:
        return 'pretty small'
    if num < 1000:
        return "pretty bg"

print(how_big(-1))
print(how_big(1))
result = how_big(1_000_000)
print(result)


# creater function ader
# allow 2 inputs that #
# returm sum of both number

# def adder(x, y):
#     return  x + y

# result = adder(1, 1) # 2 



# say_hello()
# say_hello_params("emily")
# say_hello_params("ana")

