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
print("Student:- ", Student)
