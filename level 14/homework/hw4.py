# 5) შექმენით ფუნქცია print_numbers(), რომელსაც გადაეცემა ერთი რიცხვი.
#  ფუნქციამ for ციკლის გამოყენებით დაბეჭდოს ყველა რიცხვი 1-იდან გადაცემულ რიცხვამდე.

def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)