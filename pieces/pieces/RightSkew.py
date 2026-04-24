from pieces.master.piece import Piece
from configs import colors

class RightSkew(Piece):
    def __init__(self, game, pos):
        super().__init__(game, pos)
        self.relative_points = {
            0:[[0,0],[0,1],[1,0],[1,-1]],
            1:[[0,0],[0,1],[-1,0],[1,1]]
        }
        self.color = colors[4]