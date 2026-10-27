text = "  Python Programming Language is Extremely Fun and Powerfull!  "

# To find Length of string len()
print(len(text))

# That converts the whole string to uppercase .upper()
upper = text.upper()
print(upper)

# That coverts the whole string to Lowercase .lower()
lower = text.lower()
print(lower)

# That delete the space from starting and ending of a string .strip()
formatted_string = text.strip()
print(formatted_string)

# This function is used to replace old word to a new one .replace()
replace = text.replace("Extremely","Very")
print(text.replace("Extremely","Very"))
print(replace)

# This function check the index of a word .find() 
find = text.find("Programming")
print(find)

# This function check that how many times a specific character comes .count()
count = text.count("m")
print(count)

# This function is used to check the index of a word index .index()
print(text.index("Fun"))

# This function converts the string into list in terms of spaces .split()
print(text.split())

# This function is used to capitale Every first letter of every word .title()
print("Title function : ",text.title())

# This function is used to identify the starting of any string or character .startswith()
print("Is the String stars with P : ",text.startswith("P"))

# This function is used to identify the ending of a string .endswith()
print("Is the string Ends with ll",text.endswith("ll")) 

# sorted() create a new string  and sort only numbers so it does not give output

new_string= sorted("text")