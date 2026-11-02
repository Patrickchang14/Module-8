# Module 8 M8P1 Patrick Chang 10/21/2026

#Inputs
principle_amount = float(input("Enter principle amount: "))
interest_rate = float(input("Enter interest rate: "))

#variables
count = 1
total_interest_earned = 0

#table headers before loop
print("\nFormatted output")
print(f"{'Year':<6}{'beginning_balance':<20}{'Ending balance':<15}")

#loop
while count <= 5:
    #reminder of starting balance for this specific year
    beginning_balance = principle_amount

    #calculations for this year
    annual_interest = beginning_balance*interest_rate
    ending_balance = beginning_balance + annual_interest

    #total accumulated interest
    total_interest_earned += annual_interest

    #output
    print(f"{count:<6}${beginning_balance:<19,.2f}${ending_balance:<14,.2f}")

    #principle for next year
    principle_amount = ending_balance

    #transition to next year
    count += 1

#summary output after loop
print(f"\nTotal interest earned: ${total_interest_earned:,.2f}")