
def create_quiz(questions, output_file="quiz.txt"):
    with open(output_file, "w") as file:
        for i, question in enumerate(questions, start=1):
            file.write(f"{i}. {question}\n")
            file.write("\n")
    print(f"Quiz file '{output_file}' created successfully.")

questions_list = [
    "What is the capital of France?",
    "Who wrote 'Romeo and Juliet'?",
    "What is the square root of 64?",
    "Name the largest planet in our solar system.",
    "What year did World War II end?"
]

create_quiz(questions_list)
