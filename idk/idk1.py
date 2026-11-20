# შექმენი სია რომელშიც შეინახავ მინიმუმ 12 სიტვას.
# შენი დავალებაა:
# 1. თითოეული სიტყვის პირველი ასო გადაოყვანო დიდ ასოდ 
# 2. თუ სიტყვის სიგრძე 5-ზე მეტი გამოიტანე Long word
# 3. სხვა შეთხვევაში გამოიტანე Short word
# 4. დაითვალე გრძელი სიტყვების რაოდენობა.
# 5. იპოვე ყველაზე გრძელი სიტყის სიგრძე

names = ["monitor", "desk", "window", "frame", "desk", "curtain", "book", "keyboard", "mouse", "bike", "lamp", "poster"]

long_count = 0

for names in names:
    capitalize_word = names.capitalize

    if len(names) > 5:
        print(capitalize_word, "long word")
    else:
        print(capitalize_word, "short word")

print("long words: ", long_count)

longest_word = ""

for names in names:
    if len(names) > len(longest_word):
        longest_word = names
print("longest word", longest_word)

print("lenth", len(longest_word))
