
def set_terminal_size(size_x:int, size_y:int):
    global terminal_width, terminal_height, blank_frame
    terminal_width = size_x
    terminal_height = size_y

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


def draw_point(pos_x:int, pos_y:int):
    if pos_x < 0 or pos_y < 0:
        return
    if pos_x >= terminal_width or pos_y >= terminal_height:
        return
    i = pos_y * (terminal_width + 1) + pos_x
    frame_map[i] = "@"


def draw_line(pos0_x, pos0_y, pos1_x, pos1_y):
    pass


set_terminal_size(80, 22)

new_frame()

draw_point(0, 0)
draw_point(79, 21)

draw_frame()
