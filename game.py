from pieces.pieces.Cube import Cube
from pieces.pieces.LLeftFormat import LLeft
from pieces.pieces.LRightFormat import LRight
from pieces.pieces.LargePiece import LargePiece
from pieces.pieces.LeftSkew import LeftSkew
from pieces.pieces.RightSkew import RightSkew
from pieces.pieces.TFormat import TFormat
from scripts import controls, UI, score, matriz

import time, random
from configs import size, inicial_level

class Game:
    def __init__(self):
        self.size = size

        inicial_piece = self.choice_random_piece()
        self.objects = [inicial_piece]
        self.fallingPiece = inicial_piece

        # Delay do teclado, para que não fique espamando a tecla
        self.rotate_piece_keyboard_state = False
        self.drop_piece_keyboard_state = False
        self.delay_to_move = 0
        self.stored_piece = None
        self.allow_to_store = True

        self.comming_pieces = []
        self.comming_pieces = [
            self.random_piece() for _ in range(5)
        ]

        self.lines_to_next_level = 0
        self.player_points = 0
        self.level = inicial_level
        
        # Definindo as matrizes
        matriz.reset_matriz(self)
        matriz.reset_stored_piece_matriz(self)
        matriz.reset_coming_piece_matriz(self)
    
    def run(self):
        while True:
            self.update()
            self.render()
            time.sleep(0.05) #20 FPS

    def update(self):
        for object in self.objects:
            object.update()

        if self.fallingPiece:
            controls.update(self)
        # se tiver alguma peça caindo, ela pode ser movida
        controls.move(self)
        # Aumentar o level dependendo da quantidade de linhas limpas
        score.update(self)

    def render(self):
        for object in self.objects:
            object.render()
        self.draw()

    def choice_random_piece(self):
        return random.choice([
            LLeft(self, [3,1]),
            LRight(self, [3,1]),
            Cube(self, [3,1]),
            LargePiece(self, [3,1]),
            LeftSkew(self, [3,1]),
            TFormat(self, [3,1]),
            RightSkew(self, [3,1])
        ])

    def random_piece(self):
        self.comming_pieces.append(self.choice_random_piece())

        first_piece = self.comming_pieces[0]
        self.comming_pieces.pop(0)
        return first_piece
    
    def check_for_lines(self):
        score.check_for_lines(self)
    
    def draw(self): 
        UI.draw_shadow_piece(self)
        UI.draw_coming_pieces(self)
        UI.draw_stored_piece(self)
        UI.draw(self)
        
    def reset_matriz(self):
        matriz.reset_matriz(self)

    def reset_coming_piece_matriz(self):
        matriz.reset_coming_piece_matriz(self)

    def reset_stored_piece_matriz(self):
        matriz.reset_stored_piece_matriz(self)