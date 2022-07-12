import numpy as np
import pandas as pd
import unittest
import sys
sys.path.append('/Users/griffinmccauley/Documents/MSDS/DS5100/DS5100-Final-Project')
from montecarlo.montecarlo import Die, Game, Analyzer

class DieGameTestSuite(unittest.TestCase):
    '''This DieGameTestSuite class contains the test suite of methods used to unit test the Die, Game, and Analyzer classes.'''
    
    def test_001_init(self):
        die = Die(['H', 'T'])
        self.assertTrue(all(np.array(die._die['faces']) == np.array(['H','T'])) and all(np.array(die._die['weights']) == np.ones(len(['H','T']))))
        
    def test_002_change_weight_success(self):
        die = Die(['Ace', 'King', 'Queen', 'Jack'])
        die.change_weight('Ace', 10)
        self.assertTrue(die.weights[die.faces == 'Ace'] == 10 and all(weight == 1 for weight in die.weights[die.faces != 'Ace']))
        
    def test_003_change_weight_failure(self):
        die = Die(['Ace', 'King', 'Queen', 'Jack'])
        die.change_weight('Ace', 'ten')
        self.assertTrue(die.weights[die.faces == 'Ace'] == 1)
        
    def test_004_roll_success(self):
        die = Die(['H', 'T'])
        outcomes = die.roll(10)
        self.assertTrue(len(outcomes) == 10 and all(outcome in ['H', 'T'] for outcome in outcomes))
        
    def test_005_roll_failure(self):
        die = Die(['H', 'T'])
        outcomes = die.roll('ten')
        self.assertTrue(outcomes == None)
        
    def test_006_show_die(self):
        die = Die(['H', 'T'])
        shown = die.show_die()
        self.assertTrue(all(np.array(shown['faces']) == np.array(['H','T'])) and all(np.array(shown['weights']) == np.ones(len(['H','T']))))
        
        
        
    def test_010_init(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        self.assertTrue(all(type(die) == Die for die in game.dice))
        
    def test_020_play_success(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        self.assertTrue(game._results.shape == (10, 3) and game._results.index.names[0] == 'roll_number' and game._results.columns.names[0] == 'die_number')
                
    def test_030_play_failure(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play('ten')
        self.assertFalse(hasattr(game, '_results'))
        
    def test_040_show_result_narrow(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        result = game.show_result('narrow')
        self.assertTrue(result.shape == (30, 1) and result.index.names == ['roll_number', 'die_number'] and result.columns[0] == 'face_rolled')
        
    def test_050_show_result_failure(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        with self.assertRaises(Exception):
            game.show_result('standard')
            
            
            
    def test_100_init(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        self.assertTrue(analyzer.game._results.shape == (10, 3))
        
    def test_200_jackpot(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        jackpots = analyzer.jackpot()
        self.assertTrue(type(jackpots) == int and len(analyzer.jackpots) == 10)
        
    def test_300_combo(self):
        die1 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die2 = Die(['Ace', 'King', 'Queen', 'Jack'])
        die3 = Die(['Ace', 'King', 'Queen', 'Jack'])
        game = Game([die1, die2, die3])
        game.play(10)
        analyzer = Analyzer(game)
        analyzer.combo()
        self.assertTrue(hasattr(analyzer, 'combos') and analyzer.combos.columns[0] == 'counts' and sum(analyzer.combos['counts']) == 10)
        
    def test_400_face_counts_per_roll(self):
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