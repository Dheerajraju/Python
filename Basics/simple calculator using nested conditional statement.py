a = float(input("enter the first number"))
b = float(input("enter the second number"))
operation = input("enter the operation (+,-,*,/):")

if operation == '+':
    result = a+b
elif operation == '-':
    result = a-b
elif operation == '*':
    result = a*b
elif operation == '/':
    if b !=0:
        result = a/b
    else:
        result("error")
else:
    result = "invalid opeation"

print("Result :",result)
