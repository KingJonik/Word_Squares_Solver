# Word_Squares_Solver
Repo to contain a program that solves a word square from an input of letters.

# What The Program Does
1. Takes an input consisting of a number, followed by a space, followed by a string of letters of length number^2.
2. Uses this information to filter down all english words into just those that could be possible.
3. Recursively checks each word into a position, j, and assess if it is suitable to remain there and look to build further words on top of it or not.
4. Has some efficiency measures:  
  a. A letter that only appears once in the input, must only appear on the negative diagonal.  
  b. The start of word_j (j > 0) must be equal to the j-th column of the existing word like this:  
  <img width="320" alt="image" src="https://github.com/KingJonik/Word_Squares_Solver/assets/98259607/c624709d-3356-4980-9ed5-8f8bf0413606"> 

# How To Use:
1. Install python (https://www.python.org/downloads/)
2. Run: `pip install requests` (Not completely necessary but if you want to investigate the word_helper.py then this will be needed)
3. Open command line and navigate to the src folder.
4. To run the solver, run: `python main.py arg1 arg2` where `arg1` is the number of words (n) and `arg2` is the string of letters of length n^2.
5. If a word square is solved then the output will look like:  
```
----------------  
--- SOLUTION --- 
----------------  
h e a r t  
e m b e r  
a b o v e  
r e v u e  
t r e e s
```  
6. To run tests, ensuring we are still in the src folder, run: `python -m unittest discover` (takes roughly 5 minutes to run all cases).

# Files Explained:
1. **all_words.txt** - Contains the word list from "http://norvig.com/ngrams/enable1.txt" to be used in the running of the program incase the link doesn't work in the future.
2. **word_helper.py** - Contains function to obtain the word list for the program and also one to re-download the list from the url just incase.
3. **filter_words.py** - The original word list is huge and has many words that simply won't ever be possible for the letter + number of words (n) provided in the initial input, so the aim of this is to filter all_words down to just those that could actually be possible.
4. **word_square_finder.py** - Takes the filtered words and uses a recursive algorithm to check a candidate word against the existing partial word square.
Upon finding an acceptable new word, the list of possible words would be updated when entering the new recursive level as an efficiency measure.
4. **test_cases.py** - Holds test cases used for development and debugging (takes roughly 5 minutes to run all cases).
5. **test_helper.py** - Contains helpers for assessing the test case results.
6. **main.py** - Combines and runs everything together.

# Example Cases:
1. `4 eeeeddoonnnsssrv` - solution: rose oven send ends
3. `4 aaccdeeeemmnnnoo` - solution: moan once acme need
4. `5 aaaeeeefhhmoonssrrrrttttw` - solution: feast earth armer steno throw || feast earth armor stone threw (this one had at least 2 solutions)
5. `5 aabbeeeeeeeehmosrrrruttvv` - solution: heart ember above revue trees
6. `7 aaaaaaaaabbeeeeeeedddddggmmlloooonnssssrrrruvvyyy` - solution: bravado renamed analogy valuers amoebas degrade odyssey

  
