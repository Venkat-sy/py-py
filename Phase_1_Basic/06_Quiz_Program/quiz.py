"""
Project 6: Quiz Program
External Requirements: None
"""
quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
}
score = 0
for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer: ")
    if answer.lower() == value['answer'].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The answer is:", value['answer'])

print(f"You got {score} out of 2 questions correctly")
