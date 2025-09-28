from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(16, 9)
root['bg'] = "sky blue"
root.title("Language Translator")

# Title
Label(root, text="Language Translator", font="ariel 20 bold", bg="sky blue").pack()

# Input label and entry
Label(root, text='Enter Text', font='ariel 13 bold', bg='white smoke').place(x=165, y=90)
input_text = Entry(root, width=60)
input_text.place(x=30, y=130)

# Output label and text box
Label(root, text='Output', font='ariel 13 bold', bg='white smoke').place(x=780, y=90)
output_text = Text(root, font='ariel 10', height=5, wrap="word", padx=5, pady=5, width=50)
output_text.place(x=600, y=150)

# Dropdown for languages
languages = list(LANGUAGES.values())
dest_lang = ttk.Combobox(root, values=languages, width=22)
dest_lang.place(x=130, y=160)
dest_lang.set("choose language")

# Translate function
def Translate():
    selected_lang = dest_lang.get()

    # Check if a valid language is selected
    if selected_lang == "choose language":
        output_text.delete(1.0, END)
        output_text.insert(END, "⚠ Please choose a language!")
        return

    # Find the language code (like 'fr' for French)
    lang_code = None
    for code, lang in LANGUAGES.items():
        if lang == selected_lang:
            lang_code = code
            break

    if lang_code is None:
        output_text.delete(1.0, END)
        output_text.insert(END, "❌ Language not found!")
        return

    # Translate the input text
    translator = Translator()
    translated = translator.translate(text=input_text.get(), dest=lang_code)
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

# Translate button
translate_button = Button(root, text='Translate', font='ariel 12 bold', pady=5,
                          command=Translate, bg='orange', activebackground='green')
translate_button.place(x=445, y=180)

root.mainloop()
