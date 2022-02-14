# Wordle Solver

## Installation

- Clone this repo using `git clone https://www.github.com/44za12/WordleSolver.git`
- Run `solver.py` using `python3 solver.py`

# How To Use

- Run `solver.py` and try the word mentioned there in your wordle, after wordle's response input the response from wordle in the below format:
- Enter space separated pair of letter and position use 0 for letters that were not found from your try (grey / black colored) and 6 for the letters that were found but are misplaced (yellow colored) for example: if you try "soare" and "s, e" were colored grey, "o, a" were colored yellow and "r" was colored green in the response, enter "s0 e0 o6 a6 r4" in the program. The order doesn't matter!
- Keep entering response and ultimately win!