
name = input('what is your name? ')
print(' hi  ' +name)
colo r= input('what is your favourute color:')
print('i  loves   ' +color)
print(name +'likes ' + color)
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print("i am only ", age, " years old")
#in and replace
course = 'python for me'
print(course.replace('p' , 'p'))
print('python' in course)

#arithmetic operation
x = 10
x += 3
print(x)
#operator
x = (10+3)*2**2
print(x)
#parenthesisi > exponential > multi or divi > add or sub
#math function
x = 2.9
print (round(x))
print (abs(-2.9))
import math
print(math.floor(2.9))
#if statement
is_hot = False
is_cold = False

if is_hot:
    print("its a hot day")
    print("drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("wear warm cloth")
else:

    print(" its a lovely day")
print("enjoy your day")



#logic opertor

has_high_income =False
has_good_credit= True
if has_high_income or has_good_credit:
    print(" eligable for loan")

    has_good_credit = True
    has_criminal_recor = False

    if has_good_credit and not has_criminal_recor:
        print(" eligable for loan")

        #comparision

        temp = 35
        if temp >= 30:
            print("its a hot day")
        else:
            print("its not a hot day")
            proble:
name =input("enter you name?")
print( len(name))
if len(name) < 4:
    print("name mustbe atleast 4 chrcter")

elif len(name) >15:
    print("mximum size of character is 15")

else:
    print("its alright")
#while loop

i = 1
while i <=100:
    print(i)
    i+=1
print("done")

##triangle shape
i = 1
while i <=100:
    print('*' * i)
    i+=1
 #guessing game
secret_num = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess =  int (input("guess:"))
    guess_count += 1
    if guess == secret_num:
        print('you won the guess')
        break

else:
    print('sorry ! you are failed')



    #car Game
command = ""

while command.upper() != "quit":
    command = input(">")
    if command.lower() == "start":
        print("car started...")
    elif command.lower() == "stop":
        print("car stopped ...")
    elif command.lower() == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit


        """
              )
    elif command.lower == "quit":
        print("thank you")
        break

        #for loop
for item in ['noman','dbn','bhai']:
    print(item)
    #for1
    for item in range(5, 10, 2):
        print(item)
        #for2

prices = [10,20,30]
total = 0
for price in prices:
    total += price

print(f"Total:{total}")

#nested_loop
for x in range(5):
    for y in range(4):
        print(f'({x}{y})')
    #01
num = [5, 2, 5, 2, 2]
for x_count in num:
    print('x' * x_count)


#list
name = ['noman', 'moon', 'bhai', 'dbn', 'najmul']
name[0] = 'nasir'
print(name[2:])
print(name)
#finding the largest num in the list

numbers = [3, 6, 7, 8, 1, 2]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number

print(max)


