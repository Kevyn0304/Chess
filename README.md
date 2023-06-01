# Chess
This project is to create a custom chess game, everything down from the board itself and the interactivity of it to the AI logic. It's technically two separate projects, one being the board and graphics and the other being the AI, but hopefully I can have both in this repo.

# Table of Contents
1. Classes
2. [Checklist](#checklist)

# Classes
* Board
* Pieces
  * Rook
    * Has_moved to check for castling
  * Bishop
  * Knight
  * Queen
  * King
    * Has_moved to check for castling
  * Pawn
    * Has_moved to check for castling

# Checklist <a name="checklist"></a>
- [x] Draw the basic empty chess board
- [ ] Draw pieces in correct spots
- [ ] Make sure each piece has it's own logic
- [ ] Ensure proper movement
- [ ] Show valid places to move
- [ ] Capturing works
- [ ] Castling works
- [ ] Pinned pieces are reinforced
- [ ] Change board to play from blacks perspective
- [ ] Add move history (stack)

# Design Doc
I honestly have no clue how to organize this, because I'm writing a design doc within what I thought was already the design doc. This section is meant to be kind of like what a college project website looks like, where theres sections for what needs to be done and any simply code for understanding only. Here goes nothing.

Throughout this project, I am following YouTuber Tech With Tim's Python/Pygame Checkers Tutorial. This design doc will be written as if his Checkers code is the skeleton code for my project, and I will add my Chess ideas as if they were assignments in a school project. My inspiration for such a structure comes from my programming projects in UC Berkeley. The formatting specifically is a culmination of projects I've done from the CS61 series and from CS 184.

We first created a main.py file to begin writing our code. We also created a Chess subfolder to contain any files regarding the actual game. We create a \_\_init\_\_.py file at the root directory and within the Chess folder to initialize the folders as packages. After doing this, we go back to teh main.py file and import pygame as well as initialize our program window.

Then we create a constants.py file in the Chess folder that will hold any constants that we will use throughout the project, like the values for our window's width and height. Here we also add ROWS and COLS, SQUARE_SIZE, and RGB color codes for white, black, and blue.

We now go back to main.py and create our main function, creating a clock to keep our window running at a constant framerate, and creating an event loop.

## board.py
Then we create a new file within Chess called board.py, which will take care of the chessboard and how it looks and its represented internally. Here we make a method called draw_squares, which will simply draw the checkered black and white pattern of a traiditonal chessboard.

## piece.py
In order to fill the internal representation of our chessboard with the correct chess pieces, we need to create a Piece class. However, because of the many pieces in chess, each with different properties, we will make subclasses of Piece for each one. 

Havent updated in a long time, skipped a lot of stuff. but the following is now pawn movement implementation
### Pawn Movement
