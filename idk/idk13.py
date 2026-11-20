# შექმენი სია და გამოთვალე სიის ყველა რიცხვის საშუალო არითმეტიკული.

numbers = [4, 2, 19, 49, 5, 105, 200, 1992, 1945]

total = 0

count = 0

for number in numbers:
    total += number
    count += 1

avarage = total / count
print(avarage)
