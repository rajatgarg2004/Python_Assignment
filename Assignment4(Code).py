#Q1
print("\nQ1 \n")
#Defining a function with use of recursion
def TowerOfHanoi(n , Tower1, Tower3, Tower2):
	if n == 0:
		return 0
	TowerOfHanoi(n-1, Tower1, Tower2, Tower3)
	print("Move disk",n,"from rod",Tower1,"to rod",Tower3)
	TowerOfHanoi(n-1, Tower2, Tower3, Tower1)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print("\n")
print("-"*80)
print("\n")
#Q2
print("\nQ2 \n")
from tracemalloc import start
def fact(n):
  fact=1
  for i in range(1,n+1):
    fact=fact*i
    i+=1
  return(fact) 
n=int(input('Enter the number of rows for pascals triangle '))

print("Using Loops :-")

for i in range(n):
	for j in range(n-i+1):
  #for spacing
		print(end=" ")

	for j in range(i+1):
    # nCr = n!/((n-r)!*r!)
		print(fact(i)//(fact(j)*fact(i-j)), end=" ")	
    # for new line
	print()
print()


print("Using Recurssion:-")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")
print("-"*80)
#Q3
print("\nQ3 \n")
int1 = int(input("Enter the dividend:- "))
#Loop to make sure int2 != 0(i.e. denominator must not be 0)
while True:
    int2 = int(input("Enter the divisor:- "))
    if int2 != 0 and int2>0:
        break
    else:
        print("\nThe divisor must be greater than 0.\nPlease enter the divisor again.")
Quotient=int1//int2
Remainder=int1%int2

print("Quotient = ", Quotient)
print("Remainder = ", Remainder)

#part a)
print("a) \n")
print("Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))
print("\n")
print("- "*50)
print("\n")
#part b)
print("b) \n")
if (Quotient == 0 & Remainder == 0):
    print("Both quotient and remainder are zero. \n")
if (Quotient == 0 & Remainder !=0):
    print("Quotient is zero while remainder is non zero. \n")
if (Quotient != 0 and Remainder == 0):
    print("Quotient is non zero while remainder is zero. \n")
if (Quotient != 0 and Remainder != 0):
    print("Both quotient and remainder are non zero. \n")
print("\n")
print("- "*50)
print("\n")
#part c)
print("c) \n")
list = [Quotient + 4, Remainder + 4, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f"The filtered numbers that are greater than 4 are : {result} \n")
print("- "*50)
print("\n")
#part d)
print("d) \n")
setresult = set(result)
print("Set:",setresult) 
print("\n")
print("- "*50)
print("\n")
#part e)
print("e) \n")
immutableSet = frozenset(setresult)
#Frozen Set makes the set immutable.
print("Immutable set:- ",immutableSet)
print("\n")
print("- "*50)
print("\n")
#part f)
print("f) \n")
print("Hash value of the max value from the above set:- ", hash(max(immutableSet)))
print("\n")
print("-"*80)
#Q4
print("\nQ4 \n")
class Student:
    def __init__(self, student,rollno):
        self.name = student
        self.rollno = rollno

    def __del__(self):
        print("Object deleted.")


#Creating object
student1 = Student("Rajat", 21104032)
print("Object created")
#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.rollno}.")
#deleting object
del student1
print("\n")
print("-"*80)
#Q5
print("\nQ5 \n")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_data(self):
        print("%s has a salary of %d rupees" % (self.name,self.salary))
#Creating Employee records 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
#Printing the initial values
print("The current database is:")
for i in [employee1,employee2,employee3]:
    i.print_data()

#a) Updating salary
employee1.salary = 70000
print("a) \n")
print(f"The updated salary of {employee1.name} is {employee1.salary} \n")
print("\n")
print("- "*50)
print("\n")
#b) Deleting a record
print("b) \n")
print("Record of Viren deleted", end='')
del employee3
print("\n")
print("-"*80)

#Q6
print("\nQ6 \n")
#Defining anagram function
def anagram(word):
    if len(word)==1:
        return [word]
    other_words=anagram(word[1:])
    char=word[0]
    list1=[]
    for combination in other_words:
        for i in range(len(combination)+1):
            list1.append(combination[:i]+char+combination[i:])
    return list1      


George_word=input("George's word:-").lower()
Barbie_word=input("Barbie's word:-").lower()
other_words=anagram(George_word)
print("Other possible words are:",other_words)
print("If Barbie's word is present in the list , then their friendship is real. \n")

if Barbie_word in other_words:
    print("The Friendship is real.")
else:
    print("The Friendship is fake.")
print("-"*80)
