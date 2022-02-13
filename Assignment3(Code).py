#Q1
#Input the string, lower casing the letters and splitting them
print("Question 1")
input_string = input("Enter the string: ").lower().split()
#For a single letter

if len(input_string)==1:
    input_string = input_string[0]
#Making an empty list to enter the occurences a letter/word

occurences ={}

for i in input_string:
    if i in occurences:
        occurences[i] +=1
    else:
        occurences[i]=1
print("The occurence of: ")

for i in occurences:
    print((i,occurences[i]))
print()
print("-"*80)
print()


#Q2
print("Question 2")
#Defining a function of leap year

def is_leap(year):
    
    if year%4==0:
        leap=True
    else:
        leap=False
    return leap
print("To find the next date:- \n")
#To continue or break loop for the date given

while(True):
    day= int(input("Enter the Day: "))
    month=int(input("Enter the Month: "))
    year=int(input("Enter the year: "))
    
    if month<1 or month>12:
        print("Date entered is out of range.")
    
    elif day<1 or day>31:
        print("Date entered is out of range.")
    
    elif year<1800 or year>2025:
        print("Date entered is out of range.")
    
    elif month in [4,6,9,11]:
        if day<=30:
            continue
    
    elif year%4!=0:
          if month==2:
              if day>28:
                  print("Invalid date")
    
    else:
        break
return_day= day
return_month=month
return_year=year
#Using if-else conditionals for different days and months

if month in [4,6,9,11]:
    if day<=30:
        if return_day !=30:
            return_day+=1
        else:
            return_month+=1
            return_day=1

elif month in [1,3,5,7,8,10]:
    if day!=31:
        return_day+=1
    else:
        return_month+=1
        return_day=1

elif month ==12:
    if day==31:
        return_day=1
        return_month=1
        return_year+=1

elif month==2:
    if is_leap(year):
        if day>29:
            print("Data entered is out of range.")
        
        elif day== 29:
            return_day=1
            return_month+=1
        else:
            return_day+=1
    else:

        if day==28:
            return_day=1
            return_month+=1
        else:
            return_day+=1
#Printing the date.
return_date=f"{return_day}/{return_month}/{return_year}"
print("The Next Date is : ", return_date)
print()
print("-"*80)
print()


#Q3
#Taking input of the numbers 
print("Question 3")
numbers=input("Enter the list of numbers(Also add space between 2 numbers): ")
#Making a list for integers
int_list=list(map(int,numbers.split()))
#Making a list for adding tuples
result_list=[]
#Using for loop to add the tuples in result_list

for i in int_list:
    result_list.append((i,i**2))
print()
print(result_list)
print()
print("-"*80)
print()


#Q4
#Taking input of the Grade.
print("Question 4")
a=int(input("Enter the Grade:- "))
#Using if-else conditionals for the grades entered.

if(a<4 or a>10):
    print("Error. Enter the number between 4-10")

elif(a==10):
    print("Your Grade is 'A+' and Outstanding Performace")

elif(a==9):
    print("Your Grade is 'A' and Excellent Performace")

elif(a==8):
    print("Your Grade is 'B+' and Very Good Performace")

elif(a==7):
    print("Your Grade is 'B' and Good Performace")

elif(a==6):
    print("Your Grade is 'C+' and Average Performace")

elif(a==5):
    print("Your Grade is 'C' and Below Average Performace")

elif(a==4):
    print("Your Grade is 'D' and Poor Performace")

print()
print("-"*80)
print()


#Q5
print("Question 5")
n = 6
#Creating a pattern by adding letters according to ascii values using for loop.

for i in range(n):
    
    for j in range (i):
        print(" ", end='')
    
    for k in range (2*(n-i)-1):
        print(chr(65+k), end='')
    print()

print()
print("-"*80)
print()


#Q6
# To  store the Informationrmation of the students
print("Question 6")
Input = "Y"
SID_Information = {}

while Input == "Y":
    Name = input("Enter the Name of the Student:- ")
    SID  = int(input("Enter the SID of the Student:- "))
    SID_Information[SID] = Name

    while True:
        Input = input(
            "Type 'Y' if want enter another Student's Information or Type 'N' if don't want to Enter:- "
        ).upper()

        if Input == "Y" or Input =="N":
            break
        else:
            print("\nEnter The Correct Input")
    
    if Input == "N":
        break
    
#part a.) Print the dictionary
print(SID_Information)
##part c.) sort according to the SIDs
Sorted_SIDs = sorted(SID_Information.keys())
SID_Sort = {}

for sid in Sorted_SIDs:
    SID_Sort[sid] = SID_Information[sid]


#part b. sort according to the names
Sorted_Names = sorted(SID_Information.values())
Name_Sort = {}


def get_key(val, dicti):
    
    for key, value in dicti.items():
        if val == value:
            return key


for s_name in Sorted_Names:
    s_sid = get_key(s_name, SID_Sort)
    Name_Sort[s_sid] = s_name
#Printing the sorted Names
print(Name_Sort)
#Printing the sorted SIDs
print(SID_Sort)

while True:
    SID_Find = int(input("Enter the SID to find the name:- "))

    if SID_Find in SID_Information:
        print(SID_Information[SID_Find])
        break
    else:
        print("\nEnter the SID that is already in the list")

print()
print("-"*80)
print()


#Q7
#Taking input for the terms required.
print("Question 7")
Total_Terms=int(input("Enter the number of fibonacci terms you want:- \n"))
First_Term=0
Next_Term=1
Nth_Term=0
Sum=0
#Using for loop to get the n terms

for i in range(1,Total_Terms+1):
    
    if(i==1):
        print(0)
    elif (i==2):
        print(1)
        Sum=Sum+1
    else:
        Nth_Term=First_Term+Next_Term
        Sum=Sum+Nth_Term
        print(Nth_Term)
        First_Term=Next_Term
        Next_Term=Nth_Term
print("The Average of the numbers is:-", float(Sum/Total_Terms))

print()
print("-"*80)
print()


#Q8
#Initializing the Sets
print("Question 8")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
#Using prebuilt functions union() and intersection().
#a)
#A new set of all elements that are in Set1 and Set2 but not both.
a=(Set1.union(Set2))-(Set1.intersection(Set2))
#b)
#A new set of all elements that are in only one of the three sets Set1, Set2 and Set3.
b=(Set1.union(Set2.union(Set3))) - (Set1.intersection(Set2)) - (Set1.intersection(Set3)) - (Set2.intersection(Set3))
#Sorting the set
b=set(sorted(b))
#c)
#A new set of elements that are exactly two of the sets Set1, Set2 and Set3.
c=(Set1.intersection(Set2)).union((Set2.intersection(Set3)).union(Set1.intersection(Set3)))
#d)
#A new set of all integers in the range 1 to 10 that are not in Set1.
d=set()
for i in range (1,11):
    if i not in Set1:
        d.add(i)
#Sorting the set
d=set(sorted(d))
#e)
#A new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
e=set()
for i in range (1,11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        e.add(i)
#Sorting the Set
e=set(sorted(e))
#Printing all the sets
print("Set1 = ", Set1)
print("Set2 = ", Set2)
print("Set3 = ", Set3)
print("a.) \n")
print(a, '\n')
print("b.) \n")
print(b, '\n')
print("c.) \n")
print(c, '\n')
print("d.) \n")
print(d, '\n')
print("e.) \n")
print(e)
print()
print("-"*80)
print()
