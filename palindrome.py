def is_palindrome_string(s):
    s = s.lower()
    return s == s[::-1]


s = 'abba'
print(is_palindrome_string(s))


def is_palindrome_num(num):
    num_str = str(num)
    return num_str == num_str[::-1]

num = 121
print(is_palindrome_num(num))

def is_palindrome_string1(s):
    s = s.lower()
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

s = 'abba'
print(is_palindrome_string1(s))

def is_palindrome_num1(num):
    num_str = str(num)
    n = len(num)
    for i in range(n//2):
        if num_str[i] != num_str[n-i-1]:
            return False
    return True

num = 121
print(is_palindrome_num(num))

