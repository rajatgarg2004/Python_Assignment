#Q1
#Take input for 3 integers
num1=int(input("Write your first number:-"))
num2=int(input("Write your third number:-"))
num3=int(input("Write your second number:-"))
#The formula for average of the 3 numbers is
average=float((num1+num2+num3)/3) 
print('The average of the 3 numbers is ', average, '\n')

#Q2
#Take input of the gross income
Gross_income=float(input("Gross Income in Dollars(USD):- "))
#Take input of the number of dependents
Number_of_dependents=int(input("Number of Dependents:- "))
#Taxable income = Gross Income - Standard deduction-(Dependent deduction * No. of dependents)
#Standard Deduction=10000$, Dependent Deduction=3000$
Taxable_income=float(Gross_income-10000-3000*Number_of_dependents)
#Tax = Taxable income * Tax Rate
#Tax Rate=20%
Tax=float(Taxable_income*20/100)
if Tax>0:
    print("Your Tax is ", Tax, "$", '\n')
else:
        print('Your income tax is not valid', '\n')

#Q3
#Take input of the Student ID
SID=int(input("Write your SID:- "))
#Take input of the name 
Name=str(input("Write your Full Name:- "))
#Take input of the Gender
Gender=str(input("Write your Gender(M/F/U):- "))
#Take input of of the course pursued
Course=str(input("Write your Course Name:- "))
#Take input of the CGPA
CGPA=float(input("Write your CGPA:- "))
#StudentID in List format 
Student= [SID, Name, Gender, Course, CGPA]
print("Student:- ", Student, '\n')

#Q4
#Take Input of the marks of the students
marks_of_student1=int(input("Marks of student1:- "))
marks_of_student2=int(input("Marks of student2:- "))
marks_of_student3=int(input("Marks of student3:- "))
marks_of_student4=int(input("Marks of student4:- "))
marks_of_student5=int(input("Marks of student5:- "))
#x is the list in unsorted order
x=[marks_of_student1, marks_of_student2, marks_of_student3, marks_of_student4, marks_of_student5]
#to sort the elements in list we use variable.sort() function
x.sort()
print("Marks in sorted list:- ", x, '\n')

#Q5(a)
#Making colour list of the given colors
colour_list=['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
#To remove an element we use pop function
colour_list.pop(3)
print('The list after removing the 4th element :-', colour_list, '\n')
#Q5(b)
#Making colour list of the given colors
colour_list=['Red','Green', 'White', 'Black', 'Pink', 'Yellow']
#To add an element we use insert function
colour_list.insert(3, "Purple")          
print('The updated colour list after removing "Black" and "Pink" and replacing them with "Purple" :-', colour_list[0:4] + colour_list[6:], '\n')

