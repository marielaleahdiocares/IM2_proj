print ("Enter first number")
num1 = int (input ())

print ("Enter first number")
num2 = int (input ())

print ("Operator: ")
operator = input ()

if operator == "+":
    result = num1 + num2
if operator == "-":
    result = num1 - num2
if operator == "/":
    result = num1 / num2
if operator == "*":
    result = num1 * num2

print(f"Total:{result}")
