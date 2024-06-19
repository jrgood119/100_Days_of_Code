print("Welcome to the tip calculator")

#Get bill amount
total = float(input("What was your total bill? $"))

# Get tip percentage
tip = int(input("How much would you like to give? 10, 12, or 15? "))

# Convert tip to percentage
tip_percentage = tip * 0.01

# Get number of people in party
people = int(input("How many people split the bill? "))

# Get total bill
total_bill = total * tip_percentage + total

# Get total per person
total_per_person = "{:.2f}".format(total_bill / people)

print(f"Each person should pay: ${total_per_person}")