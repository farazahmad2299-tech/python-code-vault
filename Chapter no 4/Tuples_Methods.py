tech_items = ("python", "java", "vscode", "python", "git", "python", "linux")

# len() used to find length 
print("The Length of tuple is : ",len(tech_items))

# .count() used to cound a number or a string 
print("To count Python : ",tech_items.count("python"))

# .index() used to find index of string or number 
print("The index of git is : ", tech_items.index("git"))

# max() used to find max value of touple
print("The max near alphabet to z is :  ",max(tech_items))
print("The max near alphabet to a is : ",min(tech_items))

# sorted() create a new touple and sort works on numbers so it cannot give output

new_tuple= sorted(tech_items)