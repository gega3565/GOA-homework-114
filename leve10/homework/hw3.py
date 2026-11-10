# 3) შექმენით პროგრამა, რომელშიც მომხმარებელმა უნდა გამოიცნოს წინასწარ განსაზღვრული რიცხვი
# (მაგალითად, 42). გამოიყენეთ while ციკლი, რათა მომხმარებელს ჰქონდეს გამოცნობის რამდენიმე მცდელობა.
#  თუ შეყვანილი რიცხვი საიდუმლო რიცხვზე მეტია ან ნაკლებია, გამოიტანეთ შესაბამისი შეტყობინება.
# სწორი პასუხის შემთხვევაში გამოიტანეთ გამარჯვების შეტყობინება და მცდელობების რაოდენობა.

secret = 42
attempts = 0
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

print("You win!")
print("Attempts:", attempts)

