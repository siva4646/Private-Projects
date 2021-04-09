from pathlib import Path

p = Path()

print('''
Welcome to the index of the Python Projects Folder.
Would you like to view the contents of the folder? (y or n)
''')
choice = input("").lower()
if choice == 'y':
    for item in p.glob("*"):
       print(item)
else:
    print(f'{choice} entered... exiting...')


