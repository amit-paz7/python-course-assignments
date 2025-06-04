import sys

# Predefined list of colors
AVAILABLE_COLORS = ["blue", "green", "yellow", "white", "red", "purple", "orange"]

def display_menu(colors):
    """Prints the available colors as a numbered menu."""
    print("\nAvailable colors:")
    for index, color_name in enumerate(colors):
        # Menu items are 1-indexed for user-friendliness
        print(f"  {index + 1}. {color_name.capitalize()}")
    print("-" * 20)

def get_selection_from_user(colors):
    """Prompts the user to select a color by number and validates input."""
    num_options = len(colors)
    while True:
        user_input = input(f"Please enter the number of your desired color (1-{num_options}): ")
        try:
            # Attempt to convert to float first to handle inputs like "3.0"
            # and also to identify non-integer floats like "3.5"
            num_as_float = float(user_input)
            if num_as_float.is_integer(): # Check if it's a whole number (e.g., 3.0 or 3)
                choice_int = int(num_as_float)
                # Check if the number is within the valid range (1 to len(colors))
                if 1 <= choice_int <= num_options:
                    # Adjust to 0-based index for the list
                    return colors[choice_int - 1]
                else:
                    print(f"Oops! That number is out of range. Please pick a number between 1 and {num_options}.")
            else:
                # Input was a float but not a whole number (e.g., "3.5")
                print("Invalid input. Please enter a whole number (e.g., '3', not '3.5').")
        except ValueError:
            # Handles cases where input is not a number at all (e.g., text)
            print("That doesn't look like a valid number. Please try again.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

def process_command_line_arg(arg, colors):
    """
    Tries to process a command-line argument as either a number (1-based index)
    or a color name (case-insensitive).
    Returns the selected color string or None if not valid.
    """
    # Try to interpret as a number first (1-based index)
    try:
        num_as_float = float(arg) # To handle "3.0" style inputs
        if num_as_float.is_integer():
            choice_idx = int(num_as_float)
            if 1 <= choice_idx <= len(colors):
                return colors[choice_idx - 1] # Convert 1-based to 0-based
    except ValueError:
        pass # Not a number, will try as a name next

    # Try to interpret as a color name (case-insensitive)
    arg_lower = arg.lower()
    for color_name_option in colors:
        if color_name_option.lower() == arg_lower:
            return color_name_option
            
    return None # Argument was not a valid number or name

def main():
    selected_color = None

    # Check for command-line arguments (Extra Credits 2 & 3)
    if len(sys.argv) > 1:
        cmd_arg = sys.argv[1]
        selected_color = process_command_line_arg(cmd_arg, AVAILABLE_COLORS)
        
        if selected_color:
            print(f"Color selected from command line: {selected_color.capitalize()}")
        else:
            print(f"'{cmd_arg}' is not a valid color number or name from the predefined list.")
            # Fall back to prompting if CLI arg is invalid
            selected_color = None 

    # If no valid color was selected from command line (or no arg was given),
    # display menu and prompt user.
    if not selected_color:
        display_menu(AVAILABLE_COLORS)
        selected_color = get_selection_from_user(AVAILABLE_COLORS)
        print(f"\nYou selected: {selected_color.capitalize()}")

    # Example of what you might do with the selected color:
    # print(f"Processing your choice: {selected_color}")

if __name__ == "__main__":
    main()
