# CTD 1D README File

# Project Title

# Project Description

What our Project does
This game is aimed at

What the Program aims to solve

Why we used the technologies we did

Some of the challenges we faced and features we hope to implement in the future

# Table Of Contents

# Things Used in our Program

## Minimax Algorithm

The Mini-max algorithm is a recursive or backtracking algorithm which is used in decision-making and game theory. It provides an optimal move for the player assuming that opponent is also playing optimally. It uses recursion to search through the game-tree. It computes the minimax decision for the current state.

### How it Works

For this algorithm, two players play the game, one is called MAX and other is called MIN. Both the players fight it as the opponent player gets the minimum benefit while they get the maximum benefit. They are opponents of each other, where MAX will select the maximized value and MIN will select the minimized value. 

The minimax algorithm then performs a depth-first search algorithm for the exploration of the complete game tree and proceeds all the way down to the terminal node of the tree, then backtrack the tree as the recursion.

## Display Module

This module generates UI elements displayed on the GUI using the ttk widgets provided by Tk. The two main elements are the current position of the tic-tac-toe game which displays of the left and the list of possible future states on the right.

### How it Works

All the functions in the display module (except funcClearContainer and funcFirstDiffIndex) take the following inputs;
- A root, the ttk container that the frame is to be generated in
- A style dictionary defining the appearance of the ttk widgets
- Other inputs specific to the functions as detailed below

#### Functions
1) funcFirstDiffIndex: This takes in two lists of equal length and returns the index of the first item between both lists that difer. It is used exclusively by funcGenBoard to identify where the next position is.
2) funcGenBoard: 

## Tkinter

Tkinter is a Python package that provides various controls, such as buttons, labels and text boxes used in a GUI application. These controls are commonly called Widgets.

For the game, the Tkinter programme takes in a list of 9 strings. The strings are either 'X's','O's' or an empty string (""). All strings are then displayed sequentially in a tic-tac-toe grid.

## Dependencies 

Libraries Used

# How to Run the Project

Provide a step-by-step description of how to get the development environment set and running.

# How to Use the Project

# Credits

1003608 Izzah Sarah Binte Omer Ali Saifudeen

1005790 Bryan Goh Yew Weng

1006858 Lim Kay Yuen Darryl

1006869 Teo Zheo Joshua

1006910 Edison Ang


[Readme](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/ )

[Minimax](https://www.javatpoint.com/mini-max-algorithm-in-ai)

[Tkinker](https://www.tutorialspoint.com/python/python_gui_programming.htm#:~:text=Tkinter%20provides%20various%20controls%2C%20such,controls%20are%20commonly%20called%20widgets.&text=Sr.No.&text=The%20Button%20widget%20is%20used%20to%20display%20buttons%20in%20your%20application.)

# Badges

# Tests

# Licences
