'''
Develop a Python program that accepts an employee’s basic salary as input and
calculates their bonus based on the following conditions:
i. If the salary is above 50,000, the bonus is 15% of the salary.
ii. If the salary is between 30,000 and 50,000, the bonus is 10% of the
salary.
iii. If the salary is below 30,000, the bonus is 5% of the salary.
The program should print the total salary including the bonus.
'''

'''
name = str(input("Enter Employee Name:"))
salary = float(input(f"Enter Salary of {name}: "))
print()
print("Employee:    ",name)
print("Salary:      ",round(salary,2))
if salary > 50000:
    bonus = 0.15
elif 30000< salary <= 50000:
    bonus = 0.1
elif 0< salary <=30000:
    bonus = 0.05
elif salary <=0 or salary >50000:
    print("Salary out of range!")
total_salary = round(salary+(salary*bonus),2)
print(f"Total Salary of {name} including Bonus is: {total_salary}")
'''

'''
Develop a Python program with a menu-driven system to perform temperature
conversions using functions. The menu should include:
i. Celsius to Fahrenheit F=(C×9/5) +32
ii. Fahrenheit to Celsius C=(F−32) ×5/9
Each option should be handled using a separate function.
'''
flag = True
def c_to_f(c):
    return round((c*9/5) +32,3)
def f_to_c(f):
    return round((f-32)*(5/9),2)
while flag:
    print("""
====== Temperature Conversion ======
1       Celcius to Farenheit
2       Farenheit to Celcius
3       Exit Program
""")
    choice = int(input("Enter Your Choice: "))
    if choice ==1:
        c = float(input("Enter Temperature in Celcius: "))
        f = c_to_f(c)
        print(f"{c}C is {f}F")
    elif choice ==2:
        f = float(input("Enter Temperature in Farenheit: "))
        c = f_to_c(f)
        print(f"{f}F is {c}C")
    elif choice ==3:
        flag = False
        print("Exiting Program!")
    else:
        print("Invalid Input!")