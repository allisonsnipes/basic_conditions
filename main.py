""" used to get the input from the user and saves it to a name and age variable and \n"
   eventually converts it
"""

name = input("what is your name?\n")
age = input("how old are you?\n")
age = int(age)

# incharge of printing the object inputed from the user
print(f'hello {name}, you are {age} years old.')

# incharge of printing the object but via using an alternative format to do so.
print("hello {}, you are {} years old".format(name, age))

# controls whether or not the user can buy an alcoholic beverage or not
if age < 21:
    print(f' sorry {name}, you are not old enough to buy a beverage here')
    exit()
elif age >= 21:
    print(f' welcome {name}, have a drink')
    exit()
else:
    print(f' {name} are you already drunk? Please enter a valid input')
    exit()