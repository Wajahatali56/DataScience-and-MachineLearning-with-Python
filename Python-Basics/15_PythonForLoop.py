
# Print each items of variable in list
x = ["Banana" , "orange" , "apple" , "cherry"]
for i in x:
    print(i) 

# Looping through string
x = ["Banana" , "orange" , "apple" , "cherry"]
for i in "apple":
    print(i)

# Break statement
fruits = ["Banana" , "orange" , "apple" , "cherry"]
for i in fruits:
    print(i)
    if i == "orange": # They will not print after "orange"
        break

# exit the loop , when i is "banana"  but this time the break comes before print

fruits = [ "orange" , "kiwi" , "Banana" , "cherry"]
for i in fruits:
    if i == "Banana": # They will not print after "Banana" also
        break
    print(i) 

print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# The continue statement
fruits = [ "orange" , "kiwi" , "Banana" , "cherry"]
for i in fruits:
    if i == "kiwi":
        continue
    print(i)

# The range() function
for i in range(10):
    print(i)

# Example of some deep range 
for i in range(3,10):
    print(i)

# You can specify value of increment by adding the 3rd parameter
for i in range(3 , 30 , 2):
    print(i)

# Else in for loop
for i in range(6):
    print(i)
else:
    print("They finished finally:")

# Now we will break the loop i in 3 and else will be garbage now
for i in range(6):
    if i == 3: break
    print(i)
else:
    print("Finished Finally")

# Nested loops
x = ["red" , "blue" , "green" ]
fruits = [ "orange" , "kiwi" , "Banana"]
for i in x:
    for y in fruits:
        print(i , y )

# The pass statement
for i in [0 ,1 ,2]:
    pass


#__________________BEST OF LUCK ____________________#





