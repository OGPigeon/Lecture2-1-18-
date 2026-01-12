"""
TODO: A very useful temperature-conversion app.
"""
THRESHOLD_TEMP_F: float = 68

def is_cold_f(temp_f: float) -> bool:
    """
    Tells me if its below or upove agreed upon threshold

    Args:
        temp_f (float): temperture

    Returns:
        bool: True means below agreed upon threshold
    """
    return temp_f < THRESHOLD_TEMP_F

def greet_person() -> None:
    """
    Greets the name of a person
    from the keyboard and greets
    them.
    """
    your_name: str = input("Give me your name please: ")
    print(f"How you doing {your_name}?")


def main() -> None:
    """
    Main function
    """
    pass
if __name__ == "__main__":
    main()
