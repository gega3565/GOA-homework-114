# შექმენი სია და იპოვე მასში ყვეკაზე დიდი და პატარა რიცხვები. for ციკლის დახმარებით გამოთვალე მათი სხვაობა

numbers = [64, 19, 20, 92, 29, 100, 129, 930, 488, 282]

biggest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number

difference = biggest - smallest

print(difference)








