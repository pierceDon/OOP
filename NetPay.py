# '''
# EmployeeClass.py - 
# Write a class named Employee that holds the following data about an employee in attributes: name, ID number, department, job title and monthly salary.
# The Employee class’s __init__ method should accept an argument for each attribute. 
# The Employee class should have accessor methods for each attribute. All attribute should be hidden.

# PayrollDeductionClass.py - 
# Write a class that represents a payroll deduction transaction. 
# Each instance should have the description, date, charge amount and employee ID as attributes. 
# The class’s __init__ method should accept an argument for each attribute. 
# The class should have accessor methods for each attribute. All attribute should be hidden.

# NetPay.py - write a program that will create the following employee instance as well as payroll deduction instances.
# '''

import EmployeeClass as ec
import PayrollDeductionClass as pd

def main():
    deduction = {
        'Description':[],
        'Date':[],
        'Amount Charged':[],
        'Employee ID':[]
        }
    emp_id = [39119,21547]
    date = ['8/14/2022','8/17/2022']
    amt = [22.50,15.25]
    food_court1 = pd.PayrollDeduction('food court',date[0],amt[0],emp_id[0])
    food_court2 = pd.PayrollDeduction('food court',date[1],amt[1],emp_id[1])
    deduction['Description'].append(food_court1.get_description())
    deduction['Date'].append(food_court1.get_date())
    deduction['Amount Charged'].append(food_court1.get_charge())
    deduction['Employee ID'].append(food_court1.get_id())
    deduction['Description'].append(food_court2.get_description())
    deduction['Date'].append(food_court2.get_date())
    deduction['Amount Charged'].append(food_court2.get_charge())
    deduction['Employee ID'].append(food_court2.get_id())
    cont = True
    emp_id = 58475
    while cont == True:
        if emp_id in deduction['Employee ID']:
            desc = ['gift contribution','vending machine','vending machine']
            date = ['8/12/2022','8/22/2022','8/5/2022']
            amt = [25.00,3,2.75]
            deduct = pd.PayrollDeduction(desc[0],date[0],amt[0],emp_id)
            deduction['Description'].append(deduct.get_description())
            deduction['Date'].append(deduct.get_date())
            deduction['Amount Charged'].append(deduct.get_charge())
            for x in range(1,len(desc)):
                deduction['Description'].append(deduct.set_description(desc[x]))
                deduction['Date'].append(deduct.set_date(date[x]))
                deduction['Amount Charged'].append(deduct.set_charge(amt[x]))
                deduction['Employee ID'].append(deduct.set_id(emp_id))
            cont = False
        else:
            emp = ec.Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)
            print(emp)
            deduction['Employee ID'].append(emp.get_id_number())

    print(f'''
Description:    {deduction["Description"]}
Date:           {deduction['Date']}
Amount Charged: {deduction["Amount Charged"]}
Employee ID     {deduction["Employee ID"]}
''')
    print(f'''
*** Employee Pay ***
Name: {emp.get_emp_name()}
ID Number: {emp.get_id_number()}
Department: {emp.get_department()}    
Gross Pay: {emp.get_monthly_salary()}
Net Pay: ${emp.get_monthly_salary() - sum(amt)}    
          ''')

main()
            



