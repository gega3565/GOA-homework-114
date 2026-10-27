# 5) მომხმარებელს შემოაყვანინეთ რიცხვი n და გამოიტანეთ
#  ყველა კენტი რიცხვი 1-იდან n-ის ჩათვლით.
#  ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.


n = int(input("Please enter your number: "))

for number in range(1, n + 1, 2):
    print(number)



