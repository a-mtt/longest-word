from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
            # setup
        new_game=Game()
            # exercise
        grid=new_game.grid
            # verify
        assert type(grid)==list
        assert len(grid)==9
        for letter in grid:
            assert letter in string.ascii_uppercase

    def test_game_is_valid(self):
        new_game=Game()
        test_grid=list("EOHLLDSWE")
        new_game.grid=list("EOHLLDSWE")
        word_good="HELLO"
        word_bad="NOTE"
        assert new_game.is_valid(word_good)
        assert not new_game.is_valid(word_bad)
        assert new_game.grid==test_grid

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        assert new_game.is_valid('FEUN') is False
