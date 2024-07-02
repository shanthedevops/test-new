
print("Small programe to calculate")
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
print("What you want to operation ","1.Add,2.sub,3.multiply,4.divide" )
result=input("")
if((result=="add")or(result== "1")):
    add = num1 + num2
    print("Two number of add:= ",add )
elif((result== "sub")or (result=="2")):
    sub = num1 - num2
    print("Two number of sub:= ",sub)
elif((result=="multiply")or(result=="3")):
    multiply = num1 * num2
    print("Two number of multiplication:= ", multiply)
elif((result=="divide")or(result=="4")):
    divide = num1 / num2
    print("Two number of divide:= ",divide)
else:
    print("invalid enter")