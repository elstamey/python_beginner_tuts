__author__ = 'dev'

age = 40
print("my age is " + str(age) + " years")

print("My age is {0} years".format(age))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is approximately %12.50f" %(22/7))

# {x:y} format with the number being x digits and leaving y spaces
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50f}".format(22/7))

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))