import arcade
import math
import pathlib as path
import random

screenSize = arcade.get_display_size()
arcade.load_font(':resources:/fonts/ttf/Kenney/Kenney_Pixel_Square.ttf')
GameScore = 0

class StartWindow(arcade.View):
    def __init__(self):
        super().__init__()
        self.window.background_color = arcade.color.BLACK


        self.title_name = arcade.Text(
            text="ASTEROIDS",
            x=800 / 2,
            y=350,
            color=arcade.color.WHITE,
            font_size=40, font_name= 'Kenney Pixel Square',
            anchor_x="center", 
            anchor_y="center"
        )

        self.start_button = arcade.Text(
            text="Press 'P' to play",
            x=800 / 2,
            y=290,
            color=arcade.color.WHITE, 
            font_size=13, font_name= 'Kenney Pixel Square',
            anchor_x="center", 
            anchor_y="center"
        )

        
        self.game_startable = True      
            

    def on_draw(self):
        self.window.clear(arcade.color.BLACK)
        self.title_name.draw()
        self.start_button.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.P:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
    
class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.score_text = arcade.Text("Score: 0", 10, 10, arcade.color.WHITE, 14)
        self.window.background_color = arcade.color.BLACK
        self.ship_new = arcade.load_texture(":resources:images/space_shooter/playerShip1_green.png")
        self.ship_new = self.ship_new.rotate_90()
        self.ship = arcade.Sprite(self.ship_new)
        self.sprites = arcade.SpriteList()
        self.sprites.append(self.ship)

    def setup(self):
        self.ship.center_x = self.width / 2
        self.ship.center_y = self.height / 2
        self.ship.angle = 0
        self.ship.speed = 10
        self.ship.acceleration = 5
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False
        self.ship.change_x = 0
        self.ship.change_y = 0
        self.ship.scale = (0.5, 0.5)
        self.ship.drag = 0.95
        self.ship.rotate_speed = 360
        
        
    def asteroids_func(self):
        self.as_angle = random.randint(0, 360)

        self.big_as = arcade.Sprite(":resources:/images/space_shooter/meteorGrey_big1.png")
        self.asteroids = arcade.SpriteList()
        self.asteroids.append(self.big_as)

    def bullets_func(self):
        pass

    def on_draw(self):
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time):
        if self.go_left:
            self.ship.angle -= self.ship.rotate_speed * delta_time
        if self.go_right:
            self.ship.angle += self.ship.rotate_speed * delta_time
        if self.go_up:
            self.ship.change_x += math.cos(math.radians(self.ship.angle)) * self.ship.acceleration * delta_time
            self.ship.change_y -= math.sin(math.radians(self.ship.angle)) * self.ship.acceleration * delta_time
        if self.go_down:
            pass

        # screen wrap
        if self.ship.center_x > self.width:
            self.ship.center_x = 0
        if self.ship.center_x < 0:
            self.ship.center_x = self.width
        if self.ship.center_y > self.height:
            self.ship.center_y = 0
        if self.ship.center_y < 0:
            self.ship.center_y = self.height

        self.ship.speed *= self.ship.drag
        self.sprites.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            print("Fire")
        if key == arcade.key.A:
            self.go_left = True
        if key == arcade.key.D:
            self.go_right = True
        if key == arcade.key.W:
            self.go_up = True
        if key == arcade.key.S:
            self.go_down = True
        
        if key == arcade.key.L:
            game_view = DeathView()
            game_view.setup()
            self.window.show_view(game_view)
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.go_up = False
        if key == arcade.key.S:
            self.go_down = False
        if key == arcade.key.A:
            self.go_left = False
        if key == arcade.key.D:
            self.go_right = False
        
class DeathView(arcade.View):
    def __init__(self):
        super().__init__()

        self.GameOver = arcade.Text(
            text= "Game Over",
            x = 800 / 2,
            y = 350,
            color=arcade.color.WHITE,
            font_size=40, font_name= 'Kenney Pixel Square',
            anchor_x = "center",
            anchor_y = "center"
        )

        self.GameScore = arcade.Text(
            text= f'Your score: {GameScore}',
            x = 800 / 2,
            y = 290,
            color=arcade.color.WHITE, 
            font_size=20, font_name= 'Kenney Pixel Square',
            anchor_x="center", 
            anchor_y="center"
        )

        self.restartButton = arcade.Text(
            text= "Try Again",
            x = 800 / 2,
            y = 150,
            color=arcade.color.WHITE, 
            font_size=20, font_name= 'Kenney Pixel Square',
            anchor_x="center", 
            anchor_y="center"
        )

    def on_draw(self):
        self.window.clear(arcade.color.BLACK)
        self.GameOver.draw()
        self.GameScore.draw()
        self.restartButton.draw()

        arcade.draw_lbwh_rectangle_outline(
            self.restartButton.x - self.restartButton.content_width / 2,
            self.restartButton.y - self.restartButton.content_height / 2,
            self.restartButton.content_width,
            self.restartButton.content_height,
            arcade.color.RED
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.R:
            game_view = StartWindow()
            game_view.setup()
            self.window.show_view(game_view)

    def setup(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

def main():
    main_window = arcade.Window(800, 600, "Asteroids Clone")
    start_view = StartWindow()
    main_window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()