
def get_formatted_name(first, last , middle=''):

    """Generate a neatly formatted full name."""

    if middle:  # Check if a middle name is provided
        full_name = f"{first} {middle} {last}"

    else:  # If no middle name is provided, just use first and last names
        full_name = f"{first} {last}"
    return full_name.title()