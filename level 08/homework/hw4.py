# 5) მომხმარებელს შემოაყვანინეთ რიცხვი n.
#  for ციკლის გამოყენებით გამოიტანეთ რიცხვები 1-იდან n-ის ჩათვლით.
# გამოიყენეთ if და else:
# თუ რიცხვი 2-ის ჯერადია, გამოიტანეთ "Even number".
# სხვა შემთხვევაში გამოიტანეთ "Odd number".

n = int(input("enter a number: "))

for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "is an even number")
    else:
        print(num, "is an odd number")

















