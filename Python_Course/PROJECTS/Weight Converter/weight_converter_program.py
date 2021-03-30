weight = float(input("Weight: "))
system = str(input("(L)bs or (K)g: "))
system = system.lower()

if system == 'l': 
    print(f'You are {weight * 0.45} kilograms')
elif system == 'k':
    print(f'You are {weight / 0.45} pounds')
