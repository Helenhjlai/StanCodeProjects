"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics1 import BreakoutGraphics
import random

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 32		# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add the animation loop here!
    while True:
        if lives > 0:
            if graphics.start_game:
                while True:
                    dx = graphics.get_dx()
                    dy = graphics.get_dy()

                    # win
                    if graphics.brick_remove == graphics.brick_cols * graphics.brick_rows:
                        graphics.win_word()
                        break

                    graphics.ball.move(dx, dy)
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        graphics.set_dx()
                    if graphics.ball.y <= 0 and dy < 0:
                        graphics.set_dy()
                    # if graphics.ball.y + graphics.ball.height >= graphics.window.height and dy > 0:
                    #     graphics.set_dy()

                    # detect collision

                    graphics.collision()
                    graphics.bonus_move()

                    # game reset
                    situ2 = graphics.ball.y + graphics.ball.height < graphics.paddle.y + (2/3) * graphics.paddle.height
                    if not situ2:
                        graphics.ball.x = graphics.start_x
                        graphics.ball.y = graphics.start_y
                        graphics.window.add(graphics.ball)
                        graphics.start_game = False
                        lives -= 1
                        break
                    pause(FRAME_RATE)
        else:  # game over
            graphics.game_over()
            break

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
