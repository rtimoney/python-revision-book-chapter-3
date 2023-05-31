# examining condition 

# python does not have a ternary operator
# uses conditional expression in much the same way

# declare and initialize variables
a = 1
b = 2

print('\nVariable a is :' ,  'One' if (a == 1) else 'Not One')
#remainder of a number divided by two will be zero if the number is even
print('Variable a is :' ,  'Even' if (a % 2 == 0) else 'Odd')

print('\nVariable b is :' ,  'One' if (b == 1) else 'Not One')
#remainder of a number divided by two will be zero if the number is even
print('Variable b is :' ,  'Even' if (b % 2 == 0) else 'Odd')

top = a if ( a > b ) else b
print('\nGreater Value is:', top)

# important note : some devs dislike conditional expressions because its syntax contradicts the principle  of easy readability

