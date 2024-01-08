from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkInputDialog
from dataclasses import dataclass
from modules.TranscodeMorseCode import encrypt
import datetime


def get_timestamp():
    """
    ### Gets current string formatted timestamp in YYYY-MM-DD_HH-MM-SS format.
    """
    # Get the current timestamp as a datetime object
    current_timestamp = datetime.datetime.now()
    # Format the timestamp as a string with a specific format
    TS = current_timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    return TS


def write_txt_file(filename, file_content):
    text_file = open(filename, "w")
    text_file.write(file_content)
    text_file.close()


def text_to_morse():
    TS = get_timestamp()
    filename = f"Outgoing_CW_{TS}.txt"
    default_file_loc = f"D:/dev/ham_radio_apps/TranscodeMorseCode/data/tx/"

    # Ask user to enter file type.
    enter_file_type = CTkInputDialog(
        text="Enter the message to convert to Morse Code:",
        title="Enter Message",
    )
    # Retrieve the user's input.
    message = enter_file_type.get_input()

    # If we get the user's input.
    if message:
        # Transcode the string into Morse Code.
        result = encrypt(message.upper())
        # Write the transcoded results to a txt file.
        write_txt_file(f"{default_file_loc}{filename}", result)
        # TODO: Setup logging and pass this to log.
        print(f"\n")
        print(f"{filename:-^80}")
        print(f"Message:{message}")
        print(f"Morse Code:{result}")
        print(f"\n")


@dataclass
class TextToMorse:
    """
    Example Widget.
    """

    master_app: CTk

    def frame(self):
        """
        Sets UI details for the Widget frame.
        """
        frame = CTkFrame(master=self.master_app, fg_color="#4EAC7D")
        frame.grid(row=2, column=1, rowspan=2, padx=50, pady=50)

        CTkLabel(
            master=frame,
            text=f"Text to Morse Code",
            font=("Arial Bold", 20),
            justify="center",
        ).pack(expand=True, pady=(30, 15))

        CTkButton(master=frame, text=f"Click Me", command=text_to_morse).pack(
            expand=True, fill="both", pady=(30, 15), padx=30
        )
