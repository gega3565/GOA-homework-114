# 6) მომხმარებელს შემოაყვანინეთ რიცხვი n.
#  for ციკლის გამოყენებით გადაუარეთ რიცხვებს 1-იდან n-ის ჩათვლით.
# გამოიყენეთ if და else:
# თუ რიცხვი 3-ის ჯერადია, გამოიტანეთ ეს რიცხვი.
# სხვა შემთხვევაში გამოიტანეთ "Not divisible by 3".


n  = int(input("enter a number: "))

for num in range(1, n + 1):
    if num % 3 == 0:
        print(num)
    else:
        print(num, "is not divisible by 3")

























