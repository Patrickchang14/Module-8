# M8P3 Module 8 Patrick Chang 11/1/2026

#declare employee last names and salary
employee_data = """Adams 120000.00
Baker 75000.00
Smith 50000.00
Chang 45000.00
Grimes 55000.00"""


filename = "Employees.txt"

with open(filename, "w") as file:
  file.write(employee_data)

#declare total bonus
total_bonuses = 0

print(f"{'Last Name':<15} {'Salary':<12} {'Bonus':<10}")
print("-" * 37)

#read text files, compute bonus and display
with open(filename, "r") as file:
  for line in file:
    line = line.strip()
    if not line:
      continue

    #split last names and salaries
    parts = line.split()
    last_name = parts[0]
    salary = float(parts[1])

    #determine bonus rate
    if salary >= 100000.00:
      bonus_rate = 0.20
    elif salary == 50000.00:
      bonus_rate = 0.15
    else:
      bonus_rate = 0.10

    #calculate bonus and add total
    bonus = salary * bonus_rate
    total_bonuses += bonus

    #Outputs
    print(f"{last_name:<15} {salary:<12.2f} {bonus:<10.2f}")

print("-" * 37)
#Output total bonus
print(f"Total Bonuses: {total_bonuses:,.2f}")