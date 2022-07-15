# DS5100 Final Project

## Metadata

* Title: **Monte Carlo Simulator**
* Class: DS 5100
* Date: 17 July 2022
* Author: Griffin McCauley
* GitHub Repo URL: https://github.com/Griffin-McCauley/DS5100-Final-Project

## Synopsis
### Installing
The most straightforward way to install the Monte Carlo module within this repository is to run the following lines of code from the terminal while inside the desired current working directory:

```
git clone https://github.com/Griffin-McCauley/DS5100-Final-Project.git
pip install -e .
```

This should properly install the module system wide so that you can import the classes associated with this module into any Python environment. However, if you would prefer to install the package directly from GitHub, see this Stack Overflow article (https://stackoverflow.com/questions/15268953/how-to-install-python-package-from-github#:~:text=on%20this%20post.-,To%20install%20Python%20package%20from%20github,need%20to%20clone%20that%20repository.&text=pip%20install%20.,repo%20dir%20will%20work%20too) for instructions on other installation methods.
### Importing
In order to import the Die, Game, and Analyzer classes from this module into another Python file, simply run `from module.module import Die, Game, Analyzer` at the top of your script where you import the other packages and libraries you will need.
### Creating dice
To create an instance of a die object, one simply needs to pass an array of faces (either strings or numbers) into the Die class likeso: `die = Die(['H', 'T'])`

This will initialize a die object with faces H and T with a uniform weight distribution over these two outcomes.

If you would like to change the weights of the die faces, you can use the `change_weight()` method to achieve this by passing in the face value whose weight you would like to change along with the new weight value of that face. The full method call would look like this: `die.change_weight(face_value, new_weight)`

To see the current configuration of your die, running `die.show_die()` will allow you to view all of the faces along with their associated weights.

With the faces and weights set to the desired values, you can roll the die a specific number of times using ```die.roll(number_of_rolls)```, returning a list of outcomes from the rolls.
### Playing games
Once a die object or multiple die objects have been instantiated and configured the way you would like, you can create a game object by passing a list of die objects into the Game class in the following way: `game = Game([die1, die2, die3])`. (Note that the dice being passed in must be similar, meaning that they have the same faces values. The weight values can be different, however.)

Now, once the game object has been initialized, you can proceed to play the game by running `game.play(number_of_plays)`, passing in how many times you would like to roll all of the dice.

The `play()` method above will produce a result that can be viewed using `game.show_result()`. The NxM dataframe produced (where N is the number of rolls and M is the number of dice) will contain the face value outcome of each corresponding roll.
### Analyzing games
Now that a game has been played and the outcomes stored, the results can be analyzed using the Analyzer class. An analyzer object can be instantiated by passing a game object into the Analyzer class in a similar manner as implemented by the previous classes: `analyzer = Analyzer(game)`

With the game results stored in an analyzer object, you can compute a few statistics of interest by using the methods `jackpot()`, `combo()`, and `face_counts_per_roll()`.

The `jackpot()` method will return the number of times a roll of all the dice in the game produced the same outcome, and will also give you access a `jackpots` attribute that allows you to see specifically which rolls were jackpots and which ones weren't.

Using the `combo()` method will generate a `combos` attribute that is a multi-index dataframe showing the unique combinations of outcomes along with their associated prevalence counts.

If you would like to see the number of face counts per roll, you can run `analyzer.face_counts_per_roll()` to get create an attribute `face_counts_per_roll` that will be a dataframe where each row is a single roll and each column is one of the face values and whose entries are the counts of how many times that face value appeared during that roll.

## API Description
### The Die class
This Die class defines an object which has N sides, or “faces”, and W weights, and can be rolled to select a face.
#### Methods
* \_\_init__(self, faces)
    * This initializer takes an array of faces (strings or numbers) as an input and defines an unnormalized uniform distribution over the sample space of faces, storing this distribution as a private dataframe.
* change_weight(self, face, new_weight)
    * Purpose: to change the weight of a single side
    * Inputs: 
        * the face value to be changed (string or number depending on initialization)
        * the new weight (float)
    * Output: a modified weights distribution
* roll(self, n = 1)
    * Purpose: to roll the die one or more times
    * Input: a number to specify how many times the dice should be rolled (defaults to 1)
    * Output: a list of outcomes
* show_die(self)
    * This method shows the die’s current set of faces and weights.
#### Attributes
* faces
    * an array of face values (strings or numbers)
* weights
    * an array of weight values (floats) (initialized to all 1s)

### The Game class
This Game class defines an object which consists of rolling of one or more dice of the same kind one or more times.
#### Methods
* \_\_init__(self, dice)
    * This initializer takes a list of already instantiated similar Die objects as its single input parameter.
* play(self, n)
    * Purpose: to play the game by rolling the dice a specified number of times
    * Input: a number to specify how many times the dice should be rolled
    * Output: a private dataframe of shape N rolls by M dice with each entry indicating the face rolled in that instance
* show_result(self, form = 'wide')
    * Purpose: to pass the private dataframe of results to the user
    * Input: a form parameter ('wide' or 'narrow'), specifying whether to return the dataframe in 'narrow' or 'wide' form (defaults to 'wide')
    * Output: the private dataframe of results
#### Attributes
* dice
    * a list of die objects

### The Analyzer class
This Analyzer class defines an object which takes the results of a single game and computes various descriptive statistical properties about it.
#### Methods
* \_\_init__(self, game)
    * This initializer takes a game object as its single input parameter.
* jackpot(self)
    * This method computes how many times the game resulted in all faces being identical and stores a boolean dataframe showing which rolls resulted in a jackpot as a public attribute.
* combo(self)
    * This method computes the distinct combinations of faces rolled along with their counts and stores this as a multi-indexed dataframe in a public attribute.
* face_counts_per_roll(self)
    * This method computes how many times a given face is rolled in each event and stores this as a dataframe in a public attribute.
#### Attributes
* game
    * a game object
* jackpots
    * a boolean dataframe showing which rolls resulted in a jackpot
* combos
    * a multi-indexed dataframe storing the distinct combinations of faces rolled along with their counts
* face_counts_per_roll
    * a dataframe expressing how many times a given face is rolled in each event

## Manifest
* .gitignore
* LICENSE
* README.md
* final-project-submission.ipynb
* letter-freqs.csv
* montecarlo_demo.ipynb
* setup.py
* sgb-words.txt
* montecarlo/
  * \_\_init__.py
  * montecarlo.py
  * tests/
    * montecarlo_results.txt
    * montecarlo_tests.py