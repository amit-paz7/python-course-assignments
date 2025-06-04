import sys

def generate_digit_counts(file_content):
    counts = [0] * 10  # A list to store counts for digits 0 through 9
    for char in file_content:
        if char.isdigit():  # Check if the character is a digit
            digit = int(char)
            counts[digit] += 1
    return counts

def main():
    # Check if an input file path was given
    if len(sys.argv) != 2:
        print("Please tell me which file to read.")
        print("Usage: python count_digits_in_file.py <input_file.txt>")
        return

    input_file_path = sys.argv[1]
    report_file_path = "report.txt"

    try:
        # Try to open and read the input file
        with open(input_file_path, 'r', encoding='utf-8') as f_in:
            content = f_in.read()

        # Get the counts of each digit
        digit_counts = generate_digit_counts(content)

        # Prepare the lines for the report file
        report_lines = []
        for digit_value in range(10): # For digits 0 through 9
            count = digit_counts[digit_value]
            report_lines.append(f"{digit_value} {count}")

        # Write the report to report.txt
        with open(report_file_path, 'w', encoding='utf-8') as f_out:
            for line in report_lines:
                f_out.write(line + "\n") # Write each digit and count on a new line

        print(f"Digit counts saved to '{report_file_path}'")

    except FileNotFoundError:
        print(f"Sorry, I couldn't find the file: '{input_file_path}'")
    except Exception as e:
        print(f"An error happened: {e}")

if __name__ == "__main__":
    main()
