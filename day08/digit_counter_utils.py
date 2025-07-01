# This file acts as a module containing the core functions for the script
def generate_digit_counts(file_content):
    counts = [0] * 10  # A list to store counts for digits 0 through 9
    for char in file_content:
        if char.isdigit():  # Check if the character is a digit
            digit = int(char)
            counts[digit] += 1
    return counts

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as f_in:
        return f_in.read()

def write_report_file(digit_counts, report_file_path):
    report_lines = []
    for digit_value, count in enumerate(digit_counts):
        report_lines.append(f"{digit_value} {count}")

    with open(report_file_path, 'w', encoding='utf-8') as f_out:
        for line in report_lines:
            f_out.write(line + "\n") # Write each digit and count on a new line
