# 10) https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string):
    result = ""
    vowels = "aeiou"

    for letter in string:
        if letter not in vowels:
            print(letter)

disemvowel("Hello world!")


