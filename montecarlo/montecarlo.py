import numpy as np
import pandas as pd

class Die():
    '''This Die class defines an object which has N sides, or “faces”, and W weights, and can be rolled to select a face.'''
    
    def __init__(self, faces):
        '''
        This initializer takes an array of faces (strings or numbers) as an input and defines an unnormalized uniform distribution over the sample space of faces, storing this distribution as a private dataframe.
        '''
        if len(set(map(type, faces))) == 1:
            self.faces = np.array(faces)
            self.weights = np.ones(len(faces))
            self._die = pd.DataFrame({'faces':self.faces, 'weights':self.weights})
        else:
            return print('Please input face values of the same data type.')
        
    def change_weight(self, face, new_weight):
        '''
        Purpose: to change the weight of a single side
        Inputs: 
            - the face value to be changed (string or number depending on initialization)
            - the new weight (float)
        Output: a modified weights distribution
        '''
        if face not in self.faces:
            return print('Please input a valid face value.')
        try:
            new_weight = float(new_weight)
        except ValueError:
            return print('Please input a valid weight value (i.e. a float).')       
        self.weights[self.faces == face] = new_weight
        self._die['weights'] = self.weights
                
    def roll(self, n = 1):
        '''
        Purpose: to roll the die one or more times
        Input: a number to specify how many times the dice should be rolled
        Output: a list of outcomes
        '''
        try:
            n = round(float(n))
        except ValueError:
            return print('Please input a valid number of rolls (i.e. an integer).')
        probs = [i/sum(self.weights) for i in self.weights]
        return [self._die.faces.sample(weights=probs).values[0] for roll in range(n)]
            
    def show_die(self):
        '''This method shows the die’s current set of faces and weights.'''
        return self._die
    
    
class Game():
    '''This Game class defines an object which consists of rolling of one or more dice of the same kind one or more times.'''
    
    def __init__(self, dice):
        '''This initializer takes a list of already instantiated similar Die objects as its single input parameter.'''
        self.dice = dice
        
    def play(self, n):
        '''
        Purpose: to play the game by rolling the dice a specified number of times
        Input: a number to specify how many times the dice should be rolled
        Output: a private dataframe of shape N rolls by M dice with each entry indicating the face rolled in that instance
        '''
        try:
            n = round(float(n))
        except ValueError:
            return print('Please input a valid number of rolls (i.e. an integer).')
        results = pd.DataFrame()
        for i in range(len(self.dice)):
            results = pd.concat([results, pd.DataFrame({i:self.dice[i].roll(n)})], axis=1)
        results.index = [i+1 for i in range(n)]
        results.index.name = 'roll_number'
        results.columns.name = 'die_number'
        self._results = results

    def show_result(self, form = 'wide'):
        '''
        Purpose: to pass the private dataframe of results to the user
        Input: a form parameter ('wide' or 'narrow'), specifying whether to return the dataframe in 'narrow' or 'wide' form
        Output: the private dataframe of results
        '''
        if form == 'wide':
            return self._results
        elif form == 'narrow':
            return self._results.stack().to_frame('face_rolled')
        elif form not in ['wide','narrow']:
            raise Exception("The form parameter must be 'wide' or 'narrow'.")
    
       
class Analyzer():
    '''This Analyzer class defines an object which takes the results of a single game and computes various descriptive statistical properties about it.'''

    def __init__(self, game):
        '''This initializer takes a game object as its single input parameter.'''
        self.game = game
        self._faces_dtype = game.dice[0].faces.dtype
        
    def jackpot(self):
        '''This method computes how many times the game resulted in all faces being identical and stores a boolean dataframe showing which rolls resulted in a jackpot as a public attribute.'''
        jackpot_df = pd.DataFrame()
        for i in range(len(self.game._results)):
            jackpot_df = pd.concat([jackpot_df, pd.DataFrame({'jackpot': [(len(set(self.game._results.iloc[i])) == 1)]})], axis = 0)
        jackpot_df.index = [i+1 for i in range(len(self.game._results))]
        jackpot_df.index.name = 'roll_number'
        self.jackpots = jackpot_df
        return int(sum(self.jackpots['jackpot']))
    
    def combo(self):
        '''This method computes the distinct combinations of faces rolled along with their counts and stores this as a multi-indexed dataframe in a public attribute.'''
        rolls = [sorted(list(self.game._results.iloc[i])) for i in range(len(self.game._results))]
        self.combos = pd.DataFrame(rolls).value_counts().to_frame('counts')
        
    def face_counts_per_roll(self):
        '''This method computes how many times a given face is rolled in each event and stores this as a dataframe in a public attribute.'''
        fcpr = pd.DataFrame()
        for i in range(len(self.game._results)):
            fcpr = pd.concat([fcpr, pd.DataFrame({'Ace': [sum(list(self.game._results.iloc[i] == 'Ace'))], 'King': [sum(list(self.game._results.iloc[i] == 'King'))], 'Queen': [sum(list(self.game._results.iloc[i] == 'Queen'))], 'Jack': [sum(list(self.game._results.iloc[i] == 'Jack'))]})], axis = 0)
        fcpr.index = [i+1 for i in range(len(self.game._results))]
        fcpr.index.name = 'roll_number'
        self.face_counts_per_roll = fcpr