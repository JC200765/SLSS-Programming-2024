# make an Mcdobot
# Author: Justin ,C
# Feb 22 2024

reply = input("Would you like fires with your meal ?")

if reply.lower().strip("!.?, ") == "yes":
    print("here you go")
elif reply.lower().strip("?.,! ") == "no":
    print("something is wrong with you")
else:
    print("i dont understand")
