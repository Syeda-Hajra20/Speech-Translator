from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob
from langdetect import detect
from googletrans import Translator
import speech_recognition as sr
import pyttsx3

# Initialize the Tkinter root window
root = Tk()
root.geometry('500x400')
root.title('Translator')
root.iconbitmap(r'Translator.ico')
root.resizable(False, False)
root.configure(bg='lightcoral')

# Language dictionary
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
            'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
            'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
            'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
            'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
            'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku',
            'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
            'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
            'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no',
            'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa',
            'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st',
            'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so',
            'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta',
            'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
            'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}  # (Use the same dictionary as in your original code)

# Initialize the Translator and Text-to-Speech engine
translator = Translator()
tts_engine = pyttsx3.init()

def translate_text(text, target_language):
    try:
        # Detect the source language
        source_language = detect(text)
        # Translate the text
        translated = translator.translate(text, src=source_language, dest=target_language)
        return translated.text
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")
        return None

def speak_text(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"Text-to-Speech failed: {e}")

def tt():
    input_text = varname1.get()
    target_language = lan_dict[languages.get()]
    translated_text = translate_text(input_text, target_language)
    if translated_text:
        label3.config(text=translated_text)
        speak_text(translated_text)

def main_exit():
    rr = messagebox.askyesnocancel('Notification', 'Are you sure you want to exit?', parent=root)
    if rr == True:
        root.destroy()

def start_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            label3.config(text="Listening...")
            audio = recognizer.listen(source)
            voice_text = recognizer.recognize_google(audio)
            varname1.set(voice_text)
            tt()
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, I did not understand that.")
        except sr.RequestError:
            messagebox.showerror("Error", "Sorry, there was an error with the speech recognition service.")

# Binding Functions
def on_enterentry1(e):
    entry1['bg'] = 'teal'

def on_leaveentry1(e):
    entry1['bg'] = 'white'

def on_enterentry2(e):
    entry2['bg'] = 'teal'

def on_leaveentry2(e):
    entry2['bg'] = 'white'

def on_enterbtn1(e):
    btn1['bg'] = 'teal'

def on_leavebtn1(e):
    btn1['bg'] = 'white'

def on_enterbtn2(e):
    btn2['bg'] = 'teal'

def on_leavebtn2(e):
    btn2['bg'] = 'white'

# Combobox for Languages
languages = StringVar()
font_box = Combobox(root, width=30, textvariable=languages, state='readonly')
font_box['values'] = [e for e in lan_dict.keys()]
font_box.current(37)
font_box.place(x=300, y=0)

# EntryBox for Input
varname1 = StringVar()
entry1 = Entry(root, width=30, textvariable=varname1, font=('times', 15, 'italic bold'))
entry1.place(x=150, y=40)

varname2 = StringVar()
entry2 = Entry(root, width=30, textvariable=varname2, font=('times', 15, 'italic bold'))
entry2.place(x=150, y=100)

# Labels
label1 = Label(root, text='Enter Words: ', font=('times', 15, 'italic bold'), bg='lightcoral')
label1.place(x=5, y=40)

label2 = Label(root, text='Translated: ', font=('times', 15, 'italic bold'), bg='lightcoral')
label2.place(x=5, y=100)

label3 = Label(root, text='', font=('times', 15, 'italic bold'), bg='lightcoral')
label3.place(x=150, y=100)

# Buttons
imgbt1 = PhotoImage(file=r'touch.png')
imgbt2 = PhotoImage(file=r'logot.png')

imgbt1 = imgbt1.subsample(5, 5)
imgbt2 = imgbt2.subsample(7, 7)

btn1 = Button(root, text='Translate', bg='white', activebackground='sky blue', width=100, font=('times', 15, 'italic bold'),
              image=imgbt1, compound=RIGHT, command=tt)
btn1.place(x=70, y=170)

btn2 = Button(root, text='Exit', bg='white', activebackground='sky blue', width=100, font=('times', 15, 'italic bold'),
              image=imgbt2, compound=RIGHT, command=main_exit)
btn2.place(x=280, y=170)

btn_voice = Button(root, text='Voice Input', bg='white', activebackground='sky blue', width=40, font=('times', 15, 'italic bold'),
                   command=start_voice_input)
btn_voice.place(x=20, y=230)

# Binding Events
entry1.bind('<Enter>', on_enterentry1)
entry1.bind('<Leave>', on_leaveentry1)

entry2.bind('<Enter>', on_enterentry2)
entry2.bind('<Leave>', on_leaveentry2)

btn1.bind('<Enter>', on_enterbtn1)
btn1.bind('<Leave>', on_leavebtn1)

btn2.bind('<Enter>', on_enterbtn2)
btn2.bind('<Leave>', on_leavebtn2)

root.mainloop()
