# 6. Write a python function which converts inches to cms.


def inch_to_cms():
    cm=inches*2.54
    return cm
inches=int(input("enter the value in inches: "))
print(f"The value in cms is: {inch_to_cms()}")