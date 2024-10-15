# List of 20 questions with options and correct answers
questions = [
    {
        "question": "1. What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "3. Who wrote 'Hamlet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "4. What is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "5. Which element has the chemical symbol 'O'?",
        "options": ["A. Oxygen", "B. Gold", "C. Silver", "D. Hydrogen"],
        "answer": "A"
    },
    {
        "question": "6. How many continents are there on Earth?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "7. Who painted the Mona Lisa?",
        "options": ["A. Vincent Van Gogh", "B. Pablo Picasso", "C. Michelangelo", "D. Leonardo da Vinci"],
        "answer": "D"
    },
    {
        "question": "8. What is the hardest natural substance on Earth?",
        "options": ["A. Iron", "B. Diamond", "C. Gold", "D. Ruby"],
        "answer": "B"
    },
    {
        "question": "9. How many planets are there in the solar system?",
        "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "B"
    },
    {
        "question": "10. In which year did World War I begin?",
        "options": ["A. 1914", "B. 1918", "C. 1939", "D. 1945"],
        "answer": "A"
    },
    {
        "question": "11. What is the currency of Japan?",
        "options": ["A. Yen", "B. Won", "C. Peso", "D. Dollar"],
        "answer": "A"
    },
    {
        "question": "12. What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"],
        "answer": "C"
    },
    {
        "question": "13. What gas do plants absorb from the atmosphere?",
        "options": ["A. Nitrogen", "B. Carbon Dioxide", "C. Oxygen", "D. Helium"],
        "answer": "B"
    },
    {
        "question": "14. How many bones are there in the human body?",
        "options": ["A. 200", "B. 206", "C. 210", "D. 215"],
        "answer": "B"
    },
    {
        "question": "15. Who invented the telephone?",
        "options": ["A. Thomas Edison", "B. Nikola Tesla", "C. Alexander Graham Bell", "D. Guglielmo Marconi"],
        "answer": "C"
    },
    {
        "question": "16. What is the capital of Australia?",
        "options": ["A. Sydney", "B. Canberra", "C. Melbourne", "D. Brisbane"],
        "answer": "B"
    },
    {
        "question": "17. What is the square root of 64?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    },
    {
        "question": "18. How many letters are there in the English alphabet?",
        "options": ["A. 24", "B. 25", "C. 26", "D. 27"],
        "answer": "C"
    },
    {
        "question": "19. Who was the first man to walk on the moon?",
        "options": ["A. Yuri Gagarin", "B. Buzz Aldrin", "C. Neil Armstrong", "D. Michael Collins"],
        "answer": "C"
    },
    {
        "question": "20. Which country is known as the Land of the Rising Sun?",
        "options": ["A. China", "B. Japan", "C. Thailand", "D. South Korea"],
        "answer": "B"
    }
]

def quiz():
    score = 0  # Initialize score to 0

    # Loop through each question
    for question in questions:
        print(question["question"])  # Print the question
        for option in question["options"]:  # Print the options
            print(option)
        
        # Take user input for the answer
        user_answer = input("Your answer (A/B/C/D): ").upper()

        # Check if the answer is correct
        if user_answer == question["answer"]:
            score += 10  # Add 10 points for correct answer
            print("Correct!\n")
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")
    
    # Output the final result
    print(f"Your final score is {score}/200")

    # Grade based on the score
    if score >= 180:
        grade = 'A'
    elif score >= 160:
        grade = 'B'
    elif score >= 140:
        grade = 'C'
    elif score >= 120:
        grade = 'D'
    elif score >=80:
        grade = 'E'
    else:
        grade = 'F'

    print(f"Your grade is: {grade}")

# Call the quiz function to start the quiz
quiz()
