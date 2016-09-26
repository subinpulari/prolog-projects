# Unbeatable Tic-Tac-Toe game using Naive Minimax Algorithm

### Intro
The game is coded in SWI-PROLOG 7.2.3 and Python 2.7.12. The GUI is created using Tkinter module of python. The PROLOG-Python interface is created using the python subprocess module. The game was tested in Linux systems. 

### Setting Up
 - In your Linux system, make sure you have Python 2.7 installed
 - Tkinter requires **python-tk** package. Install it using:

    ```
    sudo apt-get install python-tk
    ```
 - Install latest SWI-PROLOG from http://www.swi-prolog.org/ or use:
    ```
    sudo apt-add-repository ppa:swi-prolog/stable
    sudo apt-get update
    sudo apt-get install swi-prolog
    ```
 - Download this directory to your system
 - Open this directory in terminal and type the command below to start the game:
    
    ```
    python main.py
    ```

### Working
The moves are predicted by the AI using naive Minimax Algorithm, by producing the search tree and choosing the best path at each board state. No heuristic values are applied.A slight delay could occur in the first move due to larger time required for choosing the move at initial board states.

###References:

1. Artificial Intelligence : A Modern Approach by Stuart Russel and Peter Norvig
2. PROLOG Programming for Artificial Intelligence by Ivan Bratko
3. http://neverstopbuilding.com/minimax

