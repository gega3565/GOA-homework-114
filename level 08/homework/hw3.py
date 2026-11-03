# 4) შექმენით ცვლადი correct_password და შეინახეთ მასში პაროლი "python123".
# მომხმარებელს შეაყვანინეთ პაროლი და while ციკლის გამოყენებით 
# ხელახლა მოსთხოვეთ შეყვანა, სანამ სწორ პაროლს არ შეიყვანს.
# გამოიყენეთ if და else:
# თუ პაროლი სწორია, გამოიტანეთ "Access Granted!".
# სხვა შემთხვევაში გამოიტანეთ "Wrong password!".


original_password = "python123"

password = input("enter your password: ")

while password != original_password:
    print("the passwords wrong, try again dawg")
    retry_password = input("try entering your password againm: ")
print("access granted")






