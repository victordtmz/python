import re

def is_palindrome(word):
    normal = ''.join(re.findall(r'[a-z]+', word.lower()))
    backwards = normal[::-1]
    print(normal)
    print(backwards)
    return normal == backwards

print(is_palindrome('aaaaaa'))


