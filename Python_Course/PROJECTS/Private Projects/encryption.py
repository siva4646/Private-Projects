import hashlib

def element_to_sha512(string):
    string = hashlib.sha512(string.encode())
    return string.hexdigest()
print(element_to_sha512('Hello'))

def element_to_sha256(string):
    string = hashlib.sha256(string.encode())
    return string.hexdigest()

print('''


''')

print(element_to_sha256('Hello'))
