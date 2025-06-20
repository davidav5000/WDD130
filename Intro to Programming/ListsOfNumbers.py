numbers = []
new_numbers = -1
while new_numbers != 0:
    new_numbers = int(input("Type a number (type 0 when finished): "))
    if new_numbers != 0:
        numbers.append(new_numbers)
sum = 0
for number in numbers:
    sum += number
print(f"The sum of your numbers is: {sum}")
total_numbers = len(numbers)
avarage = sum / total_numbers
print(f"The average of your numbers is: {avarage}")
largest_number = -1
for number in numbers:
    if number > largest_number:
        largest_number = number
print(f"The largest number is: {largest_number}")
smallest_positive_number = -1
for number in numbers:
    if number > 0 and (smallest_positive_number == -1 or number < smallest_positive_number):
        smallest_positive_number = number
print(f"The smallest positive number is: {smallest_positive_number}")
print("The sorted list is: ")
numbers.sort()
for number in numbers:
    print(f"{number}")
