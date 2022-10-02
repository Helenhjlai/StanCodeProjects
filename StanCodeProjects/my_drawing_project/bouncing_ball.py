"""
File: bouncing_ball.py
Name: Helen Lai
-------------------------
Students are going to design a program that simulates a bouncing ball at a starting x and y
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

time = 0
click_swift = False
window = GWindow(800, 500, title='bouncing_ball.py')
circle = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global time, click_swift
    circle.filled = True
    circle.fill_color = 'black'
    window.add(circle, START_X, START_Y)
    onmouseclicked(bounce)

    while True:
        if click_swift:
            if time < 3:  # use TIME to count, if over 3 times, then do nothing
                vy = 2
                while True:
                    circle.move(VX, vy)
                    vy += GRAVITY
                    if circle.y + circle.height >= window.height:
                        vy = -vy * REDUCE
                    if circle.x + circle.width >= window.width:
                        circle.x = START_X
                        circle.y = START_Y
                        window.add(circle)
                        click_swift = False
                        break
                    pause(DELAY)
                time += 1
        pause(DELAY)


def bounce(_):
    """
    this program will swift click_swift to True when user click their mouse in the beginning of
    a new run.
    """
    global click_swift
    click_swift = True


if __name__ == "__main__":
    main()
