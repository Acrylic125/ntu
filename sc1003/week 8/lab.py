import random

def get_ab_score(guess: str, answer: str) -> tuple[int, int]:
    if len(guess) != 4 or len(answer) != 4:
        raise ValueError("Guess and answer must be 4 digits long")
    
    a = 0
    b = 0

    if guess == answer:
        return 4, 0

    utilised = []
    for i in range(len(guess)):
        guess_at_i = guess[i]
        answer_at_i = answer[i]
        
        if guess_at_i not in utilised:
            if guess_at_i == answer_at_i:
                a += 1
            elif guess_at_i in answer:
            # elif answer.find(guess_at_i) != -1:
                b += 1
            utilised.append(guess_at_i)
    
    return a, b

def generate_answer():
    digits = [i for i in range(10)]
    random.shuffle(digits)
    answer = "".join(map(str, digits[0:4]))
    return answer

answer = generate_answer()
print(f"Answer: {answer}")

attempts = 0
while True:
    guess = input("Enter your guess: ")

    try:
        attempts += 1
        a, b = get_ab_score(guess, answer)
        if a == 4:
            print(f"Correct! You guessed the answer in {attempts} attempts.")
            break
        print(f"Guess: {guess}\nA: {a}\nB: {b}")
    except ValueError as e:
        print("Invalid input. Make sure the guess is 4 digits long.")
