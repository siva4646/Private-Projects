cafe = ''
max_cafe = ['', 0]

while True:
    cafe = input()
    cafe = cafe.split()

    if cafe[0] == 'MEOW':
        print(max_cafe[0])
        break

    try:
        cafe[1] = int(cafe[1])
        cats = cafe[1]
        if cafe[1] > max_cafe[1]:
            max_cafe = cafe
    except ValueError:
        print(max_cafe)