# შექმენი რიცხვების სია და დაიტვალე რამდენი კენტი რიცხვია

numbers = [4, 2, 19, 49, 5, 105]

count = 0

for number in numbers:
    if number % 2 != 0:
        count += 1

print(count)

