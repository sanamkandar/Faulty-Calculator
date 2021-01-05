# the faulty calculator
while True:
    operater = input("CHOOSE YOUR OPERATER addition , multiplication , divison : ")
    num1 = int(input("ENTER YOUR 1ST NUMBER: "))
    num2 = int(input("ENTER YOUR 2ND NUMBER: "))

    if operater=="addition" and num1==56 and num2==9:
        print("sum is 77")
    elif operater=="multiplication" and num1==45 and num2==3:
        print("Multiplication of this two numbers is 555")
    elif operater=="divison" and num1==56 and num2==6:
        print("divison is 4")
    elif operater=="addition":
        print("sum is", num1+num2)
    elif operater=="multiplication":
        print("Multiplication of this two numbers is", num1*num2)
    elif operater=="divison":
        print("divison is ", num1/num2)
    else:
        print("INVALID INPUT")

