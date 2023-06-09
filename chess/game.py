import pygame

from .constants import WHITE, BLACK, BLUE, SQUARE_SIZE
from chess.board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    
    # reason for this is that users only need the reset method, they don't need access to win
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        
    def reset(self):
        self._init()
        
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        
        return False
    
    def _move(self, row, col):
        if self.valid_moves and self.selected and (row, col) in self.valid_moves:
            if self.board.get_piece(row, col) != 0:
                self.board.remove(row, col)
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        
        return True
    
    def draw_valid_moves(self, moves):
        if moves:
            for move in moves:
                row, col = move
                pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15) 
    
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK