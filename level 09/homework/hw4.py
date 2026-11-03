# უნდა შექმნა პროგრამა რომელშიც მომხარებლის დავალება იქნება, რომ გამოიცნოს შენს მიერ ჩაფიქრებული რიცხვი
# წინასწარ შექმენი რაიმე ცვლადი სადაც გექნება შენახული რაიმე რიცხვი, 
# შემდგომ მომხმარებელს მოსთხოვე ამ რიცხვის გამოცნობა იქამდე,
# სანამ არ გამოიცნობს ამ რიცხვს, ასევე მიეცი მინიშნებებიც,
# თუ მომხმარებლის ვარაუდი მეტია შენს რიცხვზე - "თქვენი რიცხვი მეტია ჩაფიქრებულზე"
# თუ რიცხვი ნაკლებია შენს რიცხვზე - "თქვენი რიცხვი ნაკლებია ჩაფიქრებულ რიცხვზე" და
# თუ მომხმარებელი გამოიცნობს ჩაფიქრებულ რიცხვს
# რომ უთხარი "თქვენ წარმატებით გამოიცანით რიცხვი!".

secret_numbr = 67

while True:
    user_guess = int(input("guess the number: "))


    if user_guess > secret_numbr:
        print("the number is higher than the secret number, try agaib")
    elif user_guess < secret_numbr:
        print("the number is lower than the secret number, try again")
    else:
        print("you have guessed the secret number correctly")
        break


