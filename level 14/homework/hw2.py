# 3) შექმენით ფუნქცია calculator(), რომელსაც გადაეცემა ორი რიცხვი და მათემატიკური ოპერატორი (+, -, *, /).
#  ფუნქციამ if-elif-else კონსტრუქციის გამოყენებით უნდა შეასრულოს შესაბამისი მათემატიკური მოქმედება
#  და დაბეჭდოს მიღებული შედეგი.

def calculator(a, b, operator):
    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0:
            print("ნულზე გაყოფა შეუძლებელია")
        else:
            print(a / b)
    else:
        print("უცნობი ოპერატორი")

calculator(10, 5, "+")
calculator(10, 5, "-")
calculator(10, 5, "*")
calculator(10, 5, "/")
