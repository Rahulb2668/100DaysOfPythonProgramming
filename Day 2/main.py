print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

total_bill_with_tip = bill+ (bill * (tip/100))
each_person_bill = round(total_bill_with_tip/people, 2)




print(f"Each Person should pay: {each_person_bill}")