# 10) მომხმარებელს შეაყვანინეთ რიცხვი n.
#  while ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-დან n-ის ჩათვლით.
#  თუ რიცხვი იყოფა 2-ზეც და 3-ზეც, გამოიტანეთ "Special Number".
#  თუ მხოლოდ 2-ზე იყოფა — "Even". თუ მხოლოდ 3-ზე იყოფა — "Divisible by 3".
#  სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი.

n = int(input("enter a number: "))

num = 1
while num <= n:
    if num % 2 == 0 and num % 3 == 0:
        print("Special Number")
    elif num % 2 == 0:
        print("Even")
    elif num % 3 == 0:
        print("Divisible by 3")
    else:
        print(num)
    num += 1







