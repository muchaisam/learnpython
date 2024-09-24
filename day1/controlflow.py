#if else
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")


#nested if else
x = 10

if x > 5:
    print("x is greater than 5")
    if x > 7:
        print("x is greater than 7")
    else:
        print("x is less than 7")


#for loops
for i in range(5):
    print(i)


#looping through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


#while loops
count = 0
while count < 5:
    print(count)
    count += 1