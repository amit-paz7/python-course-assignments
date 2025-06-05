import sys
from collections import Counter 

if len(sys.argv) < 2:
    print("---------------------------------------------------------")
    print("Oops! You need to tell me which file to read.")
    print("For example: python count_words_from_a_file.py words.txt")
    print("---------------------------------------------------------")
    sys.exit() # Stop the script if no filename is given

file_path_from_user = sys.argv[1]

all_words_in_file = []
word_counts = {}

try:
    print(f"Alright, I'm opening the file: {file_path_from_user}")
    with open(file_path_from_user, 'r') as file:
        file_content = file.read()
        text_in_lowercase = file_content.lower()
        words_from_splitting = text_in_lowercase.split()
        
        for single_word in words_from_splitting:
            if single_word: # Make sure it's not an empty string
                all_words_in_file.append(single_word)

    if not all_words_in_file:
        print(f"Hmm, the file '{file_path_from_user}' seems to be empty or only contains spaces.")
    else:
        word_counts = Counter(all_words_in_file)
        max_word_length = 0
        if word_counts: # Only if there are words to count
            for word in word_counts.keys():
                if len(word) > max_word_length:
                    max_word_length = len(word)
        
        print("\nHere are the word counts, sorted nicely:")
        for word, count in sorted(word_counts.items()):
            print(f"{word:<{max_word_length}}  {count}")

except FileNotFoundError:
    print(f"Oh no! I couldn't find the file: {file_path_from_user}")
    print("Please check if the name and path are correct.")
except Exception as e:
    print(f"Something unexpected happened: {e}")
