"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, dx=0, dy=0, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_width = brick_width

        # brick remove
        self.brick_remove = 0

        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-self.paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'
        self.window.add(self.ball, x=(self.window.width-self.ball.x)/2, y=(self.window.height-self.ball.y)/2)
        self.start_x = self.ball.x
        self.start_y = self.ball.y

        # Default initial velocity for the ball
        self.__dx = dx
        self.__dy = dy

        # Default obj x and obj y
        self.obj_x = 0
        self.obj_y = 0

        # Draw bricks
        color = ['red', 'orange', 'yellow', 'green', 'blue']
        if brick_rows % 2 != 0:
            runs = brick_rows // 2 + 1
        else:
            runs = brick_rows // 2
        for i in range(runs):
            for k in range(2):
                brick_color = color[i % 5]
                for j in range(brick_cols):
                    bricks = GRect(brick_width, brick_height)
                    bricks.filled = True
                    bricks.fill_color = brick_color
                    bricks.color = brick_color
                    self.window.add(bricks, x=j*(brick_width + brick_spacing),
                                    y=brick_offset + (2*i+k) * (brick_height + brick_spacing))
                if runs != brick_rows // 2:
                    if i == runs - 1:
                        break

        # Create bonus
        red_rect = GRect(15, 15)
        red_rect.filled = True
        red_rect.fill_color = 'red'
        red_rect.color = 'red'

        yellow_rect = GRect(15, 15)
        yellow_rect.filled = True
        yellow_rect.fill_color = 'yellow'
        yellow_rect.color = 'yellow'

        blue_rect = GRect(15, 15)
        blue_rect.filled = True
        blue_rect.fill_color = 'blue'
        blue_rect.color = 'blue'

        black_rect = GRect(15, 15)
        black_rect.filled = True
        black_rect.fill_color = 'black'
        black_rect.color = 'black'

        self.bonus_lst = [red_rect, yellow_rect, black_rect, blue_rect]
        self.bonus = self.bonus_lst[0]

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)

        # Initial game
        self.start_game = False
        onmouseclicked(self.start)

    def paddle_move(self, event):
        if event.x + (self.paddle.width/2) > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x - self.paddle.width/2 <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - (self.paddle.width/2)
        self.paddle.y = self.window.height - self.paddle_offset

    def start(self, _):
        self.start_game = True
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

    # get ball velocity
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx
        # return self.__dx

    def set_dy(self):
        self.__dy = -self.__dy
        # return self.__dy

    def win_word(self):
        win_word = GLabel('You Win!')
        self.window.add(win_word, x=(self.window.width-win_word.width)/2, y=(self.window.height-win_word.height)/2)

    def game_over(self):
        self.window.clear()
        lose_word = GLabel('Game Over You Loser!')
        self.window.add(lose_word, x=(self.window.width-lose_word.width)/2, y=(self.window.height-lose_word.height)/2)

    def choose_bonus(self):
        return self.bonus_lst[random.randint(0, 3)]

    def bonus_move(self):
        self.bonus.move(0, 1)

    def collision(self):
        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x + j * self.ball.width,
                                                self.ball.y + i * self.ball.height)

                if obj:
                    if obj == self.paddle:
                        if self.__dy > 0:
                            if self.__dx > 0:
                                if self.ball.x + self.ball.width <= self.paddle.x + self.paddle.width / 2:
                                    self.set_dx()
                            self.set_dy()
                    else:
                        if obj.width == BRICK_WIDTH:
                            self.obj_x = obj.x
                            self.obj_y = obj.y
                            self.set_dy()
                            self.brick_remove += 1
                            self.window.remove(obj)
                            # if self.brick_remove > 10:
                            #     r_n = random.randint(1, 5)
                            #     if r_n == 1:
                            #         self.bonus = self.choose_bonus()
                            #         self.window.add(self.bonus, x=self.obj_x + self.brick_width/2,
                            #                         y=self.obj_y)
                    break
