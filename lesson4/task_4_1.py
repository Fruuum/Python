from sys import argv

scr_name, w_hours, rate, award = argv

wage = float(w_hours) * float(rate) + float(award)
print(wage)
