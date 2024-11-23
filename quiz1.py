# Assignment 1 : Quiz app data saved in programs memory


# Computer Quiz Program

questions = [
    {
        "question": "What is the basic unit of data in a computer?",
        "options": ["Bit", "Byte", "Word", "Gigabyte"],
        "answer": "Bit"
    },
    {
        "question": "Which of the following is NOT an input device?",
        "options": ["Keyboard", "Mouse", "Monitor", "Scanner"],
        "answer": "Monitor"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Processing Unit", "Control Processing Unit", "Common Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": ["Python", "Java", "C++", "HTML"],
        "answer": "HTML"
    }
]

score = 0
for question in questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_answer = input("Enter your answer (1/2/3/4): ")
    if user_answer == str(question["options"].index(question["answer"]) + 1):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

print(f"\nYour final score is: {score}/{len(questions)}")