import arcade
import random

WIDTH = 640
HEIGHT = 480

x = 50
x_speed = 25
y = 240
y_speed = 25
key = arcade.Sprite(":resources:images/items/keyBlue.png", center_x=x, center_y=y, scale=0.2)
window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
score = 0


def setup():
    arcade.schedule(update, 1 / 60)
    arcade.run()


def update(delta_time):
    global x, x_speed, key, y, y_speed
    key.update()

    if key.center_x <= 15:
        x_speed = random.randint(15, 25)

    elif key.center_x >= (WIDTH-15):
        x_speed = random.randint(-25, -10)
    key.center_x += x_speed

    if key.center_y <= 15:
        y_speed = random.randint(15, 25)
    elif key.center_y >= (HEIGHT - 15):
        y_speed = random.randint(-25, -10)
    key.center_y += y_speed



@window.event
def on_draw():
    arcade.start_render()
    # Draw in here...
    key.draw()
    arcade.draw_text(f"Score {score}", WIDTH - 80, HEIGHT - 40, arcade.color.WHITE, 14)


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    global score
    if button == arcade.MOUSE_BUTTON_LEFT:
        if key.center_x - 50 <= x <= key.center_x + 50:
            if key.center_y + 50 >= y >= key.center_y - 50:
                score += 1
                if score == 1: 
                    print("You have successfully made your way through these trecherous levels and now you can rest till Zelda needs you again.")
                if score == 20:
                    print("Thank you for playing and thank you for teaching us")
if __name__ == '__main__':
    setup()
