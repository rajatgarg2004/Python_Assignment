#Q1
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

#Q2

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




#Q3

int1, int2 = map(int,input("Enter 2 numbers:- \n").split())
Quotient = int1 // int2
Remainder = int1 % int2

#part a)
print("a) \n")
print("Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part b)
print("b) \n")
if (Quotient == 0):
    print("Quotient is zero.")
if (Remainder == 0):
    print("Remainder is zero.")
if (Quotient != 0 and Remainder != 0):
    print("All of the values are non-zero.")

#part c)
print("c) \n")
list = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(list)):
    if list[i] > 4:
        result.append(list[i])
print(f"The filtered numbers that are greater than 4 are : {result}")

#part d)
print("d) \n")
setresult = set(result)
print("Set:",setresult)

#part e)
print("e) \n")
immutableSet = frozenset(setresult)
#Frozen Set makes the set immutable.
print("Immutable set:- ",immutableSet)

#part f)
print("f) \n")
print("Hash value of the max value from the above set:- ", hash(max(immutableSet)))
print()

#Q4

class Student:
    def init1(self, student,rollno):
        self.name = student
        self.roll_no = rollno

    def del1(self):
        print("Object deleted.")

#Creating object
student1 = Student("Rajat", 21104032)
print("Object created")
#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.roll_no}.")
#deleting object
del student1
print("\n")

#Q5

class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
#Creating Employee records 
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#a) Updating salary
employee1.salary = 70000
print("a) \n")
print(f" The updated salary of {employee1.name} is {employee1.salary} ")
#b) Deleting a record
print("b \n")
print("Record of Viren deleted", end='')
del employee3
print("\n")

#Q6

#Input a word from the first friend
word =input("Enter the word: ")
word=word.lower()

#Input a meaningful word with the exact same letters.
testword = input("Enter a new meaningful word using the exact same letters to test your friendship: ")
testword=testword.lower()
#Defining dictionary
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
#Shopkeeper's input to verify the meaning of the word.
def userinput():
    if count_in_dict(word) != count_in_dict(testword):
        print("The letters aren't same, friendship is fake")
        return
    ans = input("Does the word makes sense?(y/Y or n/N )")

    if ans == 'y' or ans=='Y':
        print("The friends pass the friendship test")
    elif ans == 'n' or ans=='N':
        print("The word doesn't have a meaning, friendship is fake")
    else:
        print("Invalid input,try again with y/Y or n/N ")
        userinput()
userinput()
