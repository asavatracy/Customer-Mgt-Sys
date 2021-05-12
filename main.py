import random
from datetime import date

# check if this is a new customer
new_cus = input("New customer? Y for Yes, N for no. ")

# if new customer
if new_cus == 'Y' or new_cus =='y':
    name = input("Enter your name: ")
    dob = input("Enter your date of birth in DD-MM-YYYY format: ")
    id_no = input("Enter your identification number: ")
    tel_no = input("Enter your telephone number: ")
    print("Customer registration successful!\nCustomer name is " + name + " born on " + dob +
          " , identification number " + id_no + " and telephone number " + tel_no + ".")
    quality_points = 0

# not a new customer
elif new_cus == 'N' or new_cus == 'n':
    name = input("Enter your name: ")
    dob = input("Enter your date of birth in DD-MM-YYYY format: ")
    print("Welcome back " + name + "! " + "Enjoy your shopping.")
else:
    print("Error!! Please ensure you have entered the right choice.")
    exit(0)

# check if customer has personal bag
personal_bag = input("Does customer have a personal bag? Y for Yes, N for No ")
if personal_bag == 'Y' or personal_bag == 'y':
    compartment_no = random.randint(1,10)
    print("Your compartment number is " + str(compartment_no))
# if customer does not have a personal bag
elif personal_bag == 'N' or personal_bag == 'n':
    print("Proceed to shop.")
else:
    print("Error!! Please ensure you have entered the right choice.")
    exit(0)

# enter prices for items
item_one = int(input("Please enter the price of the first item: "))
item_two = int(input("Please enter the price of the second item: "))
item_three = int(input("Please enter the price of the third item: "))
# calculate total price
total_price = item_one + item_two + item_three
# assigning values to quality points parameters
quality_price = 5000
point_below = 1
point_above = 1.5
rate = 100
# calculate quality points
if total_price <= quality_price:
    quality_points = (total_price/rate) * point_below
    print("You have earned " + str(quality_points) + " quality points.")
else:
    difference = total_price - quality_price
    quality_points = (difference/rate) * point_above
    print("You have earned " + str(quality_points) + " quality points.")
print("Your total is " + str(total_price))

# ask customer if they want to redeem points
redeem_choice = input("Do you wish to redeem your points? Y for Yes, N for No ")
if redeem_choice == 'Y' or redeem_choice == 'y':
    no_of_points = int(input("How many points do you wish to redeem? "))
    final_price = total_price - no_of_points
    print("Your final price is " + "Ksh " + str(final_price))
elif redeem_choice == 'N' or redeem_choice == 'n':
    print("Your final price is " + str(total_price))
else:
    print("Please enter a valid choice.")
    exit(0)

# ask customer to choose payment option
payment_option = input("Choose your payment option:\nC for Cash\nM for M-Pesa\nV for Visa Card ")
if payment_option == 'M' or payment_option == 'm' or payment_option =='V' or payment_option =='v':
    # customer receives discount if they use mpesa or visacard
    total_final_price = final_price * 0.98
    print("Your total final price is " + str(total_final_price))
elif payment_option == 'C' or payment_option == 'c':
    # no discount if payment is in cash
    total_final_price = final_price
    print("Your total final price is " + str(total_final_price))
else:
    print("Invalid entry! Please try again.")
    exit(0)

remaining_points = quality_points - no_of_points
today = date.today()
# print receipt
print("Supermarket Name: ABC Supermarket\n" + "Customer Name: " + name + "\n" + "Date: " + str(today) + "\n"
      + "Total Amount: Ksh " + str(total_final_price) + "\n" + "Quality Points Earned: " + str(quality_points) +
    "\n" + "Remaining Quality Points: " + str(remaining_points) + "\n")









