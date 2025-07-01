def apply_rot13(text):
    result = []
    for char in text:
        char_code = ord(char)

        if 65 <= char_code <= 90:
            char_code = (char_code - 65 + 13) % 26 + 65
        elif 97 <= char_code <= 122:
            char_code = (char_code - 97 + 13) % 26 + 97
        
        result.append(chr(char_code))
    return "".join(result)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    print("Doctests completed.")
