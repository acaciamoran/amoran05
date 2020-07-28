def is_lower_101(character):
    if ord("a") <= ord(character) <= ord("z"):
        return True
    else:
        return False

def char_rot_13(character):
    if character.isupper():
        first = ord("A")
    elif character.islower():
        first = ord("a")
    char = ord(character) - first
    new_character = (char + 13) % 26 + first
    return chr(new_character)
