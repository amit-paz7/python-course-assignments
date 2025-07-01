def apply_rot13(text):
    """
    Applies the ROT13 cipher to a string.

    This function rotates each letter by 13 places in the alphabet
    while leaving non-alphabetic characters unchanged.

    >>> apply_rot13('Hello, World!')
    'Uryyb, Jbeyq!'

    >>> apply_rot13('Python is fun.')
    'Clguba vf sha.'

    >>> apply_rot13('123')
    '123'

    >>> apply_rot13(apply_rot13('Double check'))
    'Double check'
    """
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
