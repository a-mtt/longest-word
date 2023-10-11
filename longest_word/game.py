"""
A python implementation of the longest word game

"""
import random

class Game:
    """
    Game classe with multiple methods.
    init to generate the grid
    is_valid to test validity of word
    """
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = [chr(random.randint(ord('A'),ord('Z'))) for _ in range(9)]

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        test_grid=self.grid.copy()
        for letter in word:
            if letter not in test_grid:
                return False
            test_grid.remove(letter)
        return True



if __name__=="__main__":
    game = Game()
    print(game.grid) # --> OQUWRBAZE
    my_word = "BAROQUE"
    game.is_valid(my_word) # --> True
