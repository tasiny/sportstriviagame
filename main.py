import tkinter as tk
import random
import os
from data import question_bank_1
from PIL import Image, ImageTk

blue_team_score = 0
red_team_score = 0
image_folder = "nfl_pngs"
image_file_path = f"nfl_pngs/{random.randint(0, 158)}"
trivia_dict = question_bank_1

root = tk.Tk()
root.title("Trivia Game")


def display_image():
    png_list = []
    for filename in os.listdir(image_folder):
        png_list.append(filename)
        f = os.path.join(image_folder, filename)

    top = tk.Toplevel()
    top.title("Identify the Player")
    my_img = ImageTk.PhotoImage(Image.open(f))
    tk.Label(top, image=my_img).pack()
    print(type(f))
    print(type(my_img))


# Define a function to add to the blue_team_score
def add_score_blue(amount):
    global blue_team_score
    blue_team_score += amount
    blue_score_label.config(text=f"Blue Team: {blue_team_score}")


def add_score_red(amount):
    global red_team_score
    red_team_score += amount
    red_score_label.config(text=f"Red Team: {red_team_score}")


# Define a function to show the question
def show_question():
    global current_question, answer
    current_question = random.choice(list(trivia_dict.keys()))
    answer = trivia_dict[current_question]
    question_label.config(text=current_question)
    answer_entry.delete(0, 'end')
    result_label.config(text="")


# Define a function to check the answer
def check_answer():
    global answer,blue_team_score
    user_answer = answer_entry.get()
    if user_answer == answer:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text=f"The correct answer is: {answer}", fg="red")


# Create the widgets
question_label = tk.Label(root, text="", font=("TkDefaultFont", 16))
answer_entry = tk.Entry(root, font=("TkDefaultFont", 16))
check_button = tk.Button(root, text="Check", font=("TkDefaultFont", 16), command=check_answer)
next_question_button = tk.Button(root, text="Next Question", font=("TkDefaultFont", 16), command=show_question)
result_label = tk.Label(root, text="", font=("TkDefaultFont", 16))
blue_score_label = tk.Label(root, text="Blue Team: 0", font=("TkDefaultFont", 16))
blue_add_score_button = tk.Button(root, text="Add", font=("TkDefaultFont", 16), bg="blue", fg="white", command=lambda: add_score_blue(1))
red_score_label = tk.Label(root, text="Red Team: 0", font=("TkDefaultFont", 16))
red_add_score_button = tk.Button(root, text="Add", font=("TkDefaultFont", 16), bg="red", fg="white", command=lambda: add_score_red(1))
bonus_question_button = tk.Button(root, text="Bonus", font=("TkDefaultFont", 16), command=display_image)

# Pack the widgets
question_label.grid(row=0, column=0, columnspan=4)
# answer_entry.grid(row=1, column=0, columnspan=2)
check_button.grid(row=1, column=1, columnspan=2)
next_question_button.grid(row=2, column=1, columnspan=2)
result_label.grid(row=3, column=0, columnspan=4)
blue_score_label.grid(row=4, column=1)
blue_add_score_button.grid(row=4, column=0)
red_score_label.grid(row=4, column=2)
red_add_score_button.grid(row=4, column=3)
bonus_question_button.grid(row=1, column=4)

# Show the first question
show_question()

# Start the event loop
root.mainloop()