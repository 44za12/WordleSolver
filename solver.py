import string
from collections import defaultdict
from typing import Dict

class Solver:
    def __init__(self) -> None:
        self.possibleWords = defaultdict(lambda: defaultdict(lambda: set()))
        self.nextBestGuesses = set()
        self.__initData()

    def __initData(self) -> None:
        allowedWords = set()
        with open("allwords.txt") as f:
            allowedWords = set(f.readlines())
        with open("commonwords.txt") as f:
            self.commonWords = set(i.strip for i in f.readlines())
        for l in string.ascii_lowercase:
            for word in allowedWords:
                word = word.strip()
                if l in word:
                    self.possibleWords[l][6].add(word)
                if word[0] == l:
                    self.possibleWords[l][1].add(word)
                if word[1] == l:
                    self.possibleWords[l][2].add(word)
                if word[2] == l:
                    self.possibleWords[l][3].add(word)
                if word[3] == l:
                    self.possibleWords[l][4].add(word)
                if word[4] == l:
                    self.possibleWords[l][5].add(word)
                self.nextBestGuesses.add(word)

    def __formattedOut(self, out: str) -> Dict:
        for l, pos in out.split():
            yield l, int(pos)
    
    def check(self, out: str) -> str:
        for l, pos in self.__formattedOut(out):
            if pos == 0:
                self.nextBestGuesses -= self.possibleWords[l][6]
            else:
                self.nextBestGuesses = self.nextBestGuesses.intersection(self.possibleWords[l][pos])
        try:
            nextTry = list(self.nextBestGuesses.intersection(self.commonWords))[0]
        except IndexError:
            nextTry = list(self.nextBestGuesses)[0]
        self.nextBestGuesses.remove(nextTry)
        return nextTry

    def solve(self) -> None:
        nextTry = "soare"
        tries = 1
        print("Enter space separated pair of letter and position use 0 for letters that were not found from your try (grey / black colored) and 6 for the letters that were found but are misplaced (yellow colored) for example: if you try \"soare\" and \"s, e\" were colored grey, \"o, a\" were colored yellow and \"r\" was colored green in the response, enter \"s0 e0 o6 a6 r4\" in the program. The order doesn't matter!\n")
        while tries <= 6:
            out = input(f"\nTry the word \"{nextTry}\".\nInput the response from Wordle in the mentioned format: ")
            if out == "done":
                print("Yay! Congrats!")
                return
            nextTry = self.check(out)
            tries += 1
        print(f"Sorry! In our defense the word could be any of these: \"{self.nextBestGuesses}\" logic beaten by luck :(")

solver = Solver()
solver.solve()
