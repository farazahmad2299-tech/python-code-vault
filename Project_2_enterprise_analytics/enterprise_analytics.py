company_details = ("TechCrop_Solutions","Lahore","PKR")
print("="*100)
print("\t\t\t<<<==Welcome TO TechCorp Financial Analytics Engine==>>>")
print("="*100)
print("="*100)
# Employ Names in clean way and salaray 

employ = []

salary = []

# First Employ 
print("\t\t\t\t<--Employ 1 Section--> ")
print("="*100)
print("-"*40)
name_1 = input("\nEnter your Name :  ")
name_1 = name_1.title()
employ.append(name_1)
print("-"*40)
print(f"\nThe First Employ is : {name_1}" )

print("-"*40)
salary_1 = int(input(f"\nEnter {name_1} salary : "))
print("-"*40)
salary.append(salary_1)
print(f"\nThe salary of {name_1}  is : {salary_1}")

# Second Employ
print("-"*40)
print("\t\t\t\t<--Employ 2 Section-->")
print("="*100)
name_2 = input("\n\nEnter Your name : ")
print("-"*40)
name_2 = name_2.title()
employ.append(name_2)
print(f"\nThe Second Employ is : {name_2} ")
print("-"*40)

salary_2 = int(input(f"\nEnter the salary of {name_2} : "))
print("-"*40)
salary.append(salary_2)
print(f"\nSalary of {name_2} is : {salary_2}")
print("-"*40)

# Third Employ 
print("\t\t\t\t<--Employ 3 Section--> ")
print("="*100)
print("-"*40)
name_3 = input("\nEnter your Name :  ")
name_3 = name_3.title()
employ.append(name_3)
print("-"*40)
print(f"\nThe Third Employ is : {name_3}" )

print("-"*40)
salary_3 = int(input(f"\nEnter {name_3} salary : "))
print("-"*40)
salary.append(salary_3)
print(f"\nThe salary of {name_3}  is : {salary_3}")

# Fourth Employ
print("-"*40)
print("\t\t\t\t<--Employ 4 Section-->")
print("="*100)
name_4 = input("\n\nEnter Your name : ")
print("-"*40)
name_4 = name_4.title()
employ.append(name_4)
print(f"\nThe Fourth Employ is : {name_4} ")
print("-"*40)

salary_4 = int(input(f"\nEnter the salary of {name_4} : "))
print("-"*40)
salary.append(salary_4)
print(f"\nSalary of {name_4} is : {salary_4}")
print("-"*40)

# Report Generation 
print("\t\t\t\t<<==FULL REPORT==>>")
print("="*100)

# Company details 

print(f"Company Name : {company_details[0]} \nLocation : {company_details[1]} \nCurrency : {company_details[2]}")
print("-"*40)
# <--total employs--> 

total_employs = len(employ)
print(f"\nTotal Employs are : {total_employs}")
print("-"*40)

# <--Sum of salaries-->
sum_of_salary = sum(salary)
print(f"\nTotal Salary Expensis :{sum_of_salary} ")
print("-"*40)

# <--Highest Salary , Lowest Salary and Averge Salary-->

print(f"\nThe Highest Employ Salary is : {max(salary)}")
print("-"*40)

print(f"\nThe Lowest Employ Salary is : {min(salary)} ")
print("-"*40)

print(f"\nThe Average Salary of an Employ is {sum_of_salary/total_employs}")
print("-"*40)
print("\t\t\t\tPROGRAM ENDED")
print("="*100)

