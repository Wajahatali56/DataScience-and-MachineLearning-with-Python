
# How to change the values of the dict
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x["Year"] = 2020
print(x)

# Update() method
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x.update({"Year":"2020"})
print(x)

# How to add the items in dict

x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x["color"]="skyblue"
print(x)

#  Adding the items with update() method
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x.update({"color":"green"})
print(x)

# Removing the items from dict
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x.pop("Year")
print(x)

# Removing the last inserted items from dict
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x.popitem()
print(x)

# Del keyword remove the items with the specified key name

x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
del x["Year"]
print(x)

# Del is also used to delete the whole dict 

x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
del x

# clear () method is used to empty the dict
x = {
    "brand":"Tesla",
    "Model":"xyz",
    "Year":"2002"
}
x.clear()
print(x)

#__________________BEST OF LUCK ____________________#