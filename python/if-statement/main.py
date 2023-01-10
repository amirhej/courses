var1 = 10
var2 = 20
# Logical conditions
print('Implementation of logical conditions for these two variables: ')
print('First variable value: ', var1)
print('Second variable value: ', var2)
print(var1, ' == ', var2, ' : ', var1 == var2 )
print(var1, ' != ', var2, ' : ', var1 != var2 )
print(var1, ' < ', var2, ' : ', var1 < var2 )
print(var1, ' <= ', var2, ' : ', var1 <= var2 )
print(var1, ' > ', var2, ' : ', var1 > var2 )
print(var1, ' >= ', var2, ' : ', var1 >= var2 )

# IF statement

if var1 < var2 :
    print('First variable is less than second one')
# Indentation 
# uncommnet lines 20 & 21 to see error
# if var2 < var1:
# print('First variable is less than second one')

# IF , ELIF statement:
if var2 == var1:
    print('First variable equal to second one')
elif var2 > var1:
    print('Second variable greater than first one')
# IF , ELIF, ELSE statement:
if var1 == var2:
    print('First variable equal to second one')
elif var1 > var2:
    print('First variable is greater than second one')
else:
    print('First variable is less than second one')

# Short hand if
print('Short hand if...')
if var1 < var2: print( var1 )

# Short hand if...else
print('Short hand if...else...')
print('First variable') if var1 >= var2 else print('Second variable')

## multiple else statement
print('Short hand if...else... with multiple else statement')
print(var1) if var1 > var2 else print(var2) if var2 > var1 else print('Equal')

# And
if var1 and var1 == var2:
    pirnt('First variable exists, has in access value and equals to second variable ')
# NOTE: The value in access is a value equivalent to True

# Or
if var1 > var2 or var1 < var2:
    print('Those variables are not equal')

# Nested if
age = 30

if age > 18:
    print('You are of legal age')
    if age > 45:
        print('Relax and enjoy life')
    else:
        print('We can hire you')
else:
    print('You are not of legal age')

# The Pass statement
if age < 10 and age > 99:
    pass
else:
    print('Your age is in two digits')