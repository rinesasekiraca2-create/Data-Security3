def caesar_encrypt(text, key):
    result = ""
    key = int(key)

     for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char

    return result

