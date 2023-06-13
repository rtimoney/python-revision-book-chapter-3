# initiate variables with values for comparison 
nil=0
num=0
top=1
cap='A'
low='a'

# \t adds an invisible tab character 
# --

# nil == num will return a boolean value of True (if the operands are equal) or False (if the operands are not equal)
print('Equality:\t\t', nil , '==' , num , nil == num)
# compares unicodes so A (Unicode 65) will not be equal to a (Unicode 97)
print('Equality:\t\t', cap , '==' , low , cap == low)
print('Inequality:\t\t', nil , '!=' , top , nil != top)
print('Greater:\t\t', nil , '>' , top , nil > top)
print('Greater or Equal:\t', nil , '>=' , top , nil >= top)
print('Lesser:\t\t\t', nil , '<' , top , nil < top)
print('Lesser or Equal:\t', nil , '<=' , top , nil <= top)

