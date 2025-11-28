
def generate_welcome_letter(student_name, course_name, output_file="welcome_letter.txt"):

    message = (
        f"Dear {student_name},\n\n"
        f"Welcome to the {course_name} course! We are excited to have you on board.\n"
        "We hope you enjoy learning and achieve great success.\n\n"
        "Best regards,\n"
        "The Academic Team"
    )


    with open(output_file, "w") as file:
        file.write(message)

    print(f"Welcome letter generated successfully in {output_file}.")

# Example usage:
generate_welcome_letter("Alice Johnson", "Data Science")
