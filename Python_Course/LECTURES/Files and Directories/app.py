from pathlib import Path

p = Path()
for file in p.glob('*.py'):
    print(file)  # Searches for any .py file in the current directory.

path = Path("Emails")
path.mkdir()  # Creates directory named "Emails"
path.rename("Passwords")
path = Path("Passwords")
path.rmdir()  # Removes directory "Passwords"

path = Path()
print(path.glob('*.py'))
