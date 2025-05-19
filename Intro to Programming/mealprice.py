import math
child =input("\nWhat is the price of the children's meal? ")
adult =input("What is the price of the adults meal? ")
num_children =input("How many children? ")
num_adults =input("How many adults? ")
sales_rate_tax =input("What is the sales tax rate? ")
child_input = float(child)
adult_input = float(adult)
num_children_input = int(num_children)
num_adults_input = int(num_adults)
sales_rate_tax_input = float(sales_rate_tax)
child_total = num_children_input * child_input 
adult_total = num_adults_input * adult_input
#total price of the meal
subtotal_price = child_total + adult_total
#^^^compute the total price of the meal
sales_rate_tax_total = sales_rate_tax_input / 100
sales_tax = subtotal_price * sales_rate_tax_total
final_total = sales_tax + subtotal_price
#output the final total
print(f"\nSubtotal: ${subtotal_price:.2f}")
print(f"Sales tax: ${sales_tax:.2f}")
print(f"Final total: ${final_total:.2f}")
payment =input("\nWhat is the payment amount? ")
payment_input = float(payment)
change = payment_input - final_total
if payment_input < final_total:
    print("Insufficient payment.")
else:
    print(f"\nChange: ${change:.2f}")
    #vvvAsking if the user wants to round up their purchase for charity
yesorno = input("\n------------------------------------------------\nWould you like to round up your purchase for Animal Charity? (Yes or No) ").lower()
if yesorno == "no":
    print ("\nThank you.\n")
elif yesorno == "yes":
    charity = math.ceil(final_total)
    print(f"\nYour total purchase has been rounded up from ${final_total:.2f} to ${charity:.2f} for Animal Charity. \nThank you for your donation. :)\n")
else:
    print ("\nNot valid input. Please try again.\n")