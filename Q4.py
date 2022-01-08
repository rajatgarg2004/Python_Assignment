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
print("Marks in sorted list:- ", x)
