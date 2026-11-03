# 3) მომხმარებელს შემოაყვანინეთ რიცხვი n.
#  while ციკლის გამოყენებით გამოიტანეთ რიცხვები 0-იდან n-ის ჩათვლით.
# გამოიყენეთ if და else:
# თუ რიცხვი 5-ის ჯერადია, გამოიტანეთ "Divisible by 5".
# სხვა შემთხვევაში გამოიტანეთ თავად რიცხვი.

n = int(input("enter a number: "))

i = 0

while i <= n:
    if i % 5 == 0:
        print(i, "is Divisible by 5")
    else:
        print(i, "is not divisible by 5")
    i += 1





