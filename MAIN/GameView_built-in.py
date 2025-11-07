import arcade
import math
from pathlib import Path
import random

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
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.go_up = False
        if key == arcade.key.S:
            self.go_down = False
        if key == arcade.key.A:
            self.go_left = False
        if key == arcade.key.D:
            self.go_right = False
        
def main():
    main_window  = arcade.Window(800, 600, 'Asteroids Clone', update_rate=1/60)
    # self.set_location(200, 100)
    game_view = GameView()
    main_window.show_view(game_view)
    game_view.setup()
    arcade.run()

if __name__ == "__main__":
    main()