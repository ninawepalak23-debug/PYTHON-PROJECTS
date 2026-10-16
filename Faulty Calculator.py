#Make a faulty calculator which answers all answers correctly
# except 45*3=555, 56+9=77, 56/6=4
print('Welcome to the calculator!')
num1=int(input('Enter first number: '))
print("Operators you can use are +,-,*,/")
oper=input('Enter operator you want to use: ')
print("num2 should not be equal to 0, as it would show error while performing division")
num2=int(input('Enter second number: '))
if (num1,num2)==(45,3) or (num1,num2)==(3,45) and oper=='*':
    print('The answer is 555')
elif (num1,num2)==(56,9) or (num1,num2)==(9,56) and oper=='+':
    print('The answer is 77')
elif(num1,num2)==(56,6) and oper=='/':
    print('The answer is 4')
else:
    if oper=='+':
        ans=num1+num2
    elif oper=='-':
        ans=num1-num2
    elif oper=='*':
        ans=num1*num2
    elif oper=='/':
        ans=num1/num2
    else:
        print('Not a specified operator')
    print('The answer is ', ans)
    print('Thank You for using Calculator. Have a good day.')