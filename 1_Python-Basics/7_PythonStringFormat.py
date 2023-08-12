'''
# Wrong method 
x = 10
y = "wajahat"

txt = x + y
print(txt) '''

# Use format method for concatination
age = 50
txt = "My age is {}"
print(txt.format(age))

# Format Unlimited arg*

Qty = 5
itemno = 569
price = 450.66
myorder = "I wants {} pieces of items numbers {} for price {} Rupees."
print(myorder.format(Qty , itemno , price))


# Format Unlimited arg* with indexing

Qty = 5
itemno = 569
price = 450.66
myorder = "I wants pay {2} rupees for {0} pieces of item numbers {1}."
print(myorder.format(Qty , itemno , price))

#__________________BEST OF LUCK ____________________#