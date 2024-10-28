import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Initialize the Google Translator
translator = Translator()

def translate_text():
    """
    Translates text from the input field to the selected language and displays it.
    """
    text = text_input.get("1.0", "end-1c")  # Get text from input area
    target_language = language_choice.get()  # Get selected language code

    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    try:
        translation = translator.translate(text, dest=target_language)
        translated_text.set(translation.text)
    except Exception as e:
        translated_text.set(f"Translation error: {e}")

# Set up main window
root = tk.Tk()
root.title("Text Translator")
root.geometry("500x300")
root.configure(padx=10, pady=10)

# Input Text Area
tk.Label(root, text="Enter Text to Translate:", font=("Arial", 12)).pack(anchor="w")
text_input = tk.Text(root, height=5, wrap="word", font=("Arial", 10))
text_input.pack(fill="x")

# Extended list of languages
language_codes = {
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-cn",
    "Russian": "ru",
    "Portuguese": "pt",
    "Dutch": "nl",
    "Arabic": "ar",
    "Hindi": "hi"
}

# Language Selection
tk.Label(root, text="Select Target Language:", font=("Arial", 12)).pack(anchor="w", pady=(10, 0))
language_choice = ttk.Combobox(root, values=list(language_codes.keys()), font=("Arial", 10))
language_choice.set("fr")  # Default language
language_choice.pack(fill="x")

# Translate Button
translate_button = tk.Button(root, text="Translate", command=translate_text, font=("Arial", 12), bg="#4CAF50", fg="white")
translate_button.pack(pady=10)

# Output Text Area
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(anchor="w")
translated_text = tk.StringVar()
output_label = tk.Label(root, textvariable=translated_text, wraplength=380, justify="left", font=("Arial", 10), fg="#333")
output_label.pack(anchor="w", fill="x")

# Start the main GUI loop
root.mainloop()
