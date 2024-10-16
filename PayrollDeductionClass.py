#PayrollDeductionClass.py - Write a class that represents a payroll deduction transaction. 
#Each instance should have the description, date, charge amount and employee ID as attributes. 
#The class’s __init__ method should accept an argument for each attribute. 
#The class should have accessor methods for each attribute. 
#All attribute should be hidden.
class PayrollDeduction:
    def __init__(self, desc, date, amt, num):
        self.__description = desc
        self.__date = date
        self.__charge = amt
        self.__id_number = num

    def set_description(self, desc):
        self.__description = desc
        return self.__description

    def get_description(self):
        return self.__description
    
    def set_id(self, num):
        self.__id_number = num
        return self.__id_number
    
    def get_id(self):
        return self.__id_number

    def set_date(self, date):
        self.__date = date
        return self.__date
    
    def get_date(self):
        return self.__date

    def set_charge(self, amt):
        self.__charge = amt
        return self.__charge
    
    def get_charge(self):
        return self.__charge