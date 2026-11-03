# 2) მომხმარებელს შეაყვანინეთ ასაკი. თუ ასაკი 0-ზე ნაკლებია, გამოიტანეთ "Invalid age".
#  თუ ასაკი 18 ან მეტია, გამოიტანეთ "Adult", სხვა შემთხვევაში — "Minor".

age = int(input("enter your age: "))

if age < 0:
    print("ivalid age")
elif age >= 18:
    print("adult")
else:
    print("minor")







