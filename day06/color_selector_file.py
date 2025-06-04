import sys

def load_colors_from_file(filepath):
    colors_available = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                color = line.strip().lower() # Remove whitespace and convert to lowercase
                if color: # Make sure it's not an empty line
                    colors_available.append(color)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None # Indicate an error
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    return colors_available

def main():
    # Check if the filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Please provide the name of the color file.")
        print("Usage: python color_selector_file.py <colors_file.txt>")
        return

    color_file_path = sys.argv[1]
    available_colors = load_colors_from_file(color_file_path)

    if available_colors is None: # An error occurred loading colors
        return
    
    if not available_colors:
        print(f"No colors found in '{color_file_path}'. The file might be empty.")
        return

    print("Available colors are:")
    for color in available_colors:
        print(f"- {color.capitalize()}") # Print with first letter capitalized for nicer display

    while True:
        chosen_color = input("Please choose a color from the list: ").strip().lower()

        if chosen_color in available_colors:
            print(f"Great! You selected '{chosen_color.capitalize()}'.")
            break  # Exit the loop once a valid color is chosen
        else:
            print(f"Sorry, '{chosen_color}' is not in the list. Please try again.")

if __name__ == "__main__":
    main()
