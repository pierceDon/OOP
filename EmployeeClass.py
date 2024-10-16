class Employee:
    def __init__(self, name, num, dept, job, pay):
        self.__emp_name = name
        self.__id_number = num
        self.__department = dept
        self.__job_title = job
        self.__monthly_salary = pay

    def set_emp_name(self, name):
        self.__emp_name = name
        return self.__emp_name
    
    def get_emp_name(self):
        return self.__emp_name
    
    def set_id_number(self, num):
        self.__id_number = num
        return self.__id_number
    
    def get_id_number(self):
        return self.__id_number
    
    def set_department(self, dept):
        self.__department = dept
        return self.__department

    def get_department(self):
        return self.__department
    
    def set_job_title(self, job):
        self.__job_title = job
        return self.__job_title

    def get_job_title(self):
        return self.__job_title
    
    def set_monthly_salary(self, pay):
        self.__monthly_salary = pay
        return self.__monthly_salary
        
    def get_monthly_salary(self):
        return self.__monthly_salary
    
    def __str__(self):
        return f'''
Name | ID Number | Department | Job Title | Monthly Salary
{self.__emp_name} |{self.__id_number} |{self.__department} |{self.__job_title} |${format(self.__monthly_salary, ",.2f")}
'''