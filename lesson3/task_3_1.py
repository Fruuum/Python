def my_func(num1, num2):
    dvs = num1 / num2
    return round(dvs, 3)


try:
    print(my_func(float(input("Enter 1st number: ")), float(input("Enter 2nd number: "))))
except (ZeroDivisionError, ValueError) as error:
    print(error)
