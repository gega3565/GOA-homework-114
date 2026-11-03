# 4) შექმენით ორი ცვლადი: correct_username = "gio" და correct_password = "12345".
#  მომხმარებელს შეაყვანინეთ სახელი და პაროლი. თუ ორივე სწორია,
#  გამოიტანეთ "Login successful!", სხვა შემთხვევაში — "Wrong username or password!". გამოიყენეთ and.

correct_username = "gio"
correct_password = "12345"

username = input("enter your username: ")
password = input("enter your password: ")

if correct_username == username and correct_password == password:
    print("login successful!")
else:
    print("wrong username or password, try again")





