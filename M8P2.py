# Module 8 M8P2 Patrick Chang 10/21/2026

#initial variables
a=0
b=1

#output
print("First 20 numbers of the Fibonnaci sequence:")

#run loop 20 times
for i in range(20):
    next_number = (a+b)

    #output current fibonacci number
    print(next_number, end=" ")

    #updated variables
    a=b
    b=next_number

print()  #output single line