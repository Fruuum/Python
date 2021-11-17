seasons_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer",
                8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
month_number = int(input("введите номер месяца: "))
if 0 >= month_number or month_number > 12:
    print('Error. Please, enter month number from 1 to 12')
else:
    print(seasons_dict.get(month_number))

seasons_list = [None, "Winter", "Winter", "Spring", "Spring", "Spring", "Summer",
                "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"]
month_number = int(input("введите номер месяца: "))
if 0 >= month_number or month_number > 12:
    print('Error. Please, enter month number from 1 to 12')
else:
    print(seasons_list[month_number])
