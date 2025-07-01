# This is the main script that will run
import sys
import digit_counter_utils as utils

def main():
    
    if len(sys.argv) != 2:
        print("Please tell me which file to read.")
        print("Usage: python count_digits_in_file.py <input_file.txt>")
        return

    input_file_path = sys.argv[1]
    report_file_path = "report.txt"

    try:
        content = utils.read_file_content(input_file_path)
        digit_counts = utils.generate_digit_counts(content)
        utils.write_report_file(digit_counts, report_file_path)

        print(f"Digit counts saved to '{report_file_path}'")

    except FileNotFoundError:
        print(f"Sorry, I couldn't find the file: '{input_file_path}'")
    except Exception as e:
        print(f"An error happened: {e}")

if __name__ == "__main__":
    main()
