num1=int(input('Enter number1: '))
num2=int(input('Enter number2: '))
op=input('Enter a operator: ')
if op=='+':
    print('Addition is: ',num1+num2)
elif op=='-':
    print('Subraction is: ',num1-num2)
elif op=='*':
    print('Multliplication is: ',num1*num2)
elif op=='/':
    print('Division is: ',num1/num2)
else:
    print('Invalid operator')