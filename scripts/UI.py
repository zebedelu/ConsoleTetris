import os
from configs import scaleY, scaleX, lines_for_the_next_level
from pieces.generic.shadowPiece import ShadowPiece

def draw(self):
    os.system("cls")
    all_to_show = "┌"+("─"*((scaleX*self.size[0])+(((10*scaleX))) - (scaleX-2)))+"┐\n"
    for index_linha, linha in enumerate(self.matriz):
        for _ in range(scaleY):
            # Mostrar as peças no tabuleiro
            all_to_show += "│"
            for valor in linha:
                all_to_show += valor
            all_to_show += "\033[0m"
            all_to_show += "│"
            # Mostrar a região das peças que estão vindo
            if index_linha < len(self.coming_pieces_matriz):
                for valor in self.coming_pieces_matriz[index_linha]:
                    all_to_show += valor
                all_to_show += "\033[0m"
                all_to_show += "│"
            
            # Mostrar a região da peça armazenada
            if index_linha < len(self.stored_piece_matriz):
                for valor in self.stored_piece_matriz[index_linha]:
                    all_to_show += valor
                all_to_show += "\033[0m"
                all_to_show += "│"
            
            if index_linha == len(self.stored_piece_matriz):
                all_to_show += "─"*(4*scaleX)+"┘"
            if index_linha == len(self.coming_pieces_matriz):
                all_to_show += "─"*(5*scaleX)+"┘"
            all_to_show += "\n"
    all_to_show += "└"+("─"*scaleX*self.size[0])+"┘"
    print(all_to_show)
    print(f"Pontos: {self.player_points}")
    print(f"Level: {self.level}")
    print(f"Linhas restantes: {lines_for_the_next_level - self.lines_to_next_level}")

    self.reset_matriz()

def draw_shadow_piece(self):
    if self.fallingPiece and self.size[1]-self.fallingPiece.pos[1] > 3:
        shadow_piece = ShadowPiece(self, self.fallingPiece.pos, self.fallingPiece.relative_points)
        shadow_piece.rotationId = self.fallingPiece.rotationId
        if shadow_piece.pos[1] + 2 < self.size[1]:
            shadow_piece.pos[1] += 2
        shadow_piece.isGhostBlock = True
        shadow_piece.color = "\033[38;2;100;100;100m"
        for _ in range(400):
            shadow_piece.update()
        shadow_piece.render()

def draw_coming_pieces(self):
    self.reset_coming_piece_matriz()
    y = 1
    for piece in self.comming_pieces:
        l = 0
        for rel_points in piece.piece():
            global_matriz_pos = [
                2 + rel_points[0],
                y + rel_points[1]
            ]
            self.coming_pieces_matriz[global_matriz_pos[1]][global_matriz_pos[0]] = piece.color+("▓"*scaleX)
        y += 4

def draw_stored_piece(self):
    self.reset_stored_piece_matriz()
    if self.stored_piece is None:
        return
    
    for rel_points in self.stored_piece.piece():
        global_matriz_pos = [
            2 + rel_points[0],
            2 + rel_points[1]
        ]
        self.stored_piece_matriz[global_matriz_pos[1]][global_matriz_pos[0]] = self.stored_piece.color+("▓"*scaleX)