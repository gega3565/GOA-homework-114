# 7) მომხმარებელს შემოაყვანინეთ რიცხვი n და გამოთვალეთ, რამდენჯერ უნდა დაემატოს რიცხვი 2-ს,
# რომ მიღებული ჯამი პირველად გახდეს n-ზე მეტი. საბოლოოდ გამოიტანეთ,
# რამდენჯერ შესრულდა მიმატება და რა ჯამი მიიღეთ. ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.

n = int(input("შეიყვანეთ n: "))

count = 0
for i in range(0, n + 1, 2):
    count = count + 1
total = count * 2
print("for - მიმატებების რაოდენობა:", count)
print("for - ჯამი:", total)

count = 0
total = 0
while total <= n:
    total = total + 2
    count = count + 1
print("while - მიმატებების რაოდენობა:", count)
print("while - ჯამი:", total)





