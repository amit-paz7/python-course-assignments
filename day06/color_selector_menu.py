import sys

def display_menu(colors):
    """Prints the available colors as a numbered menu."""
    print("\nAvailable colors:")
    for index, color_name in enumerate(colors):
        # Menu items are 1-indexed for user-friendliness
        print(f"{index + 1}. {color_name.capitalize()}")
    print("-" * 20)

def get_selection_from_user(colors):
    """Prompts the user to select a color by number and validates input."""
    while True:
        try:
            choice_str = input(f"Please enter the number of your desired color (1-{len(colors)}): ")
            choice_int = int(choice_str) # Try to convert to integer

            # Check if the number is within the valid range (1 to len(colors))
            if 1 <= choice_int <= len(colors):
                # Adjust to 0-based index for the list
                return colors[choice_int - 1]
            else:
                print(f"Oops! That number is out of range. Please pick a number between 1 and {len(colors)}.")
        except ValueError:
            # Handles cases where input is not a whole number (e.g., text, float)
            print("That doesn't look like a valid number. Please try again.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

def process_command_line_arg(arg, colors):
    """
    Tries to process a command-line argument as either a number or a color name.
    Returns the selected color if valid, otherwise None.
    """
    # Try to interpret as a number first
    try:
        choice_int = int(arg)
        if 1 <= choice_int <= len(colors):
            return colors[choice_int - 1] # 0-indexed
    except ValueError:
        # Not a number, so try to interpret as a color name (case-insensitive)
        arg_lower = arg.lower()
        for color_name in colors:
            if color_name.lower() == arg_lower:
                return color_name
    return None # Argument was not a valid number or color name

def main():
    color_options = ["blue", "green", "yellow", "white", "red", "purple", "orange"]
    selected_color = None

    if len(sys.argv) > 1:
        cmd_arg = sys.argv[1]
        selected_color = process_command_line_arg(cmd_arg, color_options)
        if selected_color:
            print(f"Color selected from command line: {selected_color.capitalize()}")
        else:
            print(f"'{cmd_arg}' is not a valid color number or name from the list.")
            # Optionally, you could fall back to prompting here, or just exit.
            # For now, if CLI arg is invalid, we'll still prompt.
            selected_color = None # Reset to ensure prompting

    if not selected_color:
        display_menu(color_options)
        selected_color = get_selection_from_user(color_options)
        print(f"\nYou selected: {selected_color.capitalize()}")

    # You can now do something with the selected_color
    # For example: print(f"Processing the color: {selected_color}")

if __name__ == "__main__":
    main()
