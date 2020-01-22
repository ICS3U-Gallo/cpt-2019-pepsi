import arcade
import os

 
SPRITE_SCALING = 0.5
 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Raymond Game"
MOVEMENT_SPEED = 50

class Ball:

    def __init__(self, position_x, position_y, change_x, change_y, radius):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.player_color = arcade.color.AMETHYST

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius,self.player_color)

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius

class MyGame(arcade.Window):
   def __init__(self, width, height, title):
       super().__init__(width, height, title)
       self.drawer = 0
       self.wardrobe = 0
       self.bookshelves = 0
       self.door = 0
       self.bed = 0
       self.book_1 = 0
       self.book_2 = 0
       self.book_3 = 0
       self.endscreen = 0
       self.movement_tutorial = 0

       self.code = 0
       self.exit_key = 0
    
       arcade.set_background_color(arcade.color.BROWN)
       self.ball = Ball(400,300, 0, 0, 15)
  
   def on_draw(self):
       arcade.start_render()
       self.ball.draw()

       #door
       arcade.draw_rectangle_filled(35,560,60,80,arcade.color.AMAZON)
       arcade.draw_rectangle_filled(7,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(17,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(27,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(37,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(47,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(57,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(67,560,4,80,arcade.color.GRAY)
       arcade.draw_rectangle_filled(57,560,20,15,arcade.color.GRAY)
       arcade.draw_circle_filled(62,563,2,arcade.color.BLACK)
       arcade.draw_triangle_filled(62,562,60,559,64,559,arcade.color.BLACK)
       #bed
       arcade.draw_rectangle_filled (740,80,70,120,arcade.color.GRAY)       
       arcade.draw_rectangle_filled (740,120,60,30,arcade.color.WHITE)     
       arcade.draw_rectangle_filled (740,60,70,80,arcade.color.WHITE)
       #bookshelves
       arcade.draw_rectangle_filled (365,550,60,90,arcade.color.GRAY) 
       arcade.draw_rectangle_filled (365,570,50,30,arcade.color.BLACK)
       arcade.draw_rectangle_filled (365,530,50,30,arcade.color.BLACK)
       arcade.draw_rectangle_filled (345,567,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (353,567,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (361,567,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (369,567,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (377,567,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (385,567,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (345,527,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (353,527,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (361,527,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (369,527,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (377,527,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (385,527,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (435,550,60,90,arcade.color.GRAY)
       arcade.draw_rectangle_filled (435,570,50,30,arcade.color.BLACK)
       arcade.draw_rectangle_filled (435,530,50,30,arcade.color.BLACK)
       arcade.draw_rectangle_filled (415,567,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (423,567,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (431,567,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (439,567,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (447,567,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (455,567,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (415,527,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (423,527,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (431,527,6,24,arcade.color.BLUE)
       arcade.draw_rectangle_filled (439,527,6,24,arcade.color.RED)
       arcade.draw_rectangle_filled (447,527,6,24,arcade.color.ORANGE)
       arcade.draw_rectangle_filled (455,527,6,24,arcade.color.BLUE)
       #drawer
       arcade.draw_rectangle_filled (30,30,50,50,arcade.color.GRAY)
       arcade.draw_rectangle_filled (30,30,42,42,arcade.color.WHITE)
       #wardrobe
       arcade.draw_rectangle_filled (750,540,80,100,arcade.color.GRAY)
       arcade.draw_rectangle_filled (750,540,4,100,arcade.color.BLACK)
       arcade.draw_circle_filled (740,540,3,arcade.color.YELLOW) 
       arcade.draw_circle_filled (760,540,3,arcade.color.YELLOW)

       if self.ball.position_x < 115 and self.ball.position_y > 470:
           arcade.draw_text("Hold D to interact", 235, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("with Door", 235, 314, arcade.color.WHITE, font_size=18)

       if self.ball.position_x > 635 and self.ball.position_y < 210:
           arcade.draw_text("Hold E to interact", 235, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("with Bed", 235, 314, arcade.color.WHITE, font_size=18)
     
       if self.ball.position_x > 255 and self.ball.position_x < 535 and self.ball.position_y > 435:
           arcade.draw_text("Hold O to interact", 235, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("with Bookshelves", 235, 314, arcade.color.WHITE, font_size=18)

       if self.ball.position_x < 105 and self.ball.position_y < 105:
           arcade.draw_text("Hold R to interact", 235, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("with Drawer", 235, 314, arcade.color.WHITE, font_size=18)
           
       if self.ball.position_x > 660 and self.ball.position_y > 440:
           arcade.draw_text("Hold W to interact", 235, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("with Wardrobe", 235, 314, arcade.color.WHITE, font_size=18)
       
       if self.movement_tutorial == 0:
           arcade.draw_text("Use arrow keys to move", 235, 368, arcade.color.WHITE, font_size=18)
       
       if self.drawer == 1:
           if self.code == 1:
               arcade.draw_text("Congratulations!", 435, 338, arcade.color.WHITE, font_size=18)
               arcade.draw_text("You got a key", 435, 314, arcade.color.WHITE, font_size=18)
               self.exit_key = 1
           else:
               arcade.draw_text("It seems I need", 435, 338, arcade.color.WHITE, font_size=18)
               arcade.draw_text("a code to open this", 435, 314, arcade.color.WHITE, font_size=18)

       if self.bed == 1:
           arcade.draw_text("It's just a bed", 435, 338, arcade.color.WHITE, font_size=18)

       if self.wardrobe == 1:
           arcade.draw_text("There are many outfits here", 435, 338, arcade.color.WHITE, font_size=18)

       if self.bookshelves == 1:
           arcade.draw_text("There are many books in here", 435, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("which one should I read? A, B, C", 435, 314, arcade.color.WHITE, font_size=18)
      
       if self.book_1 == 1:
           arcade.draw_text("There is a key in the", 435, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("drawer... huh", 435, 314, arcade.color.WHITE, font_size=18) 
      
       if self.book_2 == 1:
           arcade.draw_text("Congratulations!", 435, 338, arcade.color.WHITE, font_size=18)
           arcade.draw_text("You got a code", 435, 314, arcade.color.WHITE, font_size=18)
           self.code = 1
      
       if self.book_3 == 1:
            arcade.draw_text("It's the Bible", 435, 338, arcade.color.WHITE, font_size=18)
       
       if self.door == 1:
           if self.exit_key == 1:
               self.endscreen = 1
           else:
               arcade.draw_text("It seems that I need", 435, 338, arcade.color.WHITE, font_size=18) 
               arcade.draw_text("a key to open this", 435, 314, arcade.color.WHITE, font_size=18)

       if self.endscreen == 1:
           arcade.draw_rectangle_filled(400,300,800,600,arcade.color.BLACK)
           arcade.draw_text("Congratulations! you beat the game", 235, 468, arcade.color.WHITE, font_size=18)
           #sword
           arcade.draw_rectangle_filled (290,190,20,180,arcade.color.WHITE_SMOKE)
           arcade.draw_rectangle_filled (270,190,20,180,arcade.color.GRAY)
           arcade.draw_triangle_filled (260,100,280,100,280,70,arcade.color.GRAY)
           arcade.draw_triangle_filled (300,100,280,100,280,70, arcade.color.WHITE)
           arcade.draw_rectangle_filled (280,184,4,196,arcade.color.BLACK)
           arcade.draw_rectangle_filled (280,300,40,40,arcade.color.PURPLE)
           arcade.draw_triangle_filled (280,265,270,280,290,280,arcade.color.GOLD)
           arcade.draw_rectangle_filled (240,290,50,20,arcade.color.PURPLE,30)
           arcade.draw_rectangle_filled (320,290,50,20,arcade.color.PURPLE,330)
           arcade.draw_rectangle_filled (220,283,50,2,arcade.color.BLACK,30)
           arcade.draw_rectangle_filled (220,275,59,2,arcade.color.BLACK,30)
           arcade.draw_rectangle_filled (340,283,50,2,arcade.color.BLACK,330)
           arcade.draw_rectangle_filled (340,275,59,2,arcade.color.BLACK,330)
           arcade.draw_rectangle_filled (280,340,15,50,arcade.color.PURPLE)
           arcade.draw_triangle_filled (260,320,280,320,280,340,arcade.color.PURPLE)
           arcade.draw_triangle_filled (265,320,280,320,280,365,arcade.color.PURPLE)
           arcade.draw_triangle_filled (300,320,280,320,280,340,arcade.color.PURPLE)
           arcade.draw_triangle_filled (295,320,280,320,280,365,arcade.color.PURPLE)
           arcade.draw_circle_filled (280,375,15,arcade.color.LIGHT_BROWN)

   def on_update(self, delta_time):

       self.ball.update()
     
   def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
            self.movement_tutorial = 1
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
            self.movement_tutorial = 1
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
            self.movement_tutorial = 1
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED
            self.movement_tutorial = 1
        if key == arcade.key.R:
            self.drawer = 1
        if key == arcade.key.W:
            self.wardrobe = 1
        if key == arcade.key.D:
            self.door = 1
        if key == arcade.key.O:
            self.bookshelves = 1
        if key == arcade.key.E:
            self.bed = 1
        if key == arcade.key.A:
            self.book_1 = 1
        if key == arcade.key.B:
            self.book_2 = 1
        if key == arcade.key.C:
            self.book_3 = 1

   def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0
        if key == arcade.key.R:
            self.drawer = 0
        if key == arcade.key.W:
            self.wardrobe = 0
        if key == arcade.key.D:
            self.door = 0
        if key == arcade.key.O:
            self.bookshelves = 0
        if key == arcade.key.E:
            self.bed = 0
        if key == arcade.key.A:
            self.book_1 = 0
        if key == arcade.key.B:
            self.book_2 = 0
        if key == arcade.key.C:
            self.book_3 = 0

def main():
   """ Main method """
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   arcade.run()
 
 
if __name__ == "__main__":
   main()
