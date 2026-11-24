# 10) https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    result = ""
    for letter in string_:
        if letter not in vowels:
            result = result + letter
    return result


