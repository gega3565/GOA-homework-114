# 4) მომხმარებელს შეაყვანინეთ სახელი, ასაკი და სიმაღლე. სახელი შეინახეთ str() ფუნქციის გამოყენებით,
#  ასაკი გარდაქმენით int() ფუნქციით, ხოლო სიმაღლე - float() ფუნქციით.
#  გამოიყენეთ bool() ფუნქცია სახელის შესამოწმებლად და შედარების ოპერატორებით განსაზღვრეთ,
#  არის თუ არა მომხმარებელი 16 წლის ან მეტი და მისი სიმაღლე 1.70 მეტრზე მეტი. დაბეჭდეთ მიღებული შედეგები.

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

name_check = bool(name)
age_check = age >= 16
height_check = height > 1.70

print("Was a name entered?", name_check)
print("Is the age 16 or above?", age_check)
print("Is the height above 1.70 meters?", height_check)









