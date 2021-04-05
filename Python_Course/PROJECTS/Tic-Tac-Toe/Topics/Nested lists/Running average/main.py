digits = [input()]
int_digits = [int(x) for x in digits]
running_average = []
test = str(int_digits).replace('[', '').replace(']', '')
print(test)
print(len(test))
for x in range(len(test) - 1):
    print(x + 1)
    if x + 1 <= len(test) - 1:
        running_average.append((int_digits[x] + int_digits[x + 1]) / 2)
print(running_average)