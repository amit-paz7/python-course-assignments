import sys
from collections import Counter

def count_words_in_file(filepath):
    print(f"Opening the file: {filepath}")
    with open(filepath, 'r') as file:
        file_content = file.read()
        words_in_lowercase = file_content.lower().split()
        word_counts = Counter(words_in_lowercase)
        return word_counts

def print_formatted_counts(word_counts):
    if not word_counts:
        print(f"Hmm, the file seems to be empty or only contains spaces.")
        return

    max_word_length = 0
    for word in word_counts.keys():
        if len(word) > max_word_length:
            max_word_length = len(word)

    print("\nHere are the word counts, sorted nicely:")
    for word, count in sorted(word_counts.items()):
        print(f"{word:<{max_word_length}}  {count}")


# --- Main Script Logic ---
if len(sys.argv) < 2:
    print("---------------------------------------------------------")
    print("Oops! You need to tell me which file to read.")
    print("For example: python count_words_from_a_file.py words.txt")
    print("---------------------------------------------------------")
    sys.exit() 

file_path_from_user = sys.argv[1]
try:
    counts = count_words_in_file(file_path_from_user)
    print_formatted_counts(counts)

except FileNotFoundError:
    print(f"Oh no! I couldn't find the file: {file_path_from_user}")
    print("Please check if the name and path are correct.")
except Exception as e:
    print(f"Something unexpected happened: {e}")
