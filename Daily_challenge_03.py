a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b and c:
    print("Largest number is:",a)
elif b>a and c:
    print("Largest number is:",b)
elif c>a and b:
    print("Largest number is:",c)
else:
    print("You have entered a invalid number")