# ამოცანა 1: ბიბლიოთეკა
# წარმოიდგინე რომ ქმნი პატარა ბიბლიოთეკის სისტემას.
# შექმენი სამი სია:
# books-წიგნების სახელები
# authors-ავტორების სახელები
# copies-წიგნის ეგზემპლარების რაოდენობა

# მაგალითად:
# ჰარი პოტერი-რაულინგი-4ცალი
# მეფე ლირი-შექსპირი-2ცალი
# ვეფხისტყაოსანი-რუსთაველი-6ცალი

# შენი დავალებაა:
# 1. გამოიყენო while ციკლი რომელიც მომხმარებელს მენიუს აჩვენებს.

# 2. მომხმარებელს შეეძლოს ყველა წიგნის ნახვა

# 3. მომხმარებელს შეეძლოს წიგნის გამოტანა ინდექსის მიხედვით

# 4. თუ წიგნი აღარ არის ხელმისაწვდომი დაპრინტე No copies available!

# 5. თუ ინდექსი არ არსებობს დაპრინტე Invalid index!

# 6. წარმატებული გამოტანის შემთხვევაში შეამცირე ეგზემპლარების რაოდენობა

books = ["ჰარი პოტერი", "მეფე ლირი", "ვეფხისტყაოსანი"]
authors = ["რაულინგი", "შეკსფირი", "რუსთაველი"]
quantities = [4, 2, 6]

while True:
    print("1 - წიგნების ნახვა")
    print("2 - ყიდვა")
    print("3 - exit")
    choice = input("choose: ")

    if choice == "1":
        print("1 -", books[0], quantities[0])
        print("2 -", books[1], quantities[1])
        print("3 -", books[2], quantities[2])
        print("4 - back")
        while True:
            back = input("back: ")
            if back == "4":
                break
            else:
                print("enter 4 to go back")
             
#user buy option
    elif choice == "2":
        while True:
            print("1 -", books[0], quantities[0])
            print("2 -", books[1], quantities[1])
            print("3 -", books[2], quantities[2])
            print("4 - back")
            book_choice = input("choose an index: ")
#choice harry potter
            if book_choice == "1":
                if quantities[0] == 0:
                    print("out of stock")
                else:
                    while True:
                         print("chosen:", books[0], quantities[0])
                         amount = int(input("enter an amount: "))
                         if amount > quantities[0]:
                             print("not enough product")
                         else:
                             quantities[0] -= amount
                             print("success!")
                             break
#choice მეფე ლირი 
            elif book_choice == "2":

                if quantities[1] == 0:
                    print("out of stock")
                else:
                    while True:
                        print("chosen:", books[1], quantities[1])
                        amount = int(input("enter an amount: "))
                        if amount > quantities[1]:
                            print("not enough product")
                        else:
                            quantities[1] -= amount
                            print("Success!")
                            break
#choice ვეფხისტყაოსანი
            elif book_choice == "3":
                if quantities[2] == 0:
                    print("out of stock")
                else:
                    while True:
                        print("chosen:", books[2], quantities[2])
                        amount = int(input("enter an amount: "))
                        if amount > quantities[2]:
                             print("not enough product")
                        else:
                            quantities[2] -= amount
                            print("Success!")
                            break
            #user exit after buy
            elif choice == "4":
                break
            else:
                print("enter 4 to go back")
#choice exit
    elif choice == "3":
         break







