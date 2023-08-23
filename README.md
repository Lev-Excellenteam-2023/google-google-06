# Auto-Complition
"A tool that suggests completions to an input string."

## Algorithms & Structures
### Data structure
- **Outer dictionary**: Dictionary of the all words from the data files.
  - *Key*: A word from data files.
  - *Value*: Inner dictionary
- **Inner dictionary**:
  - *Key*: Tuple of (file path, line number).
  - *Value*: List of \[offsetes of the word in this line]
    
### Algorithms
  - **Initialization**: Each word is saved in the dictionary with detailes of at which file, which line number and the offset in the line.
  - **Sentence Completion**: By finding the first word we get list of tuples of files and lines that contain this word and so for the second word. Next step is making intersection between those two lists and so for the all words from the user input. After that we check if there is an sequential indexes order, if so return the 5 sentences with the highes score containing the user input. In case that the all results' scores are equal return the first five results in alphabetic order. 
  - **Sentence Correction**: If there are no 5 results in *`Sentence Completion`* we build a list of the all option of mistakes (miss a letter, aditional a letter or replace letter) and searching for results by *`Sentence Completion`* and scoring each result.
  - **Scoring**:
    The basic score equals to twice length of the input (not include spatial chars like @$,.! ...). *e.g.* The score for input *this is* is 14.
    If need to fix the input the score is
    - Change the 1st char -5
    - Change the 2nd char -4
    - Change the 3rd char -3
    - Change the 4th char -2
    - Change the 5th char or later -1
   
    - Delete or add char
      - 1st char -10
      - 2nd char -8
      - 3rd char -6
      - 4th char -4
      - 5th char or later -2
     
## Detailed Code Flow
### Loading the Data:
  1. Save all the file names (path to file) in a list by going through all the folders.
     ***Note***: The root of the data files should be in enviroment variables in name of **ROOT_PATH** (or in .env file)
  2. Save each word (letter and number only) into the data structue in this format, *word: {(file path, line number): \[offset_1, offset_2 ...], (file path, line number): \[offset_1, offset_2 ...] ... }*
### Read Sentence from the User: 
  1. Get input from user
  2. Clean the input from chars that not alphabethics, numbers or white spaces.
  3. Show the results and allow the user to continue his input. To restar input enter *`#`*. Enter `*` to close the program.
 ### Find sentences to suggest:
  Find appropriate sentences and return the 5 sentences with highest score resulrs.
