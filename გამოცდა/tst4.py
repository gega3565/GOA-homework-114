# მომხმარებელს შემოაყვანინე დადებითი მთელი რიცხვი.
# while ციკლის გამოყენებით იპოვე ამ რიცხვის ყველაზე დიდი და ყველაზე პატარა ციფრი

# n = int(input("enter a number: "))

# max_digit = 0
# min_digit = 9

# while X
n = int(input("enter a number: "))

max_digit = 0
min_digit = 9

while n > 0:
    digit = n % 10

    if digit > max_digit:
        max_digit = digit

    if digit < min_digit:
        min_digit = digit

    n = n // 10

print("Maximum", max_digit)
print("Minimum",min_digit)


