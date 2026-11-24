class Vector2():
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

terminal_width = 80
terminal_height = 22

def new_frame():
    global frame_map
    frame_map = []

    for y in range(terminal_height):
        for x in range(terminal_width):
            frame_map += "."
        frame_map += "\n"

def draw_dot(pos:Vector2):
    i = 0
    for y in range(terminal_height):
        i = y * (terminal_width + 1)
        if y == pos.y:
            for x in range(terminal_width):
                if x == pos.x:
                    frame_map[i] = "@"
                i += 1

new_frame()

draw_dot(Vector2(10, 2))
draw_dot(Vector2(20, 13))

print("".join(frame_map))
