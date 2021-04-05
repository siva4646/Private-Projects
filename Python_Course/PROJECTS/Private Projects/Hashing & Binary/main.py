import hashlib

def string_to_md5(string):
    string = hashlib.md5(string.encode())
    return string.hexdigest()

print(string_to_md5("Hello"))
