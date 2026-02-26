print ("Hello World😊")

print ("*" * 10)

x = 1 
y = 2
unit_price = 3

# variebles

students_count = 1000
rating = 4.99
is_published = False
course_name = "Python programming"
print(len(course_name))
print(course_name[0])
print(course_name[-1])
print(course_name[0:])
print(course_name[:3])
print(course_name[:])
print (students_count)

print(course_name.upper())
print(course_name.lower())
print(course_name.title())
print(course_name.find("pro "))

first = "Ntombenhle"
last = "Ngcobo"
fullName = first + " " + "\n" + last
# fullName = f"{first} \n {last}"
print(fullName)
print(len(first))



#numbers
import math
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.9))


 #input
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

#condisions
temperature = 55
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's  cold")    
print("Done")    


age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)


high_income = True
good_credit = True
student = True

if not student:
    print("Eligible ")
else:
    print("Not eligible ")   

if high_income or good_credit or not student:  
      print("Eligible ")
else:
    print("Not eligible ")  
    
    
age = 22   
if age >= 18 and age < 65:
# if 18 <= age < 65:    
    print("Eligible")
    
    
#for loops
for number in range(3):
    print("Attempy", number + 1, (number + 1)* ".")
    
successful = False 
for number in range (3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else: 
    print("Attempted 3 times and failed")    
    
    
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")