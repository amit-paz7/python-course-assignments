
import sys
from rot13_utils import apply_rot13 

def main():
    if len(sys.argv) != 2:
        print("Oops! Tell me which file to ROT13.")
        print("Usage: python rot13_file.py <your_file.txt>")
        return

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f_in:
            content = f_in.read()

        transformed_content = apply_rot13(content)

        with open(file_path, 'w', encoding='utf-8') as f_out:
            f_out.write(transformed_content)

        print(f"Done! '{file_path}' has been ROT13'd.")

    except FileNotFoundError:
        print(f"Hmm, I couldn't find the file: '{file_path}'")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
