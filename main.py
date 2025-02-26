print("Hello World")
print("I like Roti")
# comments
'''This is another comment'''

# Variables : It is a storage container for a value..
# Strings
demo_variable = "Gautam"
print(demo_variable)#don't add quotes while calling a variable

#inserting variables in string
print(f"How are you {demo_variable}?")

# Integers
age = 16

print(f"you are {age} years old na..")

#floats
price = 10.88
print(f"The Price of Roti is ${price}")

gpa = 3.2
print(f"your gpa is {gpa}")

distance = 5.5
print(f'you ran {distance} K.M.')

#boolean
is_student = True
print(f"are you a student?:{is_student}")

'''TypeCasting: Converting one variable datatype to another'''
name = "Gautam"
age = 17
percentage = 94.38
is_student = True

percentage = int(percentage)
age = float(age)
print(age)
print(type(age))
print(type(is_student))
print(type(percentage))

'''User Input'''
input("HeyENTERSomething: ")

# Exercise 1 : Calculating the area of a rectangle
length = float(input("Please Enter length of Rectangle: "))
breadth = float(input("Please Enter Width of Rectable: "))
print(f"The area of the Rectangle is: {length*breadth}")

#o Arithmetics and Maths

friends = 0
friends = friends + 1

# abs() - Gives absolute distance of a number from 0 on a no line
# pow(a,b) - a to the power b
# min(a,b,c) - returns the minimum value
# max(a,b,c) - returns the maximum value

# math module
import math

print(math.e)
print(math.pi)
print(math.sqrt(3))
print(math.ceil(32))

# Exercise : Calculation of circumference of circle

inp = int(input("Enter the radius"))
print(f"Circumference:{round(2*math.pi*inp,2)}")

# Exercise : Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds?(K or L): ")
if unit == "K":
    weight = weight * 2.205
    unit = "LBS"
    print(f"Your weight is : {round(weight,1)}{unit}")
elif unit == "L":
    weight = weight / 2.205
    unit = "KGS"
    print(f"Your weight is : {round(weight,1)}{unit}")
else:
    print("Please Enter a valid unit.")

# String METHODS
name = input("Enter your full Name: ")

# length : PRINTS THE LENGTH OF THE STRING
len(name) # -> Length of string name
result = name.find(" ")#-> For finding the position of a sub string in a string. It always finds the first occuerence.
result = name.rfind(" ")#-> For finding the last occuerence of a sub string in a string.
print(result)
name = name.capitalize()#-> For capitalising the string
name = name.upper()#-> For Upper casing the string
name = name.lower()#-> For Lower casing the string
name.isdigit()#-> True if the string only contains digits and false if not.
name.isalpha()#->TRue if only alphabets are present and false otherwise.

name.replace("substring1","substring2")#-> For replacing a substring with other subs string

#EXERCISE : Validate user input

username = input("Please Enter your username: ")


# CONDITION FOR LENGTH
if len(username)>12:
    print("Username Must be Under 12 Characters.")
elif username.isalpha() == False:
    print("Please Remove any Spaces or Numbers from the Username.")
else:
    print('The Username is Valid Thank You.')

#STRING INDEXING
crad = "32.0-23323-23"
# crad[0] would give 3 as it is the character at the 0th index of crad string
# crad[0:4] would give 32.0- as python would start from 0th index and go uptil 4th index of crad string

# crad[-2] would give - because it starts counting from the last string as 0 and then goes till -2 index.


#WHILE LOOP

#Compound Interest Calculator
principle = 0
rate = 0
time = 0
while principle<=0:
    principle = float(input("Enter the Principle amount:"))
    if principle<=0:
        print("Principle Can't be less than or equal to 0")
while rate<=0:
    rate = float(input("Enter the rate amount:"))
    if rate<=0:
        print("rate Can't be less than or equal to 0")
while time<=0:
    time = int(input("Enter the time in Years:"))
    if time<=0:
        print("time Can't be less than or equal to 0")

# Happy NEW YEAR WIsh
import time
for i in reversed(range(1,11)):
    print(i)
    time.sleep(2.00)
print("HAPPY NEW YEAR")

# LISTS IN PYTHON
fruits = ['apples','banana','orange','coconaut']
print(fruits) #-> Prints the list
print(fruits[0])#-> Prints the element of the 0th index in fruits list.
print(fruits[::2])#->prints the element stepping 2 after printing a element in index.
# print(dir(fruits))#-> Name the methods of the collection.
# print(help(fruits))#-> Description of all the methods of collection
print(len(fruits))#-> Prints the fruits list length
print("Pineapple" in fruits)#-> Return false as pineapple is not present in fruits

fruits.append("pineapple")
# fruits.remove('apples')
# fruits.clear()
print(fruits)
print(fruits.index('apples'))

# SETS IN PYTHON
fruits = {'apples','banana','orange','coconaut'}
print(len(fruits))
print(type(fruits))
# sets cannot be indexed 
# print(fruits[3])  #-> would return a error

# TUPLES IN PYTHON
fruits = ('apples','Mangoes','eals',32,2.03)
print(fruits)

EXERCISE : Shopping Cart Program
foods = []
prices = []
total = 0
while True:
    food = input("Enter a Food to Buy: ")
    if food.lower() == 'q':
        break
    else:
        price = input("Enter the price: ")
        prices.append(price)
        foods.append(food)
print("Your Cart: ")
for food in foods:
    print(food, end=" ")
for price in prices:
    total = total+int(price)
print(f"\nyour total is {total}")

# 2D LISTS
keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
for keylist in keypad:
    for keys in keylist:
        print(keys, end=" ")
    print("\n",end="")
# GETTING RANDOM NUMBERS IN PYTHON
import random
print(help(random))
num = random.randint(1,6)
print(num) #-> would return a random number.
# random.choice() -> Returns a choice from a dataset

# EXERCISE : Number Guessing Game.
hidden_num = random.randint(1,100)
while True:
    try:
        user_choice = int(input("Enter your Guess: "))
        if user_choice<hidden_num:
            print("Number is Bigger!")
        elif user_choice>hidden_num:
            print("Number is Smaller!")
        elif user_choice==hidden_num:
            print("Alright! You got it!")
            print(f"{hidden_num} is the correct number")
            break
        else:
            print("Your Choice is not a number! Please Enter a Number")
    except Exception as e:
        print("Something You Entered is not a number! Please enter a Number")
# EXERCISE : ROCK, PAPER, SCISSORS GAME
options = ["R","P","S"]
while True:
    computer_selected_option = random.choice(options)
    user_selected_option = input("Enter Your Choice:(R,P,S) and Q to quit: ")
    print(
f"""User: {user_selected_option}
Computer:{computer_selected_option}""")
    if computer_selected_option == user_selected_option:
        print('its a draw')
    elif computer_selected_option=="R" and user_selected_option=="S":
        print("Computer Won")
    elif computer_selected_option=="R" and user_selected_option =="P":
        print("You Won")
    elif computer_selected_option=="S" and user_selected_option == "P":
        print("You Lost!")
    elif computer_selected_option == "S" and user_selected_option=="R":
        print("You Won!")
    elif computer_selected_option=="P" and user_selected_option == "S":
        print("you won")
    elif computer_selected_option=="P" and user_selected_option == "R":
        print("You Lost!")
    elif user_selected_option == "Q":
        print("Thank You for Playing")
        break
    else:
        print("You Chose a Wrong Option Please Choose the Right One")
# No Notes for Functions

# Default Arguments: which are sent by default
def hello(name,hello="Gautam"):#-> Here hello = "Gautam" is a default argument
    print(f"HELLO {hello}. You are great {name}")

hello(hello="Gautam", name="Gautam")#-> This is a Keyword Argument and the order of the arguments doesn't matter

# Member ship Ooperators : Used to test whether a value of variable is found in a sequence(string, list, tuple, set, or dictionary)
# 1. in
# 2. not in 
students = {"spongebob","Patrick","Sandy"}
student = input("Enter the name of Student: ")
if student not in students:
    print(f"The {student} was not found in Students")
else:
    print(f"The {student} is a student")

grades = {"Sandy":"A", "Squidward":"B","Spongebob":"C","Patrick":"D"}
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} was not found")

email = "gautamgs20012008@gmail.com"
if "@" in email and "." in email:
    print("Email is Valid!")
else:
    print("Email is not Valid")

# LIST COMPREHENSION IN PYTHON
doubles = []
for item in range(1,11):
    doubles.append(item*2)
print(doubles)
# Same above thingy in compact form
doubles = [x*2 for x in range(1,11)]
print(doubles)
triples = [y*3 for y in range(1,21)]
print(triples)
squares = [z*z for z in range(1,11)]
print(squares)

family = ['Pranav','Gautam',"Sonu",'Raju',"Santosh Rani"]
family_upper = [fam.upper() for fam in family]
print(family_upper)
print(help("modules spam"))
