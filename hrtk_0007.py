import tkinter as tk
import random
import threading
from num2words import num2words  # Converts numbers to words (e.g., 12 → "twelve")
import pyttsx3  # Text-to-speech engine

# -------------------------------
# Function: Generate a math problem
# -------------------------------
def generate_problem():
    op = random.choice(['+', '-'])  # Choose operation
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    # Ensure subtraction doesn't result in negative numbers
    if op == '-' and b > a:
        a, b = b, a
    
    problem = f"{a} {op} {b}"
    answer = a + b if op == '+' else a - b
    return problem, answer, op

# Store current problem and answer
current_problem = ("", 0, "")

# Define colors for operations
colors = {"+" : "#33cc33", "-" : "#ff9933"}

# -------------------------------
# Function: Display a new problem
# -------------------------------
def show_problem():
    global current_problem
    current_problem = generate_problem()
    problem_text, _, op = current_problem
    prob_label.config(text=problem_text, fg=colors[op])
    ans_label.config(text="")  # Clear previous answer
    speak_problem(problem_text)

# -------------------------------
# Function: Show the answer
# -------------------------------
def show_answer():
    ans_label.config(text=str(current_problem[1]))

# -------------------------------
# Function: Speak the problem aloud
# -------------------------------
def speak_problem(text):
    def run_speech():
        spoken_text = convert_to_spoken(text)
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(spoken_text)
        engine.runAndWait()
        engine.stop()
    threading.Thread(target=run_speech).start()

# -------------------------------
# Function: Speak the answer aloud
# -------------------------------
def speak_answer():
    def run_speech():
        answer_word = num2words(current_problem[1])
        spoken_text = f"The answer is {answer_word}"
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(spoken_text)
        engine.runAndWait()
        engine.stop()
    threading.Thread(target=run_speech).start()

# -------------------------------
# Function: Convert problem to spoken format
# Example: "10 + 2" → "Ten plus Two"
# -------------------------------
def convert_to_spoken(problem_text):
    parts = problem_text.split()
    if len(parts) == 3:
        a, op, b = parts
        a_word = num2words(int(a))
        b_word = num2words(int(b))
        op_word = "plus" if op == "+" else "minus"
        return f"{a_word} {op_word} {b_word}"
    return problem_text

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Class 1 Math Trainer")
root.geometry("500x500")
root.config(bg="#fdf6e3")

# Title Label
title = tk.Label(root, text="🧮 Math Game (Class 1)", font=("Segoe UI", 24, "bold"), bg="#fdf6e3")
title.pack(pady=20)

# Problem Display Label
prob_label = tk.Label(root, text="", font=("Segoe UI", 100, "bold"), bg="#fdf6e3")
prob_label.pack(pady=20)

# Answer Display Label
ans_label = tk.Label(root, text="", font=("Segoe UI", 24, "bold"), bg="#fdf6e3")
ans_label.pack(pady=10)

# -------------------------------
# Button Frames for Layout
# -------------------------------
btn_frame_top = tk.Frame(root, bg="#fdf6e3")
btn_frame_top.pack(pady=10)

btn_frame_bottom = tk.Frame(root, bg="#fdf6e3")
btn_frame_bottom.pack(pady=10)

# -------------------------------
# Top Row Buttons
# -------------------------------
btn_next = tk.Button(btn_frame_top, text="➡️ Next Problem", font=("Segoe UI", 18, "bold"),
                     bg="#4CAF50", fg="white", command=show_problem)
btn_next.grid(row=0, column=0, padx=10)

btn_answer = tk.Button(btn_frame_top, text="👀 Show Answer", font=("Segoe UI", 18, "bold"),
                       bg="#ff9933", fg="white", command=show_answer)
btn_answer.grid(row=0, column=1, padx=10)

# -------------------------------
# Bottom Row Buttons
# -------------------------------
btn_speak = tk.Button(btn_frame_bottom, text="🔊 Speak Problem", font=("Segoe UI", 16, "bold"),
                      bg="#3399ff", fg="white", command=lambda: speak_problem(current_problem[0]))
btn_speak.grid(row=0, column=0, padx=10)

btn_speak_ans = tk.Button(btn_frame_bottom, text="🗣️ Speak Answer", font=("Segoe UI", 16, "bold"),
                          bg="#795548", fg="white", command=speak_answer)
btn_speak_ans.grid(row=0, column=1, padx=10)

# Exit Button
btn_exit = tk.Button(root, text="❌ Quit", font=("Segoe UI", 14, "bold"),
                     bg="#f44336", fg="white", command=root.quit)
btn_exit.pack(pady=10)

# -------------------------------
# Start with the first problem
# -------------------------------
show_problem()

# Run the GUI loop
root.mainloop()