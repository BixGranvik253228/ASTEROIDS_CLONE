import arcade
import math
from pathlib import Path

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.score_text = arcade.Text("Score: 0", 10, 10, arcade.color.WHITE, 14)
        self.window.background_color = arcade.color.BLACK

        # self properties

        self.ship_speed = 0.0
        self.ship_x = self.width / 2
        self.ship_y = self.height / 2
        self.thrust_mode = False
        self.rotate_speed = 360
        self.ship_acceleration = 10


        # ship_path = Path('../SPRITES/ship.png')
        # self.ship = arcade.Sprite("./ship.png")
        # self.ship = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png")
        # ship_path = str(Path(__file__).parent/'ship.png') # I don't understand this
        # ship_path = "ASTEROIDS_CLONE/SPRITES/ship_right.png"
        # self.ship = arcade.Sprite(ship_path)


        self.ship_new = arcade.load_texture(":resources:images/space_shooter/playerShip1_green.png")
        self.ship_new = self.ship_new.rotate_90()
        self.ship = arcade.Sprite(self.ship_new)


        self.sprites = arcade.SpriteList()
        self.sprites.append(self.ship)
        # self.sprites.append(self.ship_test)

        # self.ship_test.center_x = self.width / 2
        # self.ship_test.center_y = self.height / 2


    def setup(self):
        # self.ship properties
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
        self.ship.drag = 0.99
        
        # self.asteroids = arcade.SpriteList()
        # self.asteroids.append(self.big_asteroid)
        
        
        

    def on_draw(self):
        self.clear()

        # arcade.draw_triangle_outline(
        #     self.ship_x + math.cos(self.ship_angle) * 15,
        #     self.ship_y + math.sin(self.ship_angle) * 15,
        #     self.ship_x + math.cos(self.ship_angle + 140 / 180 * math.pi) * 15,
        #     self.ship_y + math.sin(self.ship_angle + 140 / 180 * math.pi) * 15,
        #     self.ship_x + math.cos(self.ship_angle - 140 / 180 * math.pi) * 15,
        #     self.ship_y + math.sin(self.ship_angle - 140 / 180 * math.pi) * 15,
        #     arcade.color.WHITE,
        #     2
        # )

        # self.ship.draw()
        self.sprites.draw()



    # def on_update(self, delta_time):
        # if self.thrust_mode:
        #     self.ship_speed += 500 * delta_time

        # self.ship_x += math.cos(self.ship_angle) * self.ship_speed * delta_time
        # self.ship_y += math.sin(self.ship_angle) * self.ship_speed * delta_time

        # diff_to_go_left = math.pi - self.ship_angle
        # diff_to_go_right = - self.ship_angle

        # if self.go_right:
        #     self.ship_angle -= self.rotate_speed * delta_time

        # if self.go_left:
        #     self.ship_angle += self.rotate_speed * delta_time

        # self.ship_speed *= 0.99

    def on_update(self, delta_time):
        if self.go_left:
            # self.ship.center_x -= self.ship.acceleration * delta_time
            # self.ship.turn_left(self.rotate_speed)
            self.ship.angle -= self.rotate_speed * delta_time
        if self.go_right:
            # self.ship.center_x += self.ship.acceleration * delta_time
            # self.ship.turn_right(self.rotate_speed)
            self.ship.angle += self.rotate_speed * delta_time

        if self.go_up:
            # self.ship.center_y += self.ship.acceleration * delta_time
            # self.ship.strafe(self.ship.speed)
            # self.ship.center_y += math.sin(math.radians(self.ship.angle)) * self.ship.speed * delta_time
            
            # self.ship.change_x += math.cos(math.radians(self.ship.angle)) * self.ship.speed * delta_time

        
            self.ship.change_x += math.cos(math.radians(self.ship.angle)) * self.ship.acceleration * delta_time
            self.ship.change_y -= math.sin(math.radians(self.ship.angle)) * self.ship.acceleration * delta_time

        if self.go_down:
            # self.ship.center_y -= self.ship.acceleration * delta_time
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


        # self.ship.speed *= 0.99
        # self.ship.change_x *= 0.99
        # self.ship.change_y *= 0.99
        self.ship.speed *= self.ship.drag
        self.sprites.update()
        # ASTEROIDS_CLONE/SPRITES/ship.png
        # /Users/uni/Documents/ADSAI_HUB/ASTEROIDS_CLONE/SPRITES/ship.png



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