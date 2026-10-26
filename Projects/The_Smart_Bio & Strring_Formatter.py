# The Intro of Program 

print("=" * 100)
print("\t\t\t\tThe_Smart_Bio & String_Formatter") 
print("=" * 100)

# User Input first_name , Last_name , Age 

first_name  = input("\nEnter your First name : ")
last_name   = input("\nEnter your Last name : ")
age = int(input("\nEnter your Age : "))

# User ka full name or first alphabet Capitale ho ga 
print("=" * 100)
print("=" * 100)
capitale_First_name = first_name.capitalize()
capitale_Last_name  = last_name.capitalize()
print(f"\nYour Full name is : {capitale_First_name} {capitale_Last_name}")

# User Age 

birth_year = 2026 - age
print(f"\nYour Birth Year is : {birth_year} ")

# Program End
print("=" * 100)
print("\nThanks for Using :)")
print("=" * 100)