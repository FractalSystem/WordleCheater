import wordle_cheater
from datetime import datetime, timedelta

time_format = "%d %B %Y"


# Generate a file with the next days_to_generate days of solutions
def generate_multiple_solutions_file(days_to_generate, filename=None):
    dt_now = datetime.now()-timedelta(days=5)
    s = ""
    for i in range(days_to_generate):
        dt = dt_now + timedelta(days=i)
        solution = wordle_cheater.generate_solution(dt)
        s += f"{dt.strftime(time_format)}: {solution}\n"

    if filename is not None:
        with open(filename, "w") as f:
            f.write(s)


if __name__ == "__main__":
    generate_multiple_solutions_file(1000, "out.txt")
