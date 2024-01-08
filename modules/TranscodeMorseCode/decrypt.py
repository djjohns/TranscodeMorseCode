from modules.TranscodeMorseCode.morse_code_dict import MORSE_CODE_DICT


def decrypt(message: str) -> str:
    """
    ## Function to decrypt a string from morse code to text.
    Uses the MORSE_CODE_DICT where the key is a alpha-numeric character and the value is that character represented in morse code.

    In morse code 1 space indicates the start of a character and 2 indicates the start of the next word.
    ### Args:
    message (str): The string we want to convert to text.
    ### Returns:
    decipher (str): The message that has been converted to text.
    """

    message += " "

    decipher = ""
    citext = ""

    # Loop over every character in the message.
    for letter in message:
        # If the character is not a space.
        if letter != " ":
            # Counter variable to keep track of space
            i = 0

            # Storing the morse code value of a single character.
            citext += letter

        # If the character is a space.
        else:
            # One space indicates a new character in a word.
            i += 1

            # Two spaces indicates a new word in the message.
            if i == 2:
                # Add a space to separate words in the decipher string.
                decipher += " "
            else:
                # Access the keys using their values (reverse of encryption).
                decipher += list(MORSE_CODE_DICT.keys())[
                    list(MORSE_CODE_DICT.values()).index(citext)
                ]
                citext = ""

    return decipher


if __name__ == "__main__":
    header = "Here is your morse code message converted to text"
    message = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."
    result = decrypt(message.upper())
    print(f"\n")
    print(f"{header:-^80}")
    print(f"Morse Code:{message}")
    print(f"Message:{result}")
    print(f"\n")
