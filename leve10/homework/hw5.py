#5) შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს რიცხვები მანამ, 
# სანამ 0-ს არ შეიყვანს. გამოიყენეთ while ციკლი რიცხვების მისაღებად და თითოეული რიცხვისთვის განსაზღვრეთ,
#  დადებითია თუ უარყოფითი და ლუწია თუ კენტი. როდესაც მომხმარებელი 0-ს შეიყვანს, 
# პროგრამამ უნდა შეწყვიტოს რიცხვების მიღება და გამოიტანოს შეყვანილი რიცხვების ჯამი, 
# მათი რაოდენობა და დადებითი რიცხვების რაოდენობა.

total = 0
count = 0
positive = 0

num = int(input("Enter number (0 to stop): "))

while num != 0:
    if num > 0:
        print("positive")
        positive = positive + 1
    else:
        print("negative")

    if num % 2 == 0:
        print("even")
    else:
        print("odd")

    total = total + num
    count = count + 1

    num = int(input("Enter number (0 to stop): "))

print("Sum:", total)
print("Count:", count)
print("Positive count:", positive)