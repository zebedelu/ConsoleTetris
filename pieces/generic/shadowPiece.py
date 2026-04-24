from pieces.master.piece import Piece

class ShadowPiece(Piece):
    def __init__(self, game, pos, relative_points):
        super().__init__(game, pos, False)
        self.relative_points = relative_points