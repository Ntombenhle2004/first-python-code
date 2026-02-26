# print ("welcome to data structures", end = ', ')
# print ('This is an exam room subject')
# print ('have a great 2026') 


# num_students = int(input("How many students? ")) #you can convert an input to whatever data type you want
# total  = 0.0
# for x in range (num_students): 
#     mark = int(input('Enter mark: '))
#     total = total + mark
# avg = total / num_students
# print ('Average is: ', avg)






num_students = int(input("How many students? ")) #you can convert an input to whatever data type you want
total  = 0.0
mrks = []
for x in range (num_students): 
    mrk = int(input('Enter mark: '))
    mrks.append(mrk)
print(mrks)
# for x in range (num_students): 
#     mrk = int(input('Enter mark: '))
#     mrks.append(mrk)
# print(mrks)
for x in range (len(mrks)):
    total = total + mrks[x]
avg = total / len(mrks)  
print ('total of ' , len(mrks) , ' marks is: ', total)
if avg >= 75:
    print('good results, avarage is: ', avg)
elif avg >= 50:
    print('fair results, avarage is: ', avg)
else:
    print('poor results, avarage is: ', avg)
    print('intervention needed')          