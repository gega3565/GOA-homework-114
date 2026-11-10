# შემოაყვანინეთ ორი დადებითი მთელი რიცხვი. იპოვეთ მათი უმცირესეი ჯერადი

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

num = 1

while True:
    if num % num1 == 0 and num % num2 == 0:
        print(num)
        break
    num += 1










