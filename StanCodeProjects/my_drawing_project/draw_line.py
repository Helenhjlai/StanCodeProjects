"""
File: draw_line.py
Name: Helen Lai
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5
window = GWindow()
count = 1
circle = GOval(2 * SIZE, 2 * SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    circle.color = 'black'
    onmouseclicked(event)


def event(m):
    """
    this program will draw a circle and a line on different situations.
    if it's the even run, then draw a line.
    on the other hand, if it's the odd run, then draw a circle.
    """
    global count

    if count % 2 != 0:
        window.add(circle, x=m.x - SIZE, y=m.y - SIZE)

    else:
        line = GLine(circle.x + SIZE, circle.y + SIZE, m.x, m.y)
        window.add(line)
        window.remove(circle)

    count += 1  # to count the runs


if __name__ == "__main__":
    main()
