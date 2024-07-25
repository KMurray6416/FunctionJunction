    # Task 1

def multiply(local_num1,local_num2):
    return(local_num1 * local_num2)

def divide(local_num1,local_num2):
    if local_num2 == 0:
        return("CAN'T DIVIDE BY ZERO!")
    else:
        return(local_num1 / local_num2)

def add(local_num1,local_num2):
    return(local_num1 + local_num2)

def subtract(local_num1,local_num2):
    return(local_num1 - local_num2)

    # Task 2

print("Please select -\n" \
        "1. Multiply\n" \
        "2. Divide\n" \
        "3. Add\n" \
        "4. Subtract\n")

choice = int(input("Please choose from above, 1,2,3,4:"))

num1 = int(input("Enter your first number:")) 
num2 = int(input("Enter your second number:"))

if choice == 1:
    print(f" {num1} * {num2} =  {multiply(num1,num2)}")
    
elif choice == 2: 
    print(f" {num1} / {num2} =  {divide(num1,num2)}")

elif choice == 3: 
    print(f" {num1} + {num2} =  {add(num1,num2)}")

elif choice == 4: 
    print(f" {num1} - {num2} =  {subtract(num1,num2)}")

else:
    print("Please try again")