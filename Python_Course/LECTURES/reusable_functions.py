emojis = {
    ":)": "😀",
    ":(": "😣",
    ";)": "😉"
}

def emoji_converter(message):
    words = message.split(' ')

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = emoji_converter(input("> "))
print(message)
