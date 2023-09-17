first = float(input("First Number: "))

operation = input('''
Please type in the operation you want to use
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
''')

second = float(input("Second Number: "))

if operation == '+':
    print('{} + {} = '.format(first, second))
    print(first + second)

elif operation == '-':
    print('{} - {} = '.format(first, second))
    print(first - second)

elif operation == '*':
    print('{} * {} = '.format(first, second))
    print(first * second)

elif operation == '/':
    print('{} / {} = '.format(first, second))
    print(first / second)

elif operation == '**':
    print('{} ** {} = '.format(first, second))
    print(first ** second)

else:
    print('ERROR!!')
