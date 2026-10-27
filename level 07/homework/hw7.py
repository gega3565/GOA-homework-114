# 8) მომხმარებელს შემოაყვანინეთ რიცხვი n და გამოიტანეთ 0-იდან n-ის ჩათვლით ყველა რიცხვი,
# რომელიც 5-ის ჯერადია. ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.

n = int(input("Please enter your number: "))

for number in range(0, n + 1, 5):
    print(number)




