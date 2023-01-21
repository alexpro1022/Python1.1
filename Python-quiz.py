#Question #1 Cube number test.. Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

#heres the infi loop that wrecked my Jupyter Notebook for awhile and completely destroyed the python1.1 document
#number = 0
#while number < 1000:
#   print(number)
#   number+=0**3


#im not sure if i misunderstand the question but i cant seem to figure out how to do it. this is the closest that i can get

number = 1
while number < 1000:
    number+=number**3
    
    print(number)



# Question #2 Get first prime numbers up to 100
for i in range(2,101): 
    for n in range(2,101):
        if i%n == 0:
            break
    if i == n:
        print(i,end=",")






#Question #3 Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age = input('Enter your age')
if int(age) < 18:
    print('kids')
elif int(age) > 18 and int(age) < 66: 
    print('adult')
else: 
    print('senior')
