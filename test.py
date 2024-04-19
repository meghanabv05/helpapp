def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")



def reverse_str(str):
    reverse_str = ""
    for char in str:
        reverse_str = char + reverse_str
    return reverse_str

str = "Hello, World!"
reversed_string =  reverse_str(str)
print(reverse_str(str))


def revnum(num):
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10
    return reverse_num

num = 1234
print(revnum(num))

x = "malayalam"

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")

