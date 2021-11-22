def account(**kwargs):
    print(" ".join(kwargs.values()))


account(name=input("Enter your name: "), surname=input("Enter your surname: "),
        date_of_birth=input("Enter your date_of_birth: "), city=input("Enter your city: "),
        mail=input("Enter your mail: "), tel=input("Enter your tel: "))
