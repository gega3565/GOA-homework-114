# იპოვე სიაში ყველაზე დიდი რიცხვი max() ფუნქციის გამოყენების გარეშე

numbers = [4, 2, 19, 49, 5, 105, 200, 1992, 1945]

biggest_number = numbers[0]

for number in numbers:
    if number > biggest_number:
        biggest_number = number

print(biggest_number)


