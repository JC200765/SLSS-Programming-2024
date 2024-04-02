def best_driver(driver):



    if driver.lower().strip("!.?,") == "lewis":
        return"yea"
    if driver.lower().strip("!.?,") == "max":
        return"no"
    

    
driver = input("who is the best f1 driver")

result = best_driver(driver)
print(result)