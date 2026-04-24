from configs import scaleX

class Block:
    def __init__(self, game, pos, cor):
        self.pos = pos
        self.game = game
        self.color = cor

    def render(self):
        self.game.matriz[self.pos[1]][self.pos[0]] = (self.color+"▓")*scaleX

    def update(self):
        pass
    