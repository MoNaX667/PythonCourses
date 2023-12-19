"""
Implement a function that receives a string and replaces all " symbols
with ' and vice versa.

"""

def replacer(s: str) -> str:
    result_phrase = ""

    for i in s:
        key = i
        if(i == '\''):
            key = "\""
        elif(i=="\""):
            key = "\'"

        result_phrase+=key

    return result_phrase

print(replacer("Hello \' and \" "))
