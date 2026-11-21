import math
print("====CALCULATOR====")

a = int(input("Enter the first no. : "))
b = int(input("Enter the second no. : "))
print("choose the operator from the folllowing : ")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
op = input("Tell the operator :")

while True :    
    def calculate(a,b,op):
        if op == "+":
            result = a + b
            print("Result is : " , result)
        elif op =="-":
            result = a - b
            print("Result is : ", result)
        elif op =="*":
            result = a * b 
            print("Result is : " , result)
        elif op =="/":
            result = a/b
            print('Result is : ' , result)
        else:
            print("Wrong input . Check again !")
            return result
        
    break

                    

