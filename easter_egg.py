# ------------------------------------------------ EASTER EGG ------------------------------------------------
# Congratulations on finding this file! Please use the following methods below to decrypt the given cipher.

def decrypt(cipher, multiple):
    text = ""
    for idx, ch in enumerate(cipher):
        if ch.isalpha():
            shift = multiple * idx % 26

            newChar = ord(ch) + shift 
            if newChar > ord('z'):
                newChar -= 26
        text += chr(newChar)

    return text

def encrypt(text, multiple):
    cipher = ""
    for idx, ch in enumerate(text):
        if ch.isalpha():
            shift = multiple * idx % 26

            newChar = ord(ch) - shift 
            if newChar < ord('a'):
                newChar += 26
        cipher += chr(newChar)

    return cipher