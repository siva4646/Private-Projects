minimum = float(0)
count = 0
while True:

    try:

        x = input()
        x = float(x)

        if count == 0:

            minimum = x
        else:
            if x < minimum:
                minimum = x
        count += 1
    except ValueError:
        if x == '.':
            print(minimum)
            break
