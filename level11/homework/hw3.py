# 4) შექმენით მასივი სახელად mixed_list სადაც შეინახავთ ყველა მონაცემთა ტიპის ელემენტებს (მინიმუმ 10),
#  თქვენი დავალებაა ეს სია შეატრიალოთ (while loop-ი გამოიყენეთ)
#  და ტერმინალში გამოიტანოთ ამ სიის შეტრიალებული ვარიანტი.

mixed_list = [1, "hello", 3.14, True, 42, "Nika", 7.5, False, "Python", 100]

result = []

index = len(mixed_list) - 1

while index >= 0:
    print(mixed_list[index])

    index -= 1
