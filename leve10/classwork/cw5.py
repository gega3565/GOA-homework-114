# მომხმარებელს შემოაყვანინეთ დადებითი მთელი რიცხვი.
# while ციკლის გამოყენებით გამოთცავეთ მხოლოდ კენთი ციფრების ჯამი

number = int(input("enter a positive whole number: "))

result = 0

while number > 0:
    digit = number % 10

    if digit % 2 != 0:
        result += digit
    number = number // 10

print(result)






