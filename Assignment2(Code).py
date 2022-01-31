#Q1

#Forming the given string.
a=str('Python is a case sensitive language')
#(a)

#For length of the string we use len() function.
print(len(a))
#(b)

#Reversing the string using slicing.
str_reverse=a[::-1]
print(str_reverse)
#(c)

#Using slicing to make another string.
new_string=a[10:26]
print(new_string)
#(d)

#Replacing "a case sensitive" with "object oriented" using replace() function.
a_replace=a.replace("a case sensitive", "object oriented")
print(a_replace)
#(e)

#To find the location of the substring we use index() function.
print(a.index("a"))
#(f)

#To remove white spaces we can replace the white space with no space.
print(a.replace(" ", ""))

print("\n")

#Q2

#Storing name,SID, department name and CGPA in respective variables.

name="Rajat Garg"
SID=21104032
department_name="EE"
CGPA="9.9"

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))

print("\n")


#Q3
# Initiating a and b with values 56 and 10 respectively
a=56
b=10

#(a)
# Implementing bit-wise operator & (and)
print(a&b)

#(b)
# Implementing bit-wise operator | (or)
print(a|b)
#(c)
#Implementing bit-wise operator ^ (XOR)
print(a^b)

#(d)
# Implementing bit-wise operator << (left shift)
a_new1=a<<2

b_new1=b<<2

print(a_new1)
print(b_new1)

#(e)
# Implementing bit-wise operator >> ( right shift operator)
a_new2=a>>2

b_new2=b>>4

print(a_new2)
print(b_new2)

print("\n")

#Q4
#Taking input of three numbers as integers.
first_number=int(input("Enter the first number:- "))
second_number=int(input("Enter the second number:- "))
third_number=int(input("Enter the third number:- "))

#Using (if,else) conditional to find the greatest integer.
if (first_number>second_number) & (first_number>third_number):
    print(first_number)
elif (second_number>first_number) &(second_number>third_number):
        print(second_number)
elif (first_number==second_number==third_number):
    print("All are equal")
else:
    print(third_number)

print("\n")

#Q5

#Taking input statement
a=str(input("Write your sentence or word and I will tell you whether it contains 'name' or not:- \n"))
#Using (if,else) conditionals
if 'name' in a:
    print("Yes")
else:
    print("No")

print("\n")

#Q6
#Taking sides as input
first_side=int(input("Enter the first side of the triangle:- "))
second_side=int(input("Enter the second side of the triangle:- "))
third_side=int(input("Enter the third side of the triangle:- "))
#Using (if,else) conditional
if(first_side+second_side>=third_side)&(first_side+third_side>=second_side)&(third_side+second_side>=first_side):
    print("The triangle can be formed")
else:
    print("The triangle cannot be formed")

    print("\n")
