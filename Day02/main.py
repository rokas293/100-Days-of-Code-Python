print("Welcom to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

bill_per_person = ("{:.2f}".format((total_bill / num_people) * (1 + tip / 100)))

print(f"Each person should pay: ${bill_per_person}")
