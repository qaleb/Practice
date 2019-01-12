def sum_of_digits(number):
    total = 0
    for digit in str(number):
        total += int(digit)
    return total
input_value = int(input("Enter positive number:"))
print(sum_of_digits(input_value))