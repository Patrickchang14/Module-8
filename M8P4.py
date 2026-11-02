#M8P4 Module 8 Patrick Chang 11/1/2026

#text file
data_content = """Widget
10
50.00
Hammer
2
10.00
Saw
4
8.50"""

with open("orders.txt", "w") as file:
    file.write(data_content)

#declare variables
total_extended_price = 0
order_count = 0

print(f"{'Item':<12} {'Quantity':<10} {'Price':<10} {'Extended Price':<15}")
print("-" * 52)

#open/read file
with open("orders.txt", "r") as file:
    while True:
        #read 3 lines in order
        item_line = file.readline()
        quantity_line = file.readline()
        price_line = file.readline()

        #end loop function
        if not item_line:
            break

        #declare variables
        item = item_line.strip()
        quantity = int(quantity_line.strip())
        price = float(price_line.strip())

        #calculate extended price
        extended_price = quantity * price

        #calculate total
        total_extended_price += extended_price
        order_count += 1

        #Output
        print(f"{item:<12} {quantity:<10} ${price:<9.2f} ${extended_price:<14.2f}")

#calculate average order
average_order = total_extended_price / order_count if order_count > 0 else 0.0

#output summary
print("-" * 52)
print(f"Total Extended Price: ${total_extended_price:.2f}")
print(f"Total Number of Orders: {order_count}")
print(f"Average Order Value: ${average_order:.2f}")