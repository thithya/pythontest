

#swapping variable
x = input(" enter the value of x:")
y = input("Enter the valuee of y:")

x , y = y , x
print ("x=", x)
print ("y=", y)

# if statement that compares two variables and prints the larger

x = float(input(" enter the value of x:"))
y = float(input("Enter the valuee of y:"))

if ( x > y):
    print("the largest value is", x)
else:
    print("the largest value is", y)

#larger string
string1 = input("enter the first string:")
string2 = input("enter the second string:")

length1 = 0
length2 = 0

for i in string1:
    length1 = length1 + 1

for i in string2:
    length2 = length2 + 1

if length1 > length2 :
    print("string1 is larger than string2")
else:
    print("string2 is larger than string1")

# The above works nicely
# You can also use the builtin len() function 

if len(string1) > len(string2):
    print(string1)
else:
    print(string2)
    
    
#for loop to print even numbers between 1 to 100

for i in range( 0, 101, 2):
    print(i)

# The above works nicely
# How would you rewrite this using the % operator?
    
    
# while loop to print even numbers

i = 0
while ( i <= 100):
    i += 2
    print(i)

# Nice, same thing, how to rewrite this using the modulus operator     
    
    
#nested loop to print astrick

rows = 3
col = 2
for i in range(rows):
    print('*', end='')
    for j in range(col):
        print('*', end= '')
    print('')
