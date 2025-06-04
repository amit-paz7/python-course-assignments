import sys

def apply_rot13(text_to_transform):
    result = []
    for char_code in [ord(char) for char in text_to_transform]:
        # Check for uppercase letters
        if 65 <= char_code <= 90:  # ASCII for A-Z
            char_code = (char_code - 65 + 13) % 26 + 65
        # Check for lowercase letters
        elif 97 <= char_code <= 122:  # ASCII for a-z
            char_code = (char_code - 97 + 13) % 26 + 97
        result.append(chr(char_code))
    return "".join(result)

def main():
    if len(sys.argv) != 2:
        print("Oops! Tell me which file to ROT13.")
        print("Usage: python rot13_file.py <your_file.txt>")
        return # Exit if no file is given

    file_path = sys.argv[1]

    try:
        # Read the original file content
        with open(file_path, 'r', encoding='utf-8') as f_in:
            content = f_in.read()

        # Get the ROT13 version
        transformed_content = apply_rot13(content)

        # Write it back to the same file
        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(transformed_content)

        print(f"Done! '{file_path}' has been ROT13'd.")

    except FileNotFoundError:
        print(f"Hmm, I couldn't find the file: '{file_path}'")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
