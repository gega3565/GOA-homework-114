# შექმენი სამი სია ერთში შეიტანე უარყოფითი და დადებითი რიცხვები ხოლო იმ
# დარჩენილი ორი სიიდან ერთში დაამატე მხოლოდ დადებითები და მეორეში უარყოფითები, ნული გამოტოვე

numbers = [4, 6, 7, -6, 129, -30, 80, 99, -7]

negative = []
positive = []

for number in numbers:
    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)


print(positive)
print(negative)


