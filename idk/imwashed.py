# წარმოიდგინე რომ ქმნი პატარა ონლაინ მაღაზიას.
# შექმენი სამი სია:
# products-პროდუქტების სახელები
# prices-პროდუქტების ფასები
# quantites-პროდუქტების რაოდენობა საწყობში

# მაგალითად:
# ტელეფონი-1500ლარი-5ცალი
# კომპიუტერი-3000ლარი-3ცალი
# მაუსი-50ლარი-20ცალი

# შენი დავალებაა:
# 1. გამოიყენო while ციკლი რომელიც მომხმარებელს მენიუს აჩვენებს.

# 2. მომხმარებელს შეეძლოს ყველა პროდუქტის ნახვა

# 3. მომხმარებელს შეეძლოს პროდუქტის შეძეენა ინდექსის მიხედვით

# 4. თუ პროფუქტი აღარ არის მარაგში დაპრინეტე Out of stock!

# 5. თუ შეძენის რაოდენობა მარაგზე მეტია დაპრინტე Not enough products!

# 6. წარმატებული შეძენის შემთხვევაში შეამცირე მარაგი

# 7. მომხმარებელს შეეძლოს მაღაზიიდან გასვლა

products = ["apple", "logitech", "nothing"]

prices = [1500, 300, 800]

quantities = [5, 20, 3]

while True:
    print("1 - apple")
    print("2 - logitech")
    print("3 - nothing")
    print("4 - exit")
    customer_choice = input("choose: ")

    if customer_choice == "1":
        print("quantity: ", quantities[0])
        amount1 = int(input("choose an amount: "))
        if quantities[0] == 0:
            print("out of stock")
        elif amount1 > quantities[0]:
            print("not enough products")
        else:
            quantities[0] = quantities[0] - amount1
            print("transaction successful")

    elif customer_choice == "2":
        print("quantity:", quantities[1])
        amount2 = int(input("choose an amount: "))
        if quantities[1] == 0:
            print("out of stock")
        elif amount2 > quantities[1]:
            print("not enough products")
        else:
            quantities[1] = quantities [1] - amount2
            print("transaction successful")

    elif customer_choice == "3":
            print("quantity:", quantities[2])
            amount3 = int(input("choose an amount: "))
            if quantities[2] == 0:
                print("out of stock")
            elif amount3 > quantities[12]:
                print("not enough products")
            else:
                quantities[2] = quantities [2] - amount3
                print("transaction successful")

    elif customer_choice == "4":
        
        print("goodbye")

    else:
        print("this product doesnt exist")