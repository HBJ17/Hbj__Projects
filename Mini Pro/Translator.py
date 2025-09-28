from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES

root = Tk()
root.geometry('1100x320')
root.resizable(16,9)
root['bg']="sky blue"

root.title("Language Translator")
Label(root, text="Language Translator", font="ariel 20 bold").pack()


Label(root,text ='Enter Text', font = 'ariel 13 bold', bg = 'white smoke').place(x=165,y=90)

input_text = Entry(root, width=60)
input_text.place(x=30,y=130)
input_text.get()

Label(root, text='Output', font = 'ariel 13 bold', bg='white smoke').place(x=780,y=90)

output_text = Text(root, font='ariel 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
output_text.place(x=500, y=150)

languages=list(LANGUAGES.values())

dest_lang=ttk.Combobox(root, values=languages, width=223)
dest_lang.place(x=130, у=160)
dest_lang.set( "choose language")

def Translate():
   translator = Translator()
   translated = translator.translate(text=input_text.get(), dest=dest_lang.get())
   output_text.delete(1.0, END)
   output_text.insert(END, translated.text)

translate_button=Button(root, text='Translate', font='ariel 12 bold', pady=5, command=Translate, bg='orange', activebackground='green')
translate_button.place(x=445,y=180)

root.mainloop()

