# 6) მომხმარებელს შეაყვანინეთ რიცხვი n. for ციკლის გამოყენებით გამოიტანეთ ყველა რიცხვი 1-დან n-ის ჩათვლით.
#  თუ რიცხვი ლუწია, გამოიტანეთ "Even", სხვა შემთხვევაში — "Odd".

n = int(input("enter a number: "))

for num in range(1, n + 1):
    if num % 2 == 0:
        print(num, "Even")
    else:
        print(num, "Odd")








































