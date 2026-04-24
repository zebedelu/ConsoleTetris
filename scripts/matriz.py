from configs import scaleX

def reset_matriz(self):
    self.matriz = [
        [" "*scaleX for _ in range(self.size[0])] for _ in range(self.size[1])
    ]
def reset_coming_piece_matriz(self):
    self.coming_pieces_matriz = [
        [" "*scaleX for _ in range(5)] for _ in range(19)
    ]
def reset_stored_piece_matriz(self):
    self.stored_piece_matriz = [
        [" "*scaleX for _ in range(4)] for _ in range(4)
    ]