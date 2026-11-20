# ამოცანა 2: საბანკო ანგარიშები
# წარმოიდგინე რომ ქმნი პატარა ბანკის სისტემას.
# შექმენი სამი სია:
# names-ანგარიშის მფლობელების სახელები
# ids-ანგარიშის ნომრები
# balances-თანხა თითოეულ ანგარიშზე

# მაგალითად:
# ნიკა-101-500ლარი
# ანა-102-1200ლარი
# გიო-103-80ლარი

# შენი დავალებაა:
# 1. გამოიყენო while ციკლი რომელიც მომხმარებელს მენიუს აჩვენებს.

# 2. მომხმარებელს შეეძლოს ყველა ანგარიშის ნახვა

# 3. მომხმარებელს შეეძლოს თანხის შეტანა ინდექსის მიხედვით

# 4. მომხმარებელს შეეძლოს თანხის ამოღება ინდექსის მიხედვით

# 5. თუ ამოსაღები თანხა ბალანსზე მეტია დაპრინტე Insufficient funds!

# 6. თუ შეყვანილი თანხა ნულია ან უარყოფითი დაპრინტე Invalid amount!


names = ["nika", "ana", "gio"]
ids = [101, 102, 103]
balances = [500, 1200, 80]

while True:
    print("account 1:", names[0])
    print("account 2:", names[1])
    print("account 3:", names[2])
    choice = input("choose an account: ")
    if choice == "1":
        print("account name:", names[0])
        print("id:", ids[0])
        print("balance:", balances[0])
        deposit = input("do you want to deposit: ")
        if deposit == "yes":
              amount = int(input("how much: "))
              balances[0] += amount
              if amount <= 0:
                    print("invalid amount")
                    break
        elif deposit == "no":
              withdraw = input("would you like to withdraw: ")
              if withdraw == "yes":
                    withdraw_amount = int(input("how much: "))
                    balances[0] -= withdraw_amount
        else:
              continue
        
    elif choice == "2":
            print("account name:", names[1])
            print("id:", ids[1])
            print("balance:", balances[1])
            deposit = input("do you want to deposit: ")
            if deposit == "yes":
                  amount = int(input("how much: "))
                  balances[1] += amount
                  if amount <= 0:
                        print("invalid amount")
                        break
            elif deposit == "no":
                      withdraw = input("would you like to withdraw: ")
                      if withdraw == "yes":
                            withdraw_amount = int(input("how much: "))
                            balances[1] -= withdraw_amount
            else:
                  continue
    
    elif choice == "3":
            print("account name:", names[2])
            print("id:", ids[2])
            print("balance:", balances[2])
            deposit = input("do you want to deposit: ")
            if deposit == "yes":
                  amount = int(input("how much: "))
                  balances[2] += amount
                  if amount <= 0:
                        print("invalid amount")
                        break
            elif deposit == "no":
                          withdraw = input("would you like to withdraw: ")
                          if withdraw == "yes":
                                withdraw_amount = int(input("how much: "))
                                balances[0] -= withdraw_amount
    else:
        print("invalid account")
        break
    







