##Contri per person calculator
rent =int(input("Enter your Rent:"))
food =int(input("\nEnter your Food Expenses:"))
extra=int(input("Enter your Extra expenses:"))
electricity_units =int(input("Enter units of Elec.used:"))
charge_per_unit=int(input("Enter charge of 1 unit Elec.in your Area:"))
electricity_bill = electricity_units*charge_per_unit
persons = int(input("No.of people living on room:"))
Amount_to_pay= (rent+food+extra+electricity_bill)//persons
print("Per Person Contri:",Amount_to_pay)

























