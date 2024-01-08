from customtkinter import CTk, set_appearance_mode, set_default_color_theme
from modules.frames import TextToMorse, MorseToText

app = CTk()
app.geometry("900x600")
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.title("Morse code Transcoder")

set_appearance_mode("system")
set_default_color_theme("dark-blue")

text_to_morse = TextToMorse(master_app=app)
text_to_morse.frame()

morse_to_text = MorseToText(master_app=app)
morse_to_text.frame()

app.mainloop()
