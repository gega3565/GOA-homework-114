# 9) მომხმარებელს შეაყვანინეთ ასაკი და გამოცდის ქულა.
#  თუ ასაკი 18 ან მეტია და ქულა 70 ან მეტია, გამოიტანეთ "You passed!".
#  თუ ასაკი 18-ზე ნაკლებია და ქულა 70 ან მეტია, გამოიტანეთ "Good result, but you are under 18!".
#  თუ ქულა 70-ზე ნაკლებია, გამოიტანეთ "You failed!".

age = int(input("enter your age: "))
test_score = int(input("enter your test score: "))

if test_score >= 70 and age >= 18:
    print("you passed")
elif test_score >= 70 and age < 18:
    print("good result but your under 18")
else:
    print("you failed")






