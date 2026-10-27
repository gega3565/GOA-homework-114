# 4) მომხმარებელს შემოაყვანინეთ რიცხვი n და გამოთვალეთ
# 0-იდან n-ის ჩათვლით არსებული ყველა ლუწი რიცხვის ჯამი.
# საბოლოოდ გამოიტანეთ მიღებული ჯამი.
# ეს დავალება შეასრულეთ როგორც for, ასევე while ციკლით.

n = int(input("შეიყვანეთ n: "))


total = 0
for i in range(0, n + 1, 2):
    total = total + i
print("for:", total)

total = 0
i = 0
while i <= n:
    total = total + i
    i = i + 2
print("while:", total)











