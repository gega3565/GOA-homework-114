# შექმენი ორი სია სადაც შეინახავ თოთოეული მოსწავლის სახელის და მეორე სიაში მათ ქულებს
# შენი დავალებაა:
# 1.გამოიყენო for ციკლი
# 2.გამოიტანო თითოეული მოსწავლის სახელი და ქულა
# 3.თუ ქულა 90 ან მეტია გამოიტანო Excellent
# 4.თუ ქულა 50-ზე ნაკლებია გამოიტანო Failed
# 5.იპოვე ყველაზე მაღალი ქულის მქონე მოსწავლე
# 6.გამოთვალე ყველა მოსწავლის ქულების ჯამი

students = ["gega", "nini", "luka", "gio", "saba", "lasha", "nika", "gabrieli", "vaxtangi"]

points = [99, 100, 67, 55, 14, 59, 98, 88, 76]

best_score = points[0]

best_student = students[0]

for i in range(len(students)):
    print(students[i], points[i])

    if points[i] >= 90:
        print("excellent")
    elif points[i] <= 50:
        print("failed")

    if points[i] > best_score:
        best_score = points[i]
        best_student = students[i]

print("best student", best_student)
print("best score", best_score)
print("total scores", sum(points))

























































