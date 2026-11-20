# მომხმარებელს შემოაყვანინე დადებითი მთელი რიცხვი. 
# while ციკლის გაოყენებით დათვალე:
# რამდენი კენტ ციფირა ამ რიცხვში
# რამდენი ლუწიციფრია რიცხვში
# რამდენია ყველა კენტიციფრის ჯამი
# რამდენია ყველა ლუწი ციფრის ჯამი.

# მაგალითად
# მომხმარებელმა შეიყვანა: 583246
# გამოიტანოს:
# კენტი ციფრების რაიდენობა
# რამდენი ლუწიციფრია რიცხვში
# რამდენია ყველა კენტიციფრის ჯამი
# რამდენია ყველა ლუწი ციფრის ჯამი.

n = int(input("enter a number: "))

odd_count = 0
even_count = 0

odd_sum = 0
even_sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even_count += 1
        even_sum += digit
    else:
        odd_count += 1
        odd_sum += digit

    n = n // 10

print("odd count", odd_count)
print("even count", even_count)
print("odd sum", odd_sum )
print("even sum", even_sum)