# M8P5 Module 8 Patrick Chang 11/1/2026

#constants
in_district_rate = 250.00
out_district_rate = 500.00

#text file
file_name = "students.txt"
sample_data = """Jones I 12
Adams I 10
Baker O 12
Smith O 16"""

with open(file_name, "w") as file:
    file.write(sample_data)

#tracking variables
total_tuition = 0
student_count = 0

print(f"{'Last Name':<12}{'Credits':<10}{'Tuition Owed':<12}")
print("-" * 34)

#process
with open(file_name, "r") as file:
    for line in file:
        #organization
        line = line.strip()
        if not line:
            continue

        #parse
        last_name, district_code, credits_str = line.split()
        credits_taken = int(credits_str)

        #calculate rate
        if district_code.upper() == 'I':
            rate = in_district_rate
        else:
            rate = out_district_rate

        #calculate tuition owed
        tuition_owed = credits_taken * rate

        #totals
        total_tuition += tuition_owed
        student_count += 1

        #output student results
        print(f"{last_name:<12}{credits_taken:<10}${tuition_owed:,.2f}")

#output final totals
print("-" * 34)
print(f"Total Tuition Owed: ${total_tuition:,.2f}")
print(f"Total Students:     {student_count}")