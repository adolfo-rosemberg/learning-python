num1 = input("Please enter the first number: ")
num2 = input("Please enter a second number: ")

# Using format
print('The result of the sum is: {}'.format(
    int(num1) + int(num2)))

# Using Interpolation Operator
print('The result of the substraction is: %s' %
      (int(num1) - int(num2)))

# Using f-strings
print(f'The result of the multiplication is: {int(num1) * int(num2)}')
