    # მომხმარებელს შემოაყვანინეთ დადებითი მთელი რიცხვი.
    # while ციკლის გამოყენებით მიიღეთ ამ ორი რიცხვის შებრუნებული ვერსია მაგალითად: 1234 - 4321

num = int(input("enter a whole positive nunber: "))

number_but_reversed = 0

while num > 0:
    digit = num % 10
    number_but_reversed = number_but_reversed * 10 + digit
    num = num // 10
print(number_but_reversed)












