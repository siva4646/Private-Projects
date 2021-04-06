water = int(input("Write how many ml of water the coffee machine has: "))
milk = int(input("Write how many ml of milk the coffee machine has: "))
coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
cups = int(input("Write how many cups of coffee you will need: "))

water_default = 200
milk_default = 50
beans_default = 15

coffee = []
coffee_two = []

if water - water_default >= 0:
    coffee.append(water)
elif milk - milk_default >= 0:
    coffee.append(milk)
elif coffee_beans - beans_default >= 0:
    coffee.append(coffee_beans)
else:
    print('No, I can make only 0 cups of coffee')
    exit()

print(f'''
{water}
{milk}
{coffee_beans}''')

