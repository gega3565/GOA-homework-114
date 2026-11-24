# 2) შექმენი ფუნქცია სახელად check_password, მისი დავალება იქნება,
#  რომ შეამოწმოს ვალიდურია თუ არა კონკრეტული გადაცემული პაროლი,
#  ფუნქციამ უნდა დააბრუნოს True იმ შემთხვევაში თუ გადაცემული პაროლი შეიცავს მინიმუმ 8 სიმბოლოს და
#  გადაცემულ პაროლში არის მინიმუმ ერთი რიცხვი, ყველა სხვა შემთხვევაში მან უნდა დააბრუნოს False.

def check_passowrd(password):
    minimum_length = len(password) >= 8
    has_digit = False
    for passwrd in password:
        if passwrd.isdigit():
            has_digit = True
    return minimum_length and has_digit

print(check_passowrd("iifhe3433"))




