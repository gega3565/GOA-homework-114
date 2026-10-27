# 4) მომხმარებელს შეაყვანინეთ მისი სახელი და ასაკი.
# შექმენით ცვლადი is_student, რომლის მნიშვნელობაც იქნება True ან False.
# გამოიყენეთ and ოპერატორი და შეამოწმეთ,
# არის თუ არა მომხმარებელი სტუდენტი და ამავე დროს 18 წლის ან უფროსი. შედეგი გამოიტანეთ ტერმინალში.

name = input("enter your name: ")
age = int(input("enter your age: "))
is_student = True

result = is_student and age >= 18

print(result)



