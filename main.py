def is_valid_hsn(hsn_code):
    """
    Validate an HSN code.

    An HSN code must:
    - Contain only numeric characters.
    - Be 4, 6, or 8 digits long.

    Args:
        hsn_code (str): The HSN code to validate.

    Returns:
        bool: True if the HSN code is valid, otherwise False.
    """
    return hsn_code.isdigit() and len(hsn_code) in (4, 6, 8)


def main():
    """Run the HSN Code Validator."""
    hsn_code = input("Enter an HSN code: ").strip()

    if is_valid_hsn(hsn_code):
        print(f"✅ {hsn_code} is a valid HSN code.")
    else:
        print(f"❌ {hsn_code} is NOT a valid HSN code.")


if __name__ == "__main__":
    main()
