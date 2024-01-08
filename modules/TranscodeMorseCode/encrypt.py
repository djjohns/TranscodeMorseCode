from modules.TranscodeMorseCode.morse_code_dict import MORSE_CODE_DICT


def encrypt(message: str) -> str:
    """
    ##  Function to encrypt a string to morse code.
    Uses the MORSE_CODE_DICT where the key is a alpha-numeric character and the value is that character represented in morse code.

    In morse code 1 space indicates the start of a character and 2 indicates the start of the next word.

    ### Args:
    message (str): The string we want to convert to morse code.
    ### Returns:
    cipher (str): The message that has been converted to morse code.
    """

    # Start with a blank cipher string.
    cipher = ""

    # Loop over every character in the message.
    for letter in message:
        # If the character is not a space.
        if letter != " ":
            # Converts the character into morse code and adds to cipher string.
            cipher += MORSE_CODE_DICT[letter] + " "

        # If the character is a space.
        else:
            # Add a second space to indicate start of next word in message.
            cipher += " "

    return cipher


if __name__ == "__main__":
    header = "Here is your message converted to morse code"
    message = "Hello World"
    result = encrypt(message.upper())
    print(f"\n")
    print(f"{header:-^80}")
    print(f"Message:{message}")
    print(f"Morse Code:{result}")
    print(f"\n")
