from configs import scaleX, colors
import random, copy
from pieces.generic.block import Block
from abc import ABC

class Piece(ABC):
    def __init__(self, game, pos, isGhostBlock=False):
        self.game = game

        self.isGhostBlock = isGhostBlock
        self.relative_points = {}
        self.pos = list(pos)
        self.anterior_pos = [0,0]

        self.CanMove = True
        self.delayToDown = 20
        self.inicialdelayToDown = self.delayToDown

        self.color = random.choice(colors)
        self.rotationId = 0
    
    def render(self):
        for relative_point in self.piece():
            self.game.matriz[
                self.pos[1] + relative_point[1]
            ][
                self.pos[0] + relative_point[0]
            ] = (self.color+"▓")*scaleX

    def update(self):
        for relative_point in self.piece():
            # Encostou no chão
            if self.pos[1] + relative_point[1] + 1 == self.game.size[1]:
                self.CanMove = False

        if self.CanMove:
            self.delayToDown -= 1
        else:
            if self.game.fallingPiece == self:
                self.game.fallingPiece = None
                
            self.delayToDown = self.inicialdelayToDown
            self.TransformInBlocks()

        if self.delayToDown <= 0:
            self.move(0,1)
            self.delayToDown = self.inicialdelayToDown

        if not self.isGhostBlock:
            self.show_ghost_piece()

    def CheckCollision(object1, block):
        # Checar colisão com o chão
        for relative_point in object1.piece():
            if object1.pos[1] + relative_point[1] + 1 == object1.game.size[1]:
                return True

        # Pegar posição global do objeto 1 e 2
        global_position_obj1 = tuple([
            (object1.pos[0] + rel_pos[0], object1.pos[1] + rel_pos[1])
        for rel_pos in object1.piece()])

        global_position_obj2 = tuple([(
            block.pos[0], block.pos[1]
        )])

        # Ver se ambos possuem alguma posição em comum
        mesma_posicao = set(global_position_obj1) & set(global_position_obj2)

        if list(mesma_posicao):
            return True
        return False
    
    def piece(self):
        return copy.deepcopy(self.relative_points[self.rotationId])
    
    def rotate(self):
        future_position = copy.copy(self)
        future_position.isGhostBlock = True
        future_position.rotationId += 1
        if future_position.rotationId >= len(future_position.relative_points):
            future_position.rotationId = 0
        future_position.update()

        canRotate = True
        for rel_point in future_position.piece():
            global_pos = [
                self.pos[0] + rel_point[0],
                self.pos[1] + rel_point[1]
            ]
            if not 0 <= global_pos[0] < self.game.size[0]:
                canRotate = False
            if not 0 <= global_pos[1] < self.game.size[1]:
                canRotate = False

        if canRotate == False:
            return
        
        for blocks in self.game.objects:
            if blocks != self and blocks != future_position:
                if future_position.CheckCollision(blocks):
                    return

        self.rotationId += 1
        if self.rotationId >= len(self.relative_points):
            self.rotationId = 0

    def move(self, movex, movey):
        if self.pos == self.anterior_pos:
            self.CanMove = False

        if not self.CanMove:
            return
        
        # Checar colisão
        PodeMover = True
        for block in self.game.objects:
            if block == self:
                continue

            block = Block(self.game, block.pos[:], "")
            block.pos[0] -= movex
            block.pos[1] -= movey

            if self.CheckCollision(block):
                PodeMover = False
                if movey != 0:
                    self.CanMove = False
        
        if PodeMover:
            canMove = True
            for rel_point in self.piece():
                global_pos = [
                    self.pos[0] + rel_point[0],
                    self.pos[1] + rel_point[1]
                ]
                if not 0 <= global_pos[0] + movex < self.game.size[0]:
                    canMove = False
                    movex = 0
                if not 0 <= global_pos[1] + movey < self.game.size[1]:
                    canMove = False

            if canMove:
                self.anterior_pos = self.pos[:]
                self.pos[0] += movex
                self.pos[1] += movey

    def TransformInBlocks(self):
        if not self in self.game.objects:
            return
        
        for relative_point in self.piece():
            global_pos = [
                    self.pos[0] + relative_point[0]
                    ,
                    self.pos[1] + relative_point[1]
                ][:]
            b = Block(self.game, global_pos[:], self.color)
            self.game.objects.append(b)

        self.game.allow_to_store = True
        
        self.game.objects.remove(self)
        del self
    
    def go_directly_down(self):
        for _ in range(400):
            self.update()
    
    def show_ghost_piece(self):
        ghost_piece = copy.copy(self)
        ghost_piece.isGhostBlock = True
        ghost_piece.color = "\033[38;2;50;50;50m"
        ghost_piece.render()