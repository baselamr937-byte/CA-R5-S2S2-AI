"""Interactive Console-Based Calculator Module.

This module provides fundamental arithmetic operations (addition,
subtraction, multiplication, division) wrapped in an interactive
console loop for repeated user calculations.
"""

from caluclator_functions import addition,subtraction,multiplication,division

while True:
    system=input("choose an operation from the following list: \n- Addition \n- Subtraction\n- Multiplication \n- Division \n- Exit \n")
    if system.lower() in ["exit", "e"]:
        print("Exiting calculator. Goodbye!")
        break

    # 2. التأكد إن الاختيار صحيح قبل طلب الأرقام
    valid_operations = ["addition", "+", "subtraction", "-", "multiplication", "*", "x", "division", "/","%"]
    if system.lower() not in valid_operations:
        print("Invalid choice! Please choose a valid operation.")
        continue
    
    x=float(input("enter first number  \n   "))
     
    y=float(input("enter second number \n   "))
    
    if y==0 and (system=='/' or "Division" or '%'):
        print("could't divsion by 0 \n enter a valid divisor")
        
        y=float(input("enter second number \n   "))

    if system in ["Addition" , '+']:
        addition(x,y)
        
    if system in ["Multiplication" , '*' , 'x']:
        multiplication(x,y)
        
    if system in ["Subtraction" , '-']:
        subtraction(x,y)
            
    if system in ["Division" ,'/' ,'%']:
        division(x,y)
if __name__ == "__main__":
    print("Calculator module executed directly.")
