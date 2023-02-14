from data import question_bank_1
import json
program_on = True

while program_on:
    question = input("Enter question: ")
    if question == "stop":
        program_on = False
    answer = input("Enter answer: ")
    with open("data.py", "a") as file2:
        question_bank_1.update({question: answer})

question_bank_1.popitem()
json_question_bank_1 = json.dumps(question_bank_1, indent=8)

with open("data.py", "w") as file3:
    file3.write(f"question_bank_1 = {json_question_bank_1}")