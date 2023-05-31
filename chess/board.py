import pygame
from .constants import BLACK, WHITE, COLS, ROWS, SQUARE_SIZE
from .piece import *

class Board:
    def __init__(self):
        self.board = []
        self.create_board()
        
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
        
        #handle pawn promotion
        if type(piece) is Pawn and row == 0 or row == ROWS:
            piece = Queen(piece)
        
    def get_piece(self, row, col):
        return self.board[row][col]
        
    
    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                # board filling logic
                if row == 0:
                    #fill with black pieces in blacks order
                    if col == 0:
                        self.board[row].append(Rook(row, col, BLACK))
                    elif col == 1:
                        self.board[row].append(Knight(row, col, BLACK))
                    elif col == 2:
                        self.board[row].append(Bishop(row, col, BLACK))
                    elif col == 3:
                        self.board[row].append(Queen(row, col, BLACK))
                    elif col == 4:
                        self.board[row].append(King(row, col, BLACK))
                    elif col == 5:
                        self.board[row].append(Bishop(row, col, BLACK))
                    elif col == 6:
                        self.board[row].append(Knight(row, col, BLACK))
                    elif col == 7:
                        self.board[row].append(Rook(row, col, BLACK))
                        
                elif row == 1:
                    #fill with pawns
                    self.board[row].append(Pawn(row, col, BLACK))
                elif row == 6:
                    #fill with white pawns
                    self.board[row].append(Pawn(row, col, WHITE))
                elif row == 7:
                    #fill with white pieces in whites order
                    if col == 0:
                        self.board[row].append(Rook(row, col, WHITE))
                    elif col == 1:
                        self.board[row].append(Knight(row, col, WHITE))
                    elif col == 2:
                        self.board[row].append(Bishop(row, col, WHITE))
                    elif col == 3:
                        self.board[row].append(Queen(row, col, WHITE))
                    elif col == 4:
                        self.board[row].append(King(row, col, WHITE))
                    elif col == 5:
                        self.board[row].append(Bishop(row, col, WHITE))
                    elif col == 6:
                        self.board[row].append(Knight(row, col, WHITE))
                    elif col == 7:
                        self.board[row].append(Rook(row, col, WHITE))
                        
                else:
                    self.board[row].append(0)
                
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)