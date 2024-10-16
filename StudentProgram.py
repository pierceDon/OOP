import StudentClass as sc

studentid = 1001
name = 'John'
dob = '10/15/2001'
classification = 'junior'

student1 = sc.Students(studentid,name,dob,classification)

student1.calc_age()
student1.register()

print(f"Student age is {student1.return_age()}")

print(f"Student can register between {student1.return_registration()}")