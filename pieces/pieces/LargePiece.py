from pieces.master.piece import Piece
from configs import colors

# Form:
# ##
# ##
# ##
# ##

class LargePiece(Piece):
    def __init__(self, game, pos):
        super().__init__(game, pos)
        self.relative_points = {
            0:[[0,0],[1,0],[-1,0],[-2,0]],
            1:[[0,0],[0,1],[0,-1],[0,-2]]
        }

        self.color = colors[0]