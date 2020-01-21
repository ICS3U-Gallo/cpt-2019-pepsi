import arcade
import math
import os
from arcade.draw_commands import Texture

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "The Legend of Link, Chrisaanth"
BULLET_SPEED = 4
MOVEMENT_SPEED = 5

EXPLOSION_TEXTURE_COUNT = 60

class Explosion(arcade.Sprite):

    def __init__(self, texture_list):
        super().__init__()

        self.current_texture = 0
        self.textures = texture_list

    def update(self):

        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()

class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.color.AMAZON)

        self.explosions_list = None

        self.explosion_texture_list = []

        columns = 16
        count = 60
        sprite_width = 256
        sprite_height = 256
        file_name = ":resources:images/spritesheets/explosion.png"

        self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height, columns, count)

        self.frame_count = 0

        self.enemy_list = None
        self.bullet_list = None
        self.player_list = None
        self.player = None
        self.player_bullets = None
        
    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.explosions_list = arcade.SpriteList()
        self.player_bullets = arcade.SpriteList()

        # Add player ship
        self.player = arcade.Sprite(":resources:images/animated_characters/female_adventurer/femaleAdventurer_idle.png", 0.5)
        self.player_list.append(self.player)

        # Add top-left enemy 
        enemy = arcade.Sprite(":resources:images/alien/alienBlue_front.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

        # Add top-right enemy 
        enemy = arcade.Sprite(":resources:images/alien/alienBlue_front.png", 0.5)
        enemy.center_x = SCREEN_WIDTH - 120   
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)
        # Add top-middle enemy 
        enemy = arcade.Sprite(":resources:images/alien/alienBlue_front.png",0.5)
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180
        self.enemy_list.append(enemy)

    def on_draw(self):

        arcade.start_render()

        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()
        self.explosions_list.draw()
        self.player_bullets.draw()

    def on_mouse_press(self, x, y, button, modifiers):

        bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        start_x = self.player.center_x
        start_y = self.player.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        dest_x = x
        dest_y = y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        bullet.angle = math.degrees(angle)
        print(f"Bullet angle: {bullet.angle:.2f}")

        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        self.player_bullets.append(bullet)

    def on_update(self, delta_time):

        self.frame_count += 1

        for enemy in self.enemy_list:

            start_x = enemy.center_x
            start_y = enemy.center_y

            dest_x = self.player.center_x
            dest_y = self.player.center_y

            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            enemy.angle = math.degrees(angle)-90

            if self.frame_count % 60 == 0:
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                bullet.center_x = start_x
                bullet.center_y = start_y

                bullet.angle = math.degrees(angle)

                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.bullet_list.append(bullet)

        for bullet in self.bullet_list:
            hit_list = arcade.check_for_collision_with_list(self.player, self.bullet_list)

            if len(hit_list) > 0:

                explosion = Explosion(self.explosion_texture_list)

                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y

                explosion.update()

                self.explosions_list.append(explosion)

                bullet.remove_from_sprite_lists()
                self.player.remove_from_sprite_lists()
                self.player_list.remove(self.player)


        for bullet in self.player_bullets:
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)

            if len(hit_list) > 0:

                explosion = Explosion(self.explosion_texture_list)

                explosion.center_x = hit_list[0].center_x
                explosion.center_y = hit_list[0].center_y

                explosion.update()

                self.explosions_list.append(explosion)

                bullet.remove_from_sprite_lists()
                self.enemy_list[0].remove_from_sprite_lists()

            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()
        self.player.update()
        self.explosions_list.update()
        self.player_bullets.update()


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
