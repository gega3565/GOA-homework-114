# 6) მომხმარებელს შემოაყვანინეთ დადებითი მთელი რიცხვი
#  n და გამოთვალეთ ამ რიცხვის ციფრების ჯამი.
# მაგალითად, თუ მომხმარებელი შეიყვანს 472-ს,
#  პროგრამამ უნდა გამოთვალოს 4 + 7 + 2 და
#  გამოიტანოს შედეგი — 13. ეს დავალება შეასრულეთ 
# როგორც for, ასევე while ციკლით.


n = int(input("შეიყვანეთ დადებითი მთელი რიცხვი: "))


total = 0
for digit in str(n):
    total = total + int(digit)
print("for:", total)

total = 0
number = n
while number > 0:
    total = total + number % 10
    number = number // 10
print("while:", total)








