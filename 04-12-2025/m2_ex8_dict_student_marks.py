def top_n_students(marks: dict, n: int = 3):
    return sorted(marks.items(), key=lambda x: x[1], reverse=True)[:n]

if __name__ == "__main__":
    marks = {
        "Asha": 88,
        "Ravi": 92,
        "Imran": 76,
        "Leena": 92,
        "Kiran": 85
    }
    top_students = top_n_students(marks, 3)
    print("Top 3 students:")
    for name, score in top_students:
        print(f"{name}: {score}")

