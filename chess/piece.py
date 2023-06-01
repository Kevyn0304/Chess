import pygame
from abc import ABC
from .constants import *

class Piece(ABC):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.moved = False
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
        self.moved = True
        
    
    def __repr__(self):
        return str(self.color)
    
class Rook(Piece):
    def draw(self, win):
        if self.color == BLACK:
            win.blit(BLACK_ROOK, (self.x - BLACK_ROOK.get_width()//2, self.y - BLACK_ROOK.get_height()//2))
        else:
            win.blit(WHITE_ROOK, (self.x - WHITE_ROOK.get_width()//2, self.y - WHITE_ROOK.get_height()//2))
                
class Knight(Piece):
    def draw(self, win):
        if self.color == BLACK:
            win.blit(BLACK_KNIGHT, (self.x - BLACK_KNIGHT.get_width()//2, self.y - BLACK_KNIGHT.get_height()//2))
        else:
            win.blit(WHITE_KNIGHT, (self.x - WHITE_KNIGHT.get_width()//2, self.y - WHITE_KNIGHT.get_height()//2))

class Bishop(Piece):
    def draw(self, win):
        if self.color == BLACK:
            win.blit(BLACK_BISHOP, (self.x - BLACK_BISHOP.get_width()//2, self.y - BLACK_BISHOP.get_height()//2))
        else:
            win.blit(WHITE_BISHOP, (self.x - WHITE_BISHOP.get_width()//2, self.y - WHITE_BISHOP.get_height()//2))

class Queen(Piece):
    def draw(self, win):
        if self.color == BLACK:
            win.blit(BLACK_QUEEN, (self.x - BLACK_QUEEN.get_width()//2, self.y - BLACK_QUEEN.get_height()//2))
        else:
            win.blit(WHITE_QUEEN, (self.x - WHITE_QUEEN.get_width()//2, self.y - WHITE_QUEEN.get_height()//2))

class King(Piece):
    def draw(self, win):
        if self.color == BLACK:
            win.blit(BLACK_KING, (self.x - BLACK_KING.get_width()//2, self.y - BLACK_KING.get_height()//2))
        else:
            win.blit(WHITE_KING, (self.x - WHITE_KING.get_width()//2, self.y - WHITE_KING.get_height()//2))

class Pawn(Piece):
    def draw(self, win):
        if self.color == BLACK:
            win.blit(BLACK_PAWN, (self.x - BLACK_PAWN.get_width()//2, self.y - BLACK_PAWN.get_height()//2))
        else:
            win.blit(WHITE_PAWN, (self.x - WHITE_PAWN.get_width()//2, self.y - WHITE_PAWN.get_height()//2))