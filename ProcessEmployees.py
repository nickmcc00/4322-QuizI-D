'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file
infile = open("employee_data.csv", "r")

csvfile = csv.reader(infile, delimiter=',')

next(csvfile)



#create an empty dictionary
employee_info = []
new_salary = 0
percent_increase = .1

#use a loop to iterate through the csv file
for value in csvfile:
    employee_title = value[4]
    full_name = value[1] + " " + value[2]
    salary = float(value[5])
    salary_increase = salary * percent_increase
    new_salary = salary + salary_increase
    
    
    #check if the employee fits the search criteria
    if employee_title == 'CSR':
        employee_info.append([full_name, salary, new_salary])

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout
for info in employee_info:
    print("Manager Name: ", info[0], "Current Salary: ", '$' + format(float(info[1]), ','))
    
print()
print('=========================================')
print()


for info in employee_info: 
    print("manager Name: ", info[0], "New Salary: ", '$' + format(float(info[2]), ','))

print()   
        

        
    
