def alphabet_position(letter):
    if not len(letter) == 1:
        return -1
    return ord(letter.lower())-97

def rotate_character(char, rot):
    al = alphabet_position(char)
    newch = (al + rot)%26
    if char.isupper():
        return chr(65+newch)
    return chr(97+newch)