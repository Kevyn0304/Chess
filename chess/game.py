import pygame

from .constants import WHITE, BLACK
from chess.board import Board

class Game:
    def __init__(self, win):
        _init()
        self.win = win
        
    def update(self):
        self.board.draw(self.win)
        pygame.display.update()
        
    
    # reason for this is that users only need the reset method, they don't need access to win
    def _init():
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}
        
    def reset(self):
        _init()