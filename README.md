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

# Design Doc
I honestly have no clue how to organize this, because I'm writing a design doc within what I thought was already the design doc. This section is meant to be kind of like what a college project website looks like, where theres sections for what needs to be done and any simply code for understanding only. Here goes nothing.

Throughout this project, I am following YouTuber Tech With Tim's Python/Pygame Checkers Tutorial. This design doc will be written as if his Checkers code is the skeleton code for my project, and I will add my Chess ideas as if they were assignments in a school project. My inspiration for such a structure comes from my programming projects in UC Berkeley. The formatting specifically is a culmination of projects I've done from the CS61 series and from CS 184.

