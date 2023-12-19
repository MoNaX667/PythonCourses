"""
Write a function that checks whether a string is a palindrome or not. The usage of
any reversing functions is prohibited.
To check your implementation you can use
strings from https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes

"""
import re

def check_str(s: str):
    counter = 0
    s = s.strip().lower()
    s = res = re.sub(r'[^\w\s]', '', s)
    s = s.replace(' ','')
    # print(f"value is \"{s}\" ")
    while counter <= (len(s)/2):
        # print(f"Conditions of {s[counter]} and {s[(len(s) - counter - 1)]}")
        if s[counter] != s[(len(s) - counter - 1)]:
            return False
        counter += 1

    return True



result = check_str("1234")
print(result)

result = check_str("1221")
print(result)

result = check_str("A man, a plan, a canal - Panama")
print(result)

