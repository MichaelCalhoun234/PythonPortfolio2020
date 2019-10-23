playScore = 101
age = 19

if (playScore > 100 and (age < 13 or age <= 18)):
    print("Im in")

user_name = input("enter a user name")
password = input ("enter a password")

uname = "Michael"
unames=("Michael")
pword = "password"

if (uname == user_name) and\
   (password == pword) and\
   (password != "password") or\
   (user_name == "admin") and\
   (user_name not in uname) and\
   (user_name in unames):
    print("Welcome user")
#Mathmatical Operators
# / * - + =
#Comparison Operators
# == != < <= !< > >=
#Logical Operators
# and or not in is
