from datetime import datetime
import json

# Base datetime extracted from the Wordle source
start_dt = datetime(2021, 6, 19, 0, 0, 0, 0)

# Wordle's word list, extracted from the Wordle source
with open("data/wordle_words.json", "r") as f:
    words = json.loads(f.read())
    print(len(words))


# Returns the generated solution for a given datetime
def generate_solution(dt):
    delta = dt - start_dt
    index = delta.days % len(words)
    return words[index]


if __name__ == "__main__":
    dt_now = datetime.now()
    solution = generate_solution(dt_now)
    print(f"Today's solution: {solution}")
