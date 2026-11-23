import tkinter as tk
import random
import os

window_width = 538
window_height = 562

colors = [
    "red", "blue", "green", "yellow",
    "orange", "purple", "pink",
    "black", "gray", "brown",
    "cyan", "white"
]

highscore_file = "highscore.txt"
score = 0
highscore = 0
current_color = ""
last_color = ""
font_family = "Rubik Bubbles"
poppins = "Poppins Regular"

def load_highscore():
    if os.path.exists(highscore_file):
        try:
            return int(open(highscore_file).read())
        except:
            return 0
    return 0

def save_highscore(value):
    with open(highscore_file, "w") as f:
        f.write(str(value))

def start_new_round():
    global current_color, last_color
    entry.delete(0, tk.END)
    word = random.choice(colors)

    current_color = random.choice(colors)
    while current_color == last_color:
        current_color = random.choice(colors)
    last_color = current_color

    word_label.config(text=word.upper(), fg=current_color)
    feedback_label.config(text="Type the COLOR of the text", fg="#e0edff")

def check_answer(event=None):
    global score, highscore
    answer = entry.get().strip().lower()
    if not answer:
        return
    if answer == current_color:
        score += 1
        score_label.config(text=f"Score: {score}")
        feedback_label.config(text="Correct!", fg="#00ff5e")
        if score > highscore:
            highscore = score
            highscore_label.config(text=f"High Score: {highscore}")
            save_highscore(highscore)
    else:
        score = 0
        score_label.config(text=f"Score: {score}")
        feedback_label.config(
            text=f"Wrong! It was {current_color.upper()}",
            fg="#fc3a3a"
        )
    window.after(800, start_new_round)

window = tk.Tk()
window.title("GUESS THE COLOR GAME 🤔")
window.geometry(f"{window_width}x{window_height}")
window.configure(bg="#24282f")
highscore = load_highscore()

tk.Label(
    window, text="Guess The Color", fg="#00d9ff", bg="#24282f", font=(font_family, 32)).pack(pady=(18, 6))
stats_frame = tk.Frame(window, bg="#24282f")
stats_frame.pack(pady=6)

score_label = tk.Label(stats_frame, text="Score: 0", fg="#e5e7eb", bg="#24282f", font=("poppins", 12, "bold"))
score_label.pack(side="left", padx=20)

highscore_label = tk.Label(stats_frame, text=f"High Score: {highscore}", fg="#e5e7eb", bg="#24282f", font=("poppins", 12, "bold"))
highscore_label.pack(side="left", padx=20)

word_label = tk.Label(window, text="", bg="#323131", fg="white", width=9, height=2, font=(font_family, 50), bd=4, relief="solid")
word_label.pack(pady=30)

entry = tk.Entry(window, font=("poppins", 20, "bold"), justify="center", bg="#8e8e8e", fg="#24282f", relief="flat")
entry.pack(ipady=10, ipadx=18)
entry.bind("<Return>", check_answer)

feedback_label = tk.Label(window,text="Type the COLOR of the text",fg="#94a3b8",bg="#24282f",font=("poppins", 12))
feedback_label.pack(pady=14)

tk.Label(window, text="💀 Made by Zain ul Abideen", fg="#ffffff", bg="#24282f", font=("poppins", 10)).pack()

start_new_round()
window.mainloop()