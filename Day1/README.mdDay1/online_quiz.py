# Online Quiz Scoring System

# List of questions, options, and correct answers
quiz = [
    {
        "question": "1. What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "2. What is 2 + 2?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 22"],
        "answer": "B"
    },
    {
        "question": "3. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "4. Who wrote 'Romeo and Juliet'?",
        "options": ["A. Dickens", "B. Shakespeare", "C. Hemingway", "D. Tolkien"],
        "answer": "B"
    },
    {
        "question": "5. Which gas do plants absorb from the air?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    }
]

score = 0

# Loop through each question
for q in quiz:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")

# Final Score
print(f"\nYour total score is {score} out of {len(quiz)}.")
