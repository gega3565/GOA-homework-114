# შექმენი ორი სია და და ახალ სიაში შეიტანე მხოლოდ ის რიცხვები რომლებიც 10-ზე მეტია

numbers = [12, 19, 9, 5, 70, 13, 4, 3, 34]

numbers_greater_10 = []

for number in numbers:
    if number > 10:
        numbers_greater_10.append(number)

print(numbers_greater_10)

