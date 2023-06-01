import pygame
from .constants import BLACK, WHITE, COLS, ROWS, SQUARE_SIZE, BLUE
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
              
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
                         
    # moves is a dictionary where the key is the location for the piece to be moved to and the value is an array of pieces to be removed.
    # remove before moving
    def get_valid_moves(self, piece):
        if piece.color == WHITE:
            direction = -1 #up the board
        else:
            direction = 1 #down the board
            
        if type(piece) == Rook:
            #rook logic
            pass
        elif type(piece) == Knight:
            #knight logic
            pass
        elif type(piece) == Bishop:
            #bishop logic
            pass
        elif type(piece) == Queen:
            #queen logic
            pass
        elif type(piece) == King:
            #king logic
            pass
        elif type(piece) == Pawn:
            #pawn logic
            moves = self.get_valid_moves_pawn(piece, direction)
            
        return moves
        
    # gotta return dictionary moves
    def get_valid_moves_pawn(self, piece, direction):
        moves = {}
        row = piece.row
        col = piece.col
        # check in front of pawn if empty square, if so add to possible moves
        if self.get_piece(row + direction, col) == 0:
            moves.update({(row + direction, col): []})
        
        # check first time moving for moving 2 pieces ahead
        if piece.moved == False and self.get_piece(row + direction, col) == 0 and self.get_piece(row + (direction * 2), col) == 0:
            moves.update({(row + (2 * direction), col): []})
            
        # check front right diagonal if enemy piece and record take location
        if self.is_valid_move(row + direction, col + 1) and type(self.get_piece(row + direction, col + 1)) == Pawn and self.get_piece(row + direction, col + 1).color != piece.color:
            moves.update({(row + direction, col + 1): [(row + direction, col + 1)]})
            
        if self.is_valid_move(row + direction, col - 1) and type(self.get_piece(row + direction, col - 1)) == Pawn and self.get_piece(row + direction, col - 1).color != piece.color:
            moves.update({(row + direction, col - 1): [(row + direction, col - 1)]})
        
        return moves
    
    def is_valid_move(self, row, col):
        # Check if the move is within the board boundaries
        if row >= 0 and col >= 0 and row < ROWS and col < COLS:
                return True
        return False
        