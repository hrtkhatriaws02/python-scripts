import tkinter as tk
import random
import pyttsx3
import threading

# ----------------------------------------
# Detect Hemant voice from available voices
# ----------------------------------------
temp_engine = pyttsx3.init()
voices = temp_engine.getProperty('voices')
hemant_voice_id = None

print("Available voices:")
for i, v in enumerate(voices):
    print(f"{i}: {v.name} - {v.id}")
    if "Hemant" in v.name:
        hemant_voice_id = v.id

if hemant_voice_id:
    print(f"\n✅ 'Hemant' voice found and will be used: {hemant_voice_id}")
else:
    print("\n⚠️ 'Hemant' voice not found. Default voice will be used.")

# ----------------------------------------
# Hindi consonants and vowels (for Barakhadi)
# ----------------------------------------
consonants = [
    'क', 'ख', 'ग', 'घ', 'च', 'छ', 'ज', 'झ', 'ट', 'ठ', 'ड', 'ढ',
    'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य',
    'र', 'ल', 'व', 'श', 'ष', 'स', 'ह'
]

vowels = {
    '': 'अ', 'ा': 'आ', 'ि': 'इ', 'ी': 'ई', 'ु': 'उ', 'ू': 'ऊ',
    'े': 'ए', 'ै': 'ऐ', 'ो': 'ओ', 'ौ': 'औ', 'ं': 'अं', 'ः': 'अः'
}

translit = {
    'क': 'Ka', 'ख': 'Kha', 'ग': 'Ga', 'घ': 'Gha', 'च': 'Cha', 'छ': 'Chha',
    'ज': 'Ja', 'झ': 'Jha', 'ट': 'Ta', 'ठ': 'Tha', 'ड': 'Da', 'ढ': 'Dha',
    'त': 'Ta', 'थ': 'Tha', 'द': 'Da', 'ध': 'Dha', 'न': 'Na', 'प': 'Pa',
    'फ': 'Pha', 'ब': 'Ba', 'भ': 'Bha', 'म': 'Ma', 'य': 'Ya', 'र': 'Ra',
    'ल': 'La', 'व': 'Va', 'श': 'Sha', 'ष': 'Sha', 'स': 'Sa', 'ह': 'Ha',
    'अ': 'A', 'आ': 'Aa', 'इ': 'I', 'ई': 'Ee', 'उ': 'U', 'ऊ': 'Oo',
    'ए': 'E', 'ऐ': 'Ai', 'ओ': 'O', 'औ': 'Au', 'अं': 'An', 'अः': 'Ah'
}

barakhadi = [(c + m, c, v) for c in consonants for m, v in vowels.items()]
colors = ["#ff6666", "#33cc33", "#3399ff", "#ff9933", "#9933ff", "#ff33cc"]

# ----------------------------------------
# Global variable for current character
# ----------------------------------------
current = ('', '', '')

# ----------------------------------------
# Function to speak text using a fresh pyttsx3 engine
# ----------------------------------------
def speak_text(text):
    def run_speech():
        try:
            print(f"[Speech Triggered] Speaking: {text}")
            local_engine = pyttsx3.init()
            local_engine.setProperty('rate', 120)
            local_engine.setProperty('volume', 1.0)
            voice_id = hemant_voice_id if hemant_voice_id else voices[0].id
            local_engine.setProperty('voice', voice_id)

            print(f"[Voice Used] Voice ID: {voice_id}")
            print(f"[Engine Properties] Rate: {local_engine.getProperty('rate')}, Volume: {local_engine.getProperty('volume')}")
            print(f"[Engine Queue Before] InLoop: {getattr(local_engine, '_inLoop', 'Unknown')}")

            local_engine.say(text)
            local_engine.runAndWait()

            print(f"[Engine Queue After] InLoop: {getattr(local_engine, '_inLoop', 'Unknown')}")
            print("[Speech Completed]")
            status_label.config(text="✅ उच्चारण पूरा हुआ")
        except Exception as e:
            print("[Speech Error]", e)
            status_label.config(text="⚠️ उच्चारण में त्रुटि")

    threading.Thread(target=run_speech, daemon=True).start()

# ----------------------------------------
# Function to show a random Barakhadi character
# ----------------------------------------
def show_random():
    global current
    current = random.choice(barakhadi)
    char, base, vowel = current
    print(f"[Next Word Clicked] Selected: {char} | Base: {base} | Vowel: {vowel}")
    label.config(text=char, fg=random.choice(colors))
    explain_label.config(text=f"{base} + {vowel} = {char}")
    explain_en_label.config(text=f"{translit.get(base, base)} + {translit.get(vowel, vowel)} = {translit.get(char, char)}")
    speak_barakhadi(char, base, vowel)

# ----------------------------------------
# Function to repeat current Barakhadi character
# ----------------------------------------
def repeat_speech():
    print(f"[Repeat Clicked] Repeating: {current}")
    speak_barakhadi(*current)

# ----------------------------------------
# Function to speak the Barakhadi explanation
# ----------------------------------------
def speak_barakhadi(char, base, vowel):
    phrase = f"{base} अधिक {vowel} बराबर {char}"
    speak_text(phrase)

# ----------------------------------------
# GUI Setup
# ----------------------------------------
root = tk.Tk()
root.title("🎓 हिंदी बाराखड़ी सीखें 🎓")
root.geometry("500x500")
root.config(bg="#e8f0fe")

title = tk.Label(root, text="🎓 हिंदी बाराखड़ी सीखें 🎓", font=("Segoe UI", 24, "bold"), bg="#e8f0fe")
title.pack(pady=20)

label = tk.Label(root, text="", font=("Segoe UI", 100, "bold"), bg="#e8f0fe")
label.pack(pady=10)

explain_label = tk.Label(root, text="", font=("Segoe UI", 20), bg="#e8f0fe")
explain_label.pack(pady=5)

explain_en_label = tk.Label(root, text="", font=("Segoe UI", 16, "italic"), bg="#e8f0fe", fg="#555")
explain_en_label.pack(pady=5)

status_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#e8f0fe", fg="#333")
status_label.pack(pady=5)

btn_next = tk.Button(root, text="➡️ अगला अक्षर", font=("Segoe UI", 18, "bold"),
                     bg="#4CAF50", fg="white", command=show_random)
btn_next.pack(pady=20)

btn_speak = tk.Button(root, text="🔊 फिर से बोलें", font=("Segoe UI", 16, "bold"),
                      bg="#3399ff", fg="white", command=repeat_speech)
btn_speak.pack(pady=5)

btn_exit = tk.Button(root, text="❌ बाहर जाएं", font=("Segoe UI", 14, "bold"),
                     bg="#f44336", fg="white", command=root.quit)
btn_exit.pack(pady=5)

show_random()
root.mainloop()