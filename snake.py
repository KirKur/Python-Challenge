from Tkinter import *
import random

# Globals
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20
IN_GAME = True
apple_cnt = 0


# Helper functions
def create_block():
    """ Creates an apple to be eaten """
    global BLOCK
    posx = SEG_SIZE * random.randint(1, (WIDTH - SEG_SIZE) / SEG_SIZE)
    posy = SEG_SIZE * random.randint(1, (HEIGHT - SEG_SIZE) / SEG_SIZE)
    BLOCK = c.create_oval(posx, posy,
                          posx + SEG_SIZE, posy + SEG_SIZE,
                          fill="red")


def main():
    """ Handles game process """
    global IN_GAME
    global TEXT
    global apple_cnt
    if IN_GAME:
        # text.delete(1.0, END)
        # text.insert(1.0, 'Length = ' + str(len(s.segments)))
        c.delete(TEXT)
        TEXT = c.create_text(WIDTH * 9 / 10, HEIGHT / 10,
                             text="Length = " + str(len(s.segments)),
                             font="Arial 15",
                             fill="white")
        s.move()
        head_coords = c.coords(s.segments[-1].instance)
        # x1, y1, x2, y2 = head_coords
        # Check for collision with gamefield edges
        # if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
        #   IN_GAME = False
        # Eating apples
        if head_coords == c.coords(BLOCK):
            s.add_segment()
            apple_cnt += 1
            c.delete(BLOCK)
            create_block()
        # Self-eating
        else:
            for index in range(len(s.segments) - 1):
                if head_coords == c.coords(s.segments[index].instance):
                    IN_GAME = False
        game_speed = 10 if (apple_cnt > 90) else 100 - apple_cnt
        root.after(game_speed, main)

    # Not IN_GAME -> stop game and print message
    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
                      text="GAME OVER!",
                      font="Arial 20",
                      fill="red")


class Segment(object):
    """ Single snake segment """

    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y,
                                           x + SEG_SIZE, y + SEG_SIZE,
                                           fill="white")


class Snake(object):
    """ Simple Snake class """

    def __init__(self, segments):
        self.segments = segments
        # possible moves
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0)}
        # initial movement direction
        self.vector = self.mapping["Right"]

    def move(self):
        """ Moves the snake with the specified vector"""
        for index in range(len(self.segments) - 1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index + 1].instance)
            c.coords(segment, x1, y1, x2, y2)

        # x1, y1, x2, y2 = c.coords(self.segments[-1].instance)
        new_x1 = WIDTH - SEG_SIZE if x1 < 0 else (0 if x2 > WIDTH else x1 + self.vector[0] * SEG_SIZE)
        new_x2 = SEG_SIZE if x2 > WIDTH else (WIDTH if x1 < 0 else x2 + self.vector[0] * SEG_SIZE)
        new_y1 = HEIGHT - SEG_SIZE if y1 < 0 else (0 if y2 > HEIGHT else y1 + self.vector[1] * SEG_SIZE)
        new_y2 = SEG_SIZE if y2 > HEIGHT else (HEIGHT if y1 < 0 else y2 + self.vector[1] * SEG_SIZE)
        c.coords(self.segments[-1].instance,
                 new_x1, new_y1,
                 new_x2, new_y2)

    def add_segment(self):
        """ Adds segment to the snake """
        last_seg = c.coords(self.segments[0].instance)
        x = last_seg[2] - SEG_SIZE
        y = last_seg[3] - SEG_SIZE
        self.segments.insert(0, Segment(x, y))

    def change_direction(self, event):
        """ Changes direction of snake """

        if event.keysym in self.mapping:
            reverse_dir = map(lambda a, b: a + b, self.vector, self.mapping[event.keysym]) == [0, 0]
            if not reverse_dir:
                self.vector = self.mapping[event.keysym]


# Setting up window
root = Tk()
root.title("PythonicWay Snake")

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003300")
c.grid()
# catch keypressing
c.focus_set()
# creating segments and snake
segments = [Segment(SEG_SIZE, SEG_SIZE),
            Segment(SEG_SIZE * 2, SEG_SIZE),
            Segment(SEG_SIZE * 3, SEG_SIZE)]

s = Snake(segments)
# Reaction on keypress
c.bind("<KeyPress>", s.change_direction)

create_block()
TEXT = c.create_text(WIDTH * 9 / 10, HEIGHT / 10,
                     text="Length = " + str(len(s.segments)),
                     font="Arial 15",
                     fill="red")
main()

root.mainloop()
