from tkinter import *

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Chennai", "Kolkata"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for AI?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Unit",
            "Control Processing Unit"
        ],
        "answer": "Central Processing Unit"
    }
]

current_q = 0
score = 0

def load_question():
    question_label.config(text=questions[current_q]["question"])
    selected_option.set(None)

    for i in range(4):
        options[i].config(
            text=questions[current_q]["options"][i],
            value=questions[current_q]["options"][i]
        )

def check_answer():
    global current_q, score

    if selected_option.get() == questions[current_q]["answer"]:
        feedback_label.config(text="Correct!", fg="green")
        score += 1
    else:
        feedback_label.config(text="Incorrect!", fg="red")

    current_q += 1
    window.after(1000, next_question)

def next_question():
    if current_q < len(questions):
        load_question()
        feedback_label.config(text="")
    else:
        question_label.config(
            text=f"Quiz Over! Score: {score}/{len(questions)}"
        )
        for rb in options:
            rb.config(state=DISABLED)

window = Tk()
window.title("Quiz Game")
window.geometry("500x350")

question_label = Label(window, text="", font=("Arial", 14), wraplength=450)
question_label.pack(pady=20)

selected_option = StringVar()

options = []
for i in range(4):
    rb = Radiobutton(
        window,
        text="",
        variable=selected_option,
        value="",
        font=("Arial", 12)
    )
    rb.pack(anchor="w")
    options.append(rb)

Button(window, text="Submit", command=check_answer).pack(pady=15)

feedback_label = Label(window, text="", font=("Arial", 12))
feedback_label.pack()

load_question()
window.mainloop()
