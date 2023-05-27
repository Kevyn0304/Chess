from abc import ABC
from .constants import WHITE, BLACK, SQUARE_SIZE

class Piece(ABC):
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        
        if self.color == BLACK:
            self.direction = -1
        else:
            self.direction = 1
            
        self.x = 0
        self.y = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col
        self.y = SQUARE_SIZE * self.row
        
    def move_to(self, rank, file):
        self.validate_move(rank, file)
        self.never_moved = False
        self.rank = rank
        self.file = file
    
    black_rook = pygame.image.load('images/black_rook.png')
    def draw(self, win, image):
        win.blit(image, (x, y))
        
    def __repr__(self):
        return str(self.color)
    
class Pawn(Piece):
    """Simple Pawn class. Does not know about en-passant captures
    because that would require some kind of last-move caching, which
    will depend on where you want to go with this code. Uses `dir`
    attribute to indicate direction of travel.

    """
    def __init__(self, *args, dir=1, **kwargs):
        super().__init__(*args, **kwargs)
        self.dir = -1 if dir < 0 else +1

    def valid_moves(self):
        """Yield all valid moves from this location."""

        piece_at = self.board.piece_at
        color = self.color
        file = self.file

        dir = self.dir
        r1 = self.rank + dir

        # Captures
        for f1 in (file-1, file+1):
            if piece_at(r1, f1).color != color:
                yield (r1, f1)

        # Non-captures
        if not piece_at(r1, file):
            yield (r1, file)

            # SPECIAL: Double move if done first 
            r2 = r1 + dir

            if self.never_moved and not piece_at(r2, file):
                yield (r2, file)