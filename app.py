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
