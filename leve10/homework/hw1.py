# 1) შექმენით პროგრამა, რომელიც მომხმარებელს შეაყვანინებს 10 რიცხვს.
#  თითოეული რიცხვის შეყვანის შემდეგ პროგრამამ უნდა შეამოწმოს, არის თუ არა ის დადებითი, 
# უარყოფითი თუ ნული და ასევე დაადგინოს, ლუწია თუ კენტი.
# საბოლოოდ გამოიტანეთ რამდენი დადებითი, უარყოფითი, ლუწი და კენტი რიცხვი შეიყვანა მომხმარებელმა.

positive = 0
negative = 0
even = 0
odd = 0

for i in range(10):
    num = int(input("Enter number: "))

    if num > 0:
        print("positive")
        positive = positive + 1
    elif num < 0:
        print("negative")
        negative = negative + 1
    else:
        print("zero")

    if num % 2 == 0:
        print("even")
        even = even + 1
    else:
        print("odd")
        odd = odd + 1

print("Positive:", positive)
print("Negative:", negative)
print("Even:", even)
print("Odd:", odd)













