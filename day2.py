#write  a programe remove the duplicate in a list

numbers = [2, 3, 2, 4]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#tuples#unpack

coordinate = (1, 2, 3)

x, y, z = coordinate

print(y)
#read function
f = open("123.txt", "r")

for x in f:
    print(x)
 #ANOTHER METHOD FOR READ
f = open("123.txt", "r")
print(f.read())

#write method
f = open("123.txt", "w")
f.write('hello bhai kmn aso?')
#input from suer
x = input(" write something: ")
y = open('123.txt', 'w')
y.write(x)

