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
            temp = Queen(piece.row, piece.col, piece.color)
            self.piece = temp
        
    # returns either 0 or a Piece object
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
                    #self.board[row].append(Pawn(row, col, BLACK))
                    self.board[row].append(0)
                    
                elif row == 6:
                    #fill with white pawns
                    #self.board[row].append(Pawn(row, col, WHITE))
                    self.board[row].append(0)
                    
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
              
    def remove(self, row, col):
        self.board[row][col] = 0
                         
    # moves is a dictionary where the key is the location for the piece to be moved to and the value is an array of pieces to be removed.
    # remove before moving
    def get_valid_moves(self, piece):
        if piece.color == WHITE:
            direction = -1 #up the board
        else:
            direction = 1 #down the board
            
        if type(piece) == Rook:
            #rook logic
            moves = self.get_valid_moves_rook(piece)
            
        elif type(piece) == Knight:
            #knight logic
            moves = self.get_valid_moves_knight(piece)
            
        elif type(piece) == Bishop:
            #bishop logic
            moves = self.get_valid_moves_bishop(piece)
            
        elif type(piece) == Queen:
            #queen logic
            moves = self.get_valid_moves_rook(piece)
            moves.update(self.get_valid_moves_bishop(piece))
            
        elif type(piece) == King:
            #king logic
            moves = self.get_valid_moves_king(piece)
            
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
        # used not zero because for some reason doesn't work if I check Piece instead
        if self.within_border(row + direction, col + 1) and self.get_piece(row + direction, col + 1) != 0 and self.get_piece(row + direction, col + 1).color != piece.color:
            moves.update({(row + direction, col + 1): [(row + direction, col + 1)]})
            
        if self.within_border(row + direction, col - 1) and self.get_piece(row + direction, col - 1) != 0 and self.get_piece(row + direction, col - 1).color != piece.color:
            moves.update({(row + direction, col - 1): [(row + direction, col - 1)]})
        
        return moves
    
    
    def get_valid_moves_rook(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        
        # check pieces going up, down, left, and right
        #   check if current piece is empty (0), current color, or opponents color and within borders of board
        #       if empty, add to moves and continue checking
        #       elif opponent, add piece to valid moves and stop
        #       elif current color, stop without including current coordinates
        
        # check direction up
        for up in range(row - 1, -1, -1):
            print("up:")
            if self.within_border(row, up):
                current = self.get_piece(up, col)
                if current == 0:
                    print(" empty")
                    moves.update({(up, col) : []})
                elif current.color != piece.color:
                    print(" enemy")
                    moves.update({(up, col): [(up, col)]})
                    break
                else: # current.color = piece.color
                    print(" ally")
                    break
            
            
        # check direction down
        for down in range(row + 1, ROWS):
            print("down:")
            if self.within_border(row, down):
                current = self.get_piece(down, col)
                if current == 0:
                    print(" empty")
                    moves.update({(down, col) : []})
                elif current.color != piece.color:
                    print(" enemy")
                    moves.update({(down, col): [(down, col)]})
                    break
                else: # current.color = piece.color
                    print(" ally")
                    break
                
        
        
        # check direction right
        for right in range(col + 1, COLS):
            print("right:")
            if self.within_border(right, col):
                current = self.get_piece(row, right)
                if current == 0:
                    print(" empty")
                    moves.update({(row, right) : []})
                elif current.color != piece.color:
                    print(" enemy")
                    moves.update({(row, right): [(row, right)]})
                    break
                else: # current.color = piece.color
                    print(" ally")
                    break
                
        # check direction left
        for left in range(col - 1, -1, -1):
            print("left")
            if self.within_border(row, col):
                current = self.get_piece(row, left)
                if current == 0:
                    print(" empty")
                    moves.update({(row, left) : []})
                elif current.color != piece.color:
                    print(" enemy")
                    moves.update({(row, left): [(row, left)]})
                    break
                else: # current.color = piece.color
                    print(" ally")
                    break
                
        return moves
            
    
    def get_valid_moves_knight(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        
    def get_valid_moves_bishop(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        
        return moves
    
    def get_valid_moves_queen(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        
    def get_valid_moves_king(self, piece):
        moves = {}
        row = piece.row
        col = piece.col
        
        
    def within_border(self, row, col):
        # Check if the move is within the board boundaries
        if row >= 0 and col >= 0 and row < ROWS and col < COLS:
                return True
        return False
        