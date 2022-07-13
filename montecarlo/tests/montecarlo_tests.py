import numpy as np
import pandas as pd
import unittest
from montecarlo.montecarlo import Die, Game, Analyzer

class DieGameTestSuite(unittest.TestCase):
    '''This DieGameTestSuite class contains the test suite of methods used to unit test the Die, Game, and Analyzer classes.'''
    
    def test_001_init(self):
        '''This test checks that the __init__ method of the Die class correctly initializes a die object.'''
        die = Die(['H', 'T'])
        self.assertTrue(all(np.array(die._die['faces']) == np.array(['H','T'])) and all(np.array(die._die['weights']) == np.ones(len(['H','T']))))
        
    def test_002_change_weight_success(self):
        '''This test checks that the change_weight method of the Die class correctly changes the weight of a single side.'''
        die = Die(['Ace', 'King', 'Queen', 'Jack'])
        die.change_weight('Ace', 10)
        self.assertTrue(die.weights[die.faces == 'Ace'] == 10 and all(weight == 1 for weight in die.weights[die.faces != 'Ace']))
        
    def test_003_change_weight_failure(self):
        '''This test checks that the change_weight method of the Die class does not change the weight of a single side when given an incorrect input.'''
        die = Die(['Ace', 'King', 'Queen', 'Jack'])
        die.change_weight('Ace', 'ten')
        self.assertTrue(die.weights[die.faces == 'Ace'] == 1)
        
    def test_004_roll_success(self):
        '''This test checks that the roll method of the Die class correctly outputs a list of outcomes.'''
        die = Die(['H', 'T'])
        outcomes = die.roll(10)
        self.assertTrue(len(outcomes) == 10 and all(outcome in ['H', 'T'] for outcome in outcomes))
        
    def test_005_roll_failure(self):
        '''This test checks that the roll method of the Die class does not output a list of outcomes when given an incorrect input.'''
        die = Die(['H', 'T'])
        outcomes = die.roll('ten')
        self.assertTrue(outcomes == None)
        
    def test_006_show_die(self):
        '''This test checks that the show_die method of the Die class correctly returns the private dataframe of the .die attribute.'''
        die = Die(['H', 'T'])
        shown = die.show_die()
        self.assertTrue(all(np.array(shown['faces']) == np.array(['H','T'])) and all(np.array(shown['weights']) == np.ones(len(['H','T']))))
        
            
    def test_010_init(self):
        '''This test checks that the __init__ method of the Game class correctly initializes a game object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        self.assertTrue(all(type(die) == Die for die in game.dice))
        
    def test_020_play_success(self):
        '''This test checks that the play method of the Game class correctly generates the ._results attribute of the game object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        self.assertTrue(game._results.shape == (10, 3) and game._results.index.names[0] == 'roll_number' and game._results.columns.names[0] == 'die_number')
                
    def test_030_play_failure(self):
        '''This test checks that play method of the Game class does not generate the ._results attribute of the game object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play('ten')
        self.assertFalse(hasattr(game, '_results'))
        
    def test_040_show_result_narrow(self):
        '''This test checks that the show_result method of the Game class correctly outputs the results dataframe in narrow format when provided the 'narrow' argument.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        result = game.show_result('narrow')
        self.assertTrue(result.shape == (30, 1) and result.index.names == ['roll_number', 'die_number'] and result.columns[0] == 'face_rolled')
        
    def test_050_show_result_failure(self):
        '''This test checks that the show_result method of the Game class raises an exception if the user passes an invalid option (i.e. not 'wide' or 'narrow').'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        with self.assertRaises(Exception):
            game.show_result('standard')
            
                   
    def test_100_init(self):
        '''This test checks that the __init__ method of the Analyzer class correctly initializes an analyzer object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        self.assertTrue(analyzer.game._results.shape == (10, 3))
        
    def test_200_jackpot(self):
        '''This test checks that jackpot method of the Analyzer class outputs a value of the correct type and that it correctly generates the .jackpots attribute of the analyzer object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        jackpots = analyzer.jackpot()
        self.assertTrue(type(jackpots) == int and len(analyzer.jackpots) == 10)
        
    def test_300_combo(self):
        '''This test checks that the combo method of the Analyzer class correctly generates the .combos attribute of the analyzer object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        analyzer.combo()
        self.assertTrue(hasattr(analyzer, 'combos') and analyzer.combos.columns[0] == 'counts' and sum(analyzer.combos['counts']) == 10)
        
    def test_400_face_counts_per_roll(self):
        '''This test checks that the face_counts_per_roll method of the Analyzer class correctly generates the .face_counts_per_roll attribute of the analyzer object.'''
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        analyzer.face_counts_per_roll()
        self.assertTrue(hasattr(analyzer, 'face_counts_per_roll') and analyzer.face_counts_per_roll.shape == (10, 4) and all([sum(analyzer.face_counts_per_roll.iloc[i]) == 3 for i in range(len(analyzer.face_counts_per_roll))]))
           
                       
if __name__ == '__main__':
    unittest.main(verbosity=2)