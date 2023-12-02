import tkinter as tk
from gtts import gTTS
import os

def read_aloud():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        # Language: German
        tts = gTTS(text=text, lang='de')
        tts.save("output.mp3")
        os.system("output.mp3")

# Create the main window
root = tk.Tk()
root.title("Text to Speech")

# Create GUI elements
text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(padx=10, pady=10)

read_button = tk.Button(root, text="Read Aloud", command=read_aloud)
read_button.pack(padx=10, pady=5)

root.mainloop()
