marks_of_student1=int(input("marks of student1:- "))
marks_of_student2=int(input("marks of student2:- "))
marks_of_student3=int(input("marks of student3:- "))
marks_of_student4=int(input("marks of student4:- "))
marks_of_student5=int(input("marks of student5:- "))
#x is the list in unsorted order
x=[marks_of_student1, marks_of_student2, marks_of_student3, marks_of_student4, marks_of_student5]
#to sort the elements in list we use variable.sort() function
x.sort()
print("Marks in sorted list:- ", x)
