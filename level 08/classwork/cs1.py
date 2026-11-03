#1) while ციკლის გამოყენებით გამოიტანეთ ტერმინალში თქვენი სახელი 20-ჯერ.

counter = 0
name = "gega"

while counter < 20:
    print(name)
    counter += 1

# 2) while ციკლის დახმარებით გამოიტანეთ მხოლოდ ლუწი რიცხვები 0-იდან 100-ის ჩათვლით.

counter = 0

while counter <= 100:
    print(counter)
    counter += 2

# 3) შექმენით ცვლადი სახელად correct_password,
#  შემდგომ შეინახეთ მასში სწორი პაროლი მაგალითად "python123",
#  შემდგომ მომხმარებელს შემოაყვანინეთ პაროლი და მანამ, 
# სანამ მომხმარებელი არ შეიყვანს სწორ პაროლს - ხელახლა მოსთხოვეთ პაროლის შემოყვანა, 
# იმ შემთხვევაში თუ მომხმარებელმა პაროლი შემოიყვანა სწორად ტერმინალში გამოუტანეთ "Access Granted!".

original_password = "python123"

password = input("enter your password: ")

while password != original_password:
    print("the passwords wrong, try again dawg")
    retry_password = input("try entering your password againm: ")
print("access granted")







