"""
File: my_drawing.py
Name: Helen Lai
----------------------
Title: My French Bulldog!

French bulldog is my favorite dog breed.
I really wanna pet a french bulldog, but my mom hates pet's fur which will cause allergy
and she doesn't want to clean our house that full of fur.
I love french bulldog a lot although lots of people said they're ugly.
"""

from campy.graphics.gobjects import GOval, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(400, 400, title='my french bulldog')


def main():
    """
    Title: No one can stop my love for frenchies!

    French bulldog is my favorite dog breed.
    I really wanna pet a french bulldog, but my mom hates pet's fur which will cause allergy
    and she doesn't want to clean our house that full of fur.
    I love french bulldog a lot although lots of people said they're ugly.
    SEE MY DRAWING!!! You'll definitely change your mind!! French bulldogs are REALLY CUTE!
    """
    hear()
    head()
    eye()
    word()


def word():
    line = GLine(80, 350, 320, 350)
    line_u = GLine(80, 290, 320, 290)

    label = GLabel('French Bulldog')
    label.font = '-30'

    window.add(line)
    window.add(line_u)
    window.add(label, x=86, y=340)


def eye():
    circle1 = GOval(10, 20)
    circle1.filled = True
    circle1.filled = 'black'

    circle2 = GOval(10, 20)
    circle2.filled = True
    circle2.fill_color = 'black'

    window.add(circle1, 170, 170)
    window.add(circle2, 215, 170)


def hear():  # 9 parts
    # draw the left side first and then draw a reflection
    triangle1 = GPolygon()
    triangle1.add_vertex((20, 80))
    triangle1.add_vertex((30, 72))
    triangle1.add_vertex((36, 90))

    # make a reflection
    triangle11 = GPolygon()
    triangle11.add_vertex((20 + 2 * (98 - 20), 80))
    triangle11.add_vertex((30 + 2 * (98 - 30), 72))
    triangle11.add_vertex((36 + 2 * (98 - 36), 90))

    triangle2 = GPolygon()
    triangle2.add_vertex((20, 80))
    triangle2.add_vertex((19.7, 100))
    triangle2.add_vertex((36, 90))

    triangle22 = GPolygon()
    triangle22.add_vertex((20 + 2 * (98 - 20), 80))
    triangle22.add_vertex((19.7 + 2 * (98 - 19.7), 100))
    triangle22.add_vertex((36 + 2 * (98 - 36), 90))

    triangle3 = GPolygon()
    triangle3.add_vertex((30, 72))
    triangle3.add_vertex((36, 90))
    triangle3.add_vertex((51, 85))

    triangle33 = GPolygon()
    triangle33.add_vertex((30 + 2 * (98 - 30), 72))
    triangle33.add_vertex((36 + 2 * (98 - 36), 90))
    triangle33.add_vertex((51 + 2 * (98 - 51), 85))

    triangle4 = GPolygon()
    triangle4.add_vertex((36, 90))
    triangle4.add_vertex((19.7, 100))
    triangle4.add_vertex((47, 99.5))

    triangle44 = GPolygon()
    triangle44.add_vertex((36 + 2 * (98 - 36), 90))
    triangle44.add_vertex((19.7 + 2 * (98 - 19.7), 100))
    triangle44.add_vertex((47 + 2 * (98 - 47), 99.5))

    triangle5 = GPolygon()
    triangle5.add_vertex((36, 90))
    triangle5.add_vertex((47, 99.5))
    triangle5.add_vertex((51, 85))

    triangle55 = GPolygon()
    triangle55.add_vertex((36 + 2 * (98 - 36), 90))
    triangle55.add_vertex((47 + 2 * (98 - 47), 99.5))
    triangle55.add_vertex((51 + 2 * (98 - 51), 85))

    triangle6 = GPolygon()
    triangle6.add_vertex((19.7, 100))
    triangle6.add_vertex((47, 99.5))
    triangle6.add_vertex((47.5, 150))

    triangle66 = GPolygon()
    triangle66.add_vertex((19.7 + 2 * (98 - 19.7), 100))
    triangle66.add_vertex((47 + 2 * (98 - 47), 99.5))
    triangle66.add_vertex((47.5 + 2 * (98 - 47.5), 150))

    triangle7 = GPolygon()
    triangle7.add_vertex((51, 85))
    triangle7.add_vertex((47, 99.5))
    triangle7.add_vertex((76, 120))

    triangle77 = GPolygon()
    triangle77.add_vertex((51 + 2 * (98 - 51), 85))
    triangle77.add_vertex((47 + 2 * (98 - 47), 99.5))
    triangle77.add_vertex((76 + 2 * (98 - 76), 120))

    triangle8 = GPolygon()
    triangle8.add_vertex((47, 99.5))
    triangle8.add_vertex((47.5, 150))
    triangle8.add_vertex((76, 120))

    triangle88 = GPolygon()
    triangle88.add_vertex((47 + 2 * (98 - 47), 99.5))
    triangle88.add_vertex((47.5 + 2 * (98 - 47.5), 150))
    triangle88.add_vertex((76 + 2 * (98 - 76), 120))

    triangle9 = GPolygon()
    triangle9.add_vertex((19.7, 100))
    triangle9.add_vertex((47.5, 150))
    triangle9.add_vertex((40, 165))

    triangle99 = GPolygon()
    triangle99.add_vertex((19.7 + 2 * (98 - 19.7), 100))
    triangle99.add_vertex((47.5 + 2 * (98 - 47.5), 150))
    triangle99.add_vertex((40 + 2 * (98 - 40), 165))

    window.add(triangle1, 100, 30)
    window.add(triangle11, 100, 30)

    window.add(triangle2, 100, 30)
    window.add(triangle22, 100, 30)

    window.add(triangle3, 100, 30)
    window.add(triangle33, 100, 30)

    window.add(triangle4, 100, 30)
    window.add(triangle44, 100, 30)

    window.add(triangle5, 100, 30)
    window.add(triangle55, 100, 30)

    window.add(triangle6, 100, 30)
    window.add(triangle66, 100, 30)

    window.add(triangle7, 100, 30)
    window.add(triangle77, 100, 30)

    window.add(triangle8, 100, 30)
    window.add(triangle88, 100, 30)

    window.add(triangle9, 100, 30)
    window.add(triangle99, 100, 30)


def head():  # 15 parts
    # draw the left side first and then draw a reflection
    quad1 = GPolygon()
    quad1.add_vertex((40, 165))
    quad1.add_vertex((47.5, 150))
    quad1.add_vertex((48, 167))
    quad1.add_vertex((39.4, 189))

    # reflection
    quad1f = GPolygon()
    quad1f.add_vertex((40+2*(98-40), 165))
    quad1f.add_vertex((47.5+2*(98-47.5), 150))
    quad1f.add_vertex((48+2*(98-48), 167))
    quad1f.add_vertex((39.4+2*(98-39.4), 189))

    quad2 = GPolygon()
    quad2.add_vertex((39.4, 189))
    quad2.add_vertex((48, 167))
    quad2.add_vertex((50, 188))
    quad2.add_vertex((49, 210))

    quad22 = GPolygon()
    quad22.add_vertex((39.4 + 2 * (98 - 39.4), 189))
    quad22.add_vertex((48 + 2 * (98 - 48), 167))
    quad22.add_vertex((50 + 2 * (98 - 50), 188))
    quad22.add_vertex((49 + 2 * (98 - 49), 210))

    quad3 = GPolygon()
    quad3.add_vertex((49, 210))
    quad3.add_vertex((50, 188))
    quad3.add_vertex((82, 162))
    quad3.add_vertex((69, 184))

    quad33 = GPolygon()
    quad33.add_vertex((49 + 2 * (98 - 49), 210))
    quad33.add_vertex((50 + 2 * (98 - 50), 188))
    quad33.add_vertex((82 + 2 * (98 - 82), 162))
    quad33.add_vertex((69 + 2 * (98 - 69), 184))

    quad4 = GPolygon()
    quad4.add_vertex((49, 210))
    quad4.add_vertex((69, 184))
    quad4.add_vertex((69, 225))
    quad4.add_vertex((53, 222))

    quad44 = GPolygon()
    quad44.add_vertex((49 + 2 * (98 - 49), 210))
    quad44.add_vertex((69 + 2 * (98 - 69), 184))
    quad44.add_vertex((69 + 2 * (98 - 69), 225))
    quad44.add_vertex((53 + 2 * (98 - 53), 222))

    quad5 = GPolygon()
    quad5.add_vertex((69, 225))
    quad5.add_vertex((69, 184))
    quad5.add_vertex((98, 194))
    quad5.add_vertex((80, 218))

    quad55 = GPolygon()
    quad55.add_vertex((69 + 2 * (98 - 69), 225))
    quad55.add_vertex((69 + 2 * (98 - 69), 184))
    quad55.add_vertex((98 + 2 * (98 - 98), 194))
    quad55.add_vertex((80 + 2 * (98 - 80), 218))

    quad6 = GPolygon()
    quad6.add_vertex((98, 194))
    quad6.add_vertex((98, 218))
    quad6.add_vertex((80, 218))

    quad66 = GPolygon()
    quad66.add_vertex((98 + 2 * (98 - 98), 194))
    quad66.add_vertex((98 + 2 * (98 - 98), 218))
    quad66.add_vertex((80 + 2 * (98 - 80), 218))

    quad7 = GPolygon()
    quad7.add_vertex((98, 194))
    quad7.add_vertex((69, 184))
    quad7.add_vertex((84, 174))
    quad7.add_vertex((98, 188))

    quad77 = GPolygon()
    quad77.add_vertex((98 + 2 * (98 - 98), 194))
    quad77.add_vertex((69 + 2 * (98 - 69), 184))
    quad77.add_vertex((84 + 2 * (98 - 84), 174))
    quad77.add_vertex((98 + 2 * (98 - 98), 188))

    quad8 = GPolygon()
    quad8.add_vertex((69, 184))
    quad8.add_vertex((82, 162))
    quad8.add_vertex((88, 162))
    quad8.add_vertex((84, 174))

    quad88 = GPolygon()
    quad88.add_vertex((69 + 2 * (98 - 69), 184))
    quad88.add_vertex((82 + 2 * (98 - 82), 162))
    quad88.add_vertex((88 + 2 * (98 - 88), 162))
    quad88.add_vertex((84 + 2 * (98 - 84), 174))

    quad9 = GPolygon()
    quad9.add_vertex((48, 167))
    quad9.add_vertex((80, 145))
    quad9.add_vertex((82, 162))
    quad9.add_vertex((50, 188))

    quad99 = GPolygon()
    quad99.add_vertex((48 + 2 * (98 - 48), 167))
    quad99.add_vertex((80 + 2 * (98 - 80), 145))
    quad99.add_vertex((82 + 2 * (98 - 82), 162))
    quad99.add_vertex((50 + 2 * (98 - 50), 188))

    quad10 = GPolygon()
    quad10.add_vertex((47.5, 150))
    quad10.add_vertex((76, 120))
    quad10.add_vertex((80, 145))
    quad10.add_vertex((48, 167))

    quad101 = GPolygon()
    quad101.add_vertex((47.5 + 2 * (98 - 47.5), 150))
    quad101.add_vertex((76 + 2 * (98 - 76), 120))
    quad101.add_vertex((80 + 2 * (98 - 80), 145))
    quad101.add_vertex((48 + 2 * (98 - 48), 167))

    quad11 = GPolygon()
    quad11.add_vertex((76, 120))
    quad11.add_vertex((98, 118))
    quad11.add_vertex((80, 145))

    quad111 = GPolygon()
    quad111.add_vertex((76 + 2 * (98 - 76), 120))
    quad111.add_vertex((98 + 2 * (98 - 98), 118))
    quad111.add_vertex((80 + 2 * (98 - 80), 145))

    quad12 = GPolygon()
    quad12.add_vertex((82, 162))
    quad12.add_vertex((80, 145))
    quad12.add_vertex((98, 118))
    quad12.add_vertex((98, 152))

    quad121 = GPolygon()
    quad121.add_vertex((82 + 2 * (98 - 82), 162))
    quad121.add_vertex((80 + 2 * (98 - 80), 145))
    quad121.add_vertex((98 + 2 * (98 - 98), 118))
    quad121.add_vertex((98 + 2 * (98 - 98), 152))

    quad13 = GPolygon()
    quad13.add_vertex((82, 162))
    quad13.add_vertex((98, 152))
    quad13.add_vertex((98, 162))

    quad131 = GPolygon()
    quad131.add_vertex((82 + 2 * (98 - 82), 162))
    quad131.add_vertex((98, 152))
    quad131.add_vertex((98, 162))

    quad14 = GPolygon()
    quad14.add_vertex((84, 174))
    quad14.add_vertex((88, 162))
    quad14.add_vertex((98, 162))
    quad14.add_vertex((98, 178))

    quad141 = GPolygon()
    quad141.add_vertex((84 + 2 * (98 - 84), 174))
    quad141.add_vertex((88 + 2 * (98 - 84), 162))
    quad141.add_vertex((98, 162))
    quad141.add_vertex((98, 178))

    quad15 = GPolygon()
    quad15.add_vertex((84, 174))
    quad15.add_vertex((98, 178))
    quad15.add_vertex((98, 188))

    quad151 = GPolygon()
    quad151.add_vertex((84 + 2 * (98 - 84), 174))
    quad151.add_vertex((98, 178))
    quad151.add_vertex((98, 188))

    window.add(quad1, 100, 30)
    window.add(quad1f, 100, 30)

    window.add(quad2, 100, 30)
    window.add(quad22, 100, 30)

    window.add(quad3, 100, 30)
    window.add(quad33, 100, 30)

    window.add(quad4, 100, 30)
    window.add(quad44, 100, 30)

    window.add(quad5, 100, 30)
    window.add(quad55, 100, 30)

    window.add(quad6, 100, 30)
    window.add(quad66, 100, 30)

    window.add(quad7, 100, 30)
    window.add(quad77, 100, 30)

    window.add(quad8, 100, 30)
    window.add(quad88, 100, 30)

    window.add(quad9, 100, 30)
    window.add(quad99, 100, 30)

    window.add(quad10, 100, 30)
    window.add(quad101, 100, 30)

    window.add(quad11, 100, 30)
    window.add(quad111, 100, 30)

    window.add(quad12, 100, 30)
    window.add(quad121, 100, 30)

    window.add(quad13, 100, 30)
    window.add(quad131, 100, 30)

    window.add(quad14, 100, 30)
    window.add(quad141, 100, 30)

    window.add(quad15, 100, 30)
    window.add(quad151, 100, 30)


if __name__ == '__main__':
    main()
