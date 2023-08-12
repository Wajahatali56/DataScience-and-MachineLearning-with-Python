
# loop through lists

list = ['Banana', 'pineapple', 'orange', 'apple', 'mangoes', 'gava']
for i in list:
    print(i)

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Looping through the index number

list = ['Banana', 'pineapple', 'orange', 'apple', 'mangoes', 'gava']
for i in range(len(list)):
    print(list[i])

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Using while loop
list = ['Banana', 'pineapple', 'orange', 'apple', 'mangoes', 'gava']
i = 0
while i < len(list):
    print(list[i])
    i = i+1

print("\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
# Looping using list Comprehension(short - hand method )

list = ['Banana', 'pineapple', 'orange', 'apple', 'mangoes', 'gava']
[print(i) for i in list]

# list Comprehension
fruits = ['Banana', 'pineapple', 'orange', 'apple', 'mangoes', "kulfi"]
newfruits = []
for i in fruits:
    if "i" in i:
        newfruits.append(i)
print(newfruits)        

# list Comprehension in 1 line code 

fruits = ['Banana', 'pineapple', 'orange', 'apple', 'mangoes', "kulfi"]
newfruits = [i for i in fruits if "i" in i]
print(newfruits)


#__________________BEST OF LUCK ____________________#









