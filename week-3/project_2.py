print("Welcome to Izifin Technolgy's ATR Calculator \n")

while True:
  option = int(input("""
Choose an action:
1. Calculate staff Annual Tax Revenue (ATR)
2. End program
"""))

  if option == 2:
    break

  years_of_exp = int(input("Enter staff years of experience: "))
  age = int(input("Enter staff age: "))

  atr = None
  if years_of_exp > 25 and age >= 55:
    atr = 5_600_000
  elif years_of_exp > 20 and age >= 45:
    atr = 4_480_000
  elif years_of_exp > 10 and age >= 35:
    atr = 1_500_000
  else:
    atr = 550_000

  print(f"Staff with {years_of_exp} year(s) of experience and aged {age} has N{atr} ATR")
