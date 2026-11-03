# 7) შექმენით ცვლადი correct_password = "python123".
#  while ციკლის გამოყენებით მომხმარებელს პაროლი შეაყვანინეთ მანამ,
#  სანამ სწორ პაროლს არ შეიყვანს. არასწორი პაროლის შემთხვევაში გამოიტანეთ "Wrong password!",
#  სწორი პაროლის შემთხვევაში — "Access Granted!".

correct_password = "python123"

password = input("enter your password: ")

while password != correct_password:
    print("the password wrong try again.")
    password = input("re-enter your password: ")

print("access granted")





















0

























