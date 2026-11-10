# მომხმარებელს შემოაყვანინე ორი დადებითი მთელი რიცხვი.
# for ციკლის გამოყენებით დაითვალე რამდენი საერთო გამყოფი აქვთ ამ რიცხვებს.

num1 = int(input("enter a whole number: "))
num2 = int(input("enter a second whole number: "))

count = 0

for divider in range(1, num1 + 1):
    if num1 % divider == 0 and num2 % divider == 0:
        count += 1
print(count)






