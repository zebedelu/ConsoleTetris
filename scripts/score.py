from configs import lines_for_the_next_level, ponctuation_per_lines

def update(self):
    if self.lines_to_next_level > lines_for_the_next_level and self.fallingPiece:
        self.level += 1
        self.lines_to_next_level = 0
        self.fallingPiece.delayToDown = 20 - self.level
    
def check_for_lines(self):
    # Contar linha por linha para ver qual fez ponto
    lines_with_possible_points = {}
    for block in self.objects[:]:
        if not block.pos[1] in lines_with_possible_points:
            lines_with_possible_points[block.pos[1]] = [block]
        else:
            lines_with_possible_points[block.pos[1]].append(block)
    amount_lines = 0
    
    for line in lines_with_possible_points:
        if len(lines_with_possible_points[line]) == self.size[0]:
            amount_lines += 1
            y = lines_with_possible_points[line][0].pos[1]
            # Remove aquela linha inteira
            for block in lines_with_possible_points[line]:
                self.objects.remove(block)
            
            # move todos que estavam acima 1 casa abaixo
            for block in self.objects:
                if block.pos[1] < y:
                    block.pos[1] += 1
    
    if amount_lines >= 1:
        self.player_points += ponctuation_per_lines[amount_lines] * (self.level + 1)
        self.lines_to_next_level += amount_lines