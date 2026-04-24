from configs import key_to_store_piece, key_to_rotate_piece, key_to_drop_piece, moves
import keyboard

def update(self):
    # Armazenar a peça para usar depois
    if keyboard.is_pressed(key_to_store_piece) and self.allow_to_store:
        self.objects.remove(self.fallingPiece)
        if self.stored_piece:
            self.objects.append(self.stored_piece)
        self.stored_piece, self.fallingPiece = self.fallingPiece, self.stored_piece
        self.allow_to_store = False

    # Detectar seta para cima para poder rotacionar peça
    if keyboard.is_pressed(key_to_rotate_piece) and not self.rotate_piece_keyboard_state:
        self.fallingPiece.rotate()
    self.rotate_piece_keyboard_state = keyboard.is_pressed(key_to_rotate_piece)
    
    # Detectar barra de espaço para soltar a peça
    if keyboard.is_pressed(key_to_drop_piece) and not self.drop_piece_keyboard_state:
        self.fallingPiece.go_directly_down()
    self.drop_piece_keyboard_state = keyboard.is_pressed(key_to_drop_piece)
    
def move(self):
    if not self.fallingPiece is None:
        for tecla in moves:
            if keyboard.is_pressed(tecla) and self.delay_to_move <= 0:
                self.fallingPiece.move(*moves[tecla])
                self.delay_to_move = 1
                break
        self.delay_to_move -= 1
    else:
        self.check_for_lines()
        p = self.random_piece()
        self.fallingPiece = p
        self.objects.append(p)