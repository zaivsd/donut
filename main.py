# from time import sleep

class Vector2():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

def set_terminal_size(size:Vector2):
    global terminal_width, terminal_height, blank_frame
    terminal_width = size.x
    terminal_height = size.y

    blank_frame = []
    for y in range(terminal_height):
        for x in range(terminal_width):
            blank_frame += "."
        blank_frame += "\n"

def new_frame():
    global frame_map
    frame_map = blank_frame.copy()

def draw_frame():
    print("".join(frame_map), end="\033[3J\033[2J\033[H")

def draw_point(pos:Vector2):
    i = pos.y * (terminal_width + 1) + pos.x
    frame_map[i] = "@"

def draw_line(pos0:Vector2, pos1:Vector2):
    pass

set_terminal_size(Vector2(80, 22))

new_frame()

draw_point(Vector2(0, 0))
draw_point(Vector2(79, 21))

# draw_frame()
print("".join(frame_map))
