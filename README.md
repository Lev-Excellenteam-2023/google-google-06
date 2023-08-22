# Project Name

*Quick description. E.g., "A tool that analyzes fruit prices over time." (Replace with your project description)*
"A tool that suggests completions to an input string."

## Algorithms & Structures
### Data structure
- **Example Algorithm**: Used to analyze fruit price trends. *(This is just an example. Replace with your algorithm or data structure and its role in the code flow.)*
- **Outer dictionary**: Dictionary of the all words from the data files.
  - *Key*: A word from data files.
  - *Value*: Inner dictionary
- **Inner dictionary**:
  - *Key*: Tuple of (file path, line number).
  - *Value*: List of \[offsets of the word in this line]
 
### Algorithms
  - **Initialization**: Each word is saved in the dictionary with detailes of at which file, which line number and the offset in the line.
  - **Searching word**: Each word from input found in dictinary
  - **Sentence Completion**: After that the firts and second words found makig intersection between the words files and line nmber. Continuing to do that wit the word                                    after. Checking if there is an order of words offset one after one. Returns the 5 results with the highest scores. 
  - **Sentence Correction**: 

## Detailed Code Flow

### Loading the Data:
  1. 
### Read Sentence from the User:
### If the Number of Sentences is Less Than 5:

*Start by detailing how you've set up your main data structures. E.g., "We begin by collecting fruit prices from various sources." Then, explain the core logic or algorithm. E.g., "Next, we apply the Example Algorithm to identify price spikes." Conclude with any post-processing or output generation. E.g., "Finally, we visualize the price trends on a graph."*

**Hint**: This section is just a placeholder example of fruit prices. Replace it with a clear and detailed flow of your actual project's logic, algorithms, and processes.
