# მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ არის თუ არა მარტივი რიცხვი.
# მარტივი რიცხვი იყოფა მხოლოდ ერთზე და საკუთარ თავზე

num = int(input("enter a numbre: "))

prime_num = True

if num < 2:
    prime_num = False

for divider in range(2, num):
    if num % divider == 0:
        prime_num = False

if prime_num:
    print("prime")
else:
    print("not priem")



