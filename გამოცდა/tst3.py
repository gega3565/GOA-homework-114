# მომხმარებელს შემოაყვანიე დადებითი მთელი რიცხვი.
# while ციკლის გამოყენებით შეამოწმე, იკითხება თუ არა ეს რიცხვი ორივე მხრიდან ერთნაირად.
# თუ რიცხვი თავდაპირველად და შებრუნებული სახით ერთნაირია გამოიტანე
# Palindorme წინააღმდეგ შემთხვევაში Not Palindorme

n = int(input("enter a number: "))

original = n
reversed = 0

while n > 0:
    digit = n % 10 
    reversed = reversed * 10 + digit
    n = n // 10

if original == reversed:
    print("palindrome")
else:
    print("not palindrome")