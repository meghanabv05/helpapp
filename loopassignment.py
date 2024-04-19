my_list = ["monday","tuesday","wednesday",'thursday']


x = 0

while x < 3:

    x += 1

    for i in my_list:

        if i == "monday":
            continue
        print(i)