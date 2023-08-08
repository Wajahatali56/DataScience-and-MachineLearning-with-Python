
print("Hello this is wajahat coder")

#create and calling a function
def my_fun():
    print("Hello this is wajahat coder")
my_fun()

# Definition of Arguments - arguments are specified after the function name and inside the parenthesis

def my_name(fname):
    print(fname + " Arshad")
my_name("Wajahat")
my_name("Hamid")
my_name("fahad")

# Number of arguments - 2 args
def my_name(fname , lname):
    print(fname + " " + lname)
my_name("Wajahat","Arshad")

# Arbitrary Arguments , *args
def my_youngboy(*kids):
    print("The youngest child is " + kids[2])
my_youngboy("Hamid" , "Fahad" , "Wajahat")

# Keyword Arguments key=value
def my_child(child1, child2, child3):
    print("The youngest child is " + child1)
my_child(child3="Fahad" , child2="Hamid" ,child1="wajahat")    

# Arbitrary keyword arguments **kwargs
def my_info(**kids):
    print("His last name is " + kids["lname"])
my_info(fname = "Wajahat" , lname = "Ali")

# Default parameter value
def my_fun(country = "Pakistan"):
    print("I am from " + country)
my_fun("India")
my_fun()
my_fun("UK")
my_fun("Srilanka")    

# Passing a list as an argument
def my_fun(food):
    for i in food:
        print(i)
fruits = ["apple","banana","cherry"] 
my_fun(fruits)       

# Return values - To let a function return a value then you use return statement
def my_return(x):
    return 5 * x
print(my_return(2))
print(my_return(3))
print(my_return(4))

# The pass statement
def my_function():
    pass

#__________________BEST OF LUCK ____________________#