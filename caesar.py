from helpers import alphabet_position, rotate_character

def rot13(text):
    output = ""
    for ch in text:
        newch = ch
        if ch.isalpha():
            if ch.lower() > "m":
                newch = chr(ord(ch)-13)
            else:
                newch = chr(ord(ch)+13)
        output += newch
    return output

def encrypt(text, rot):
    output = ""
    for ch in text:
        newch = ch
        if ch.isalpha():
            newch = rotate_character(ch, rot)
        output += newch
    return output

def rotate_string(text, rot):
    return encrypt(text, rot)

def main():
    text = input("Type a message:")
    rot = input("Rotate by:")
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()