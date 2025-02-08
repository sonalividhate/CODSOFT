print("----Mini Calculator----")
num1 = float(input("Enter a number here: "))
num2 = float(input("Enter another number here: "))

print("""
      press 1 for addition
      press 2 for subtraction
      press 3 for multiplication
      press 4 for Division""")

choice =int(input("Enter a numbers "))

if choice ==1:
    sum=num1+num2
    print("the addition of the given two numbers is ",sum)
elif choice ==2:
    sub=num1-num2
    print("the subtraction of the given two numbers is ",sub)
elif choice ==3:
    multi=num1*num2
    print("the multiplication of the given two numbers is ",multi)
elif choice ==4:
    div=num1/num2
    print("the division of the given two numbers is ",div)
else:
    print("Invalid input")