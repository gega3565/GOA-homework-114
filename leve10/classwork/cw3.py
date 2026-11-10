# მომხმარებელს შემოაყვანინეთ ორი დადებითი რიცხვი იპოვეთ მათი უდიდესი საერთო გამყოფი

num1 = int(input("enter your fisrt positive number: "))
num2 = int(input("enter your second positive number: "))

biggest_common_divider = 1

for divider in range (1, num1 + 1):
    if num1 % divider == 0 and num2 % divider == 0:
        biggest_common_divider = divider

print(biggest_common_divider)








