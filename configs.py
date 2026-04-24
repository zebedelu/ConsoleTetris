# SCREEN SIZE CONFIGS
size = (10,20)
scaleX = 2
scaleY = 1

# GAME CONFIGS
colors = [
    "\033[38;2;0;255;255m", # ciano      
    "\033[38;2;255;255;0m", # amarelo    
    "\033[38;2;160;0;240m", # roxo
    "\033[38;2;0;255;0m",   # verde claro
    "\033[38;2;255;0;0m",   # vermelho
    "\033[38;2;0;0;255m",   # azul       
    "\033[38;2;255;165;0m"  # laranja
]
moves = {
    "a":[-1,0],
    "d":[1,0],
    "s":[0,1]
}
ponctuation_per_lines = {
    1:40,
    2:100,
    3:300,
    4:1200
}
lines_for_the_next_level = 20
inicial_level = 1

# KEYBOARD CONFIGS
key_to_drop_piece = "space"
key_to_rotate_piece = "up arrow"
key_to_store_piece = "c"