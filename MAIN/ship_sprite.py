import arcade
import math
from pathlib import Path

class window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=1/60)
        self.set_location(200, 100)
        arcade.set_background_color(arcade.color.BLACK)

        self.ship_angle = 0.0
        self.ship_speed = 0.0
        self.ship_x = self.width / 2
        self.ship_y = self.height / 2
        self.thrust_mode = False
        self.turn_right = False
        self.turn_left = False
        self.turn_speed = 4.0
        self.ship_acceleration = 1.0

        # ship_path = Path('../SPRITES/ship.png')
        # self.ship = arcade.Sprite("./ship.png")
        # self.ship_test = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png")
        ship_path = (Path(__file__).parent/'ship.png').resolve() # I don't understand this
        self.ship = arcade.Sprite(str(ship_path))

        self.ship.center_x = self.ship_x
        self.ship.center_y = self.ship_y
        self.ship.angle = self.ship_angle

        self.sprites = arcade.SpriteList()
        self.sprites.append(self.ship)
        
        
        

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

        # diff_to_left = math.pi - self.ship_angle
        # diff_to_right = - self.ship_angle

        # if self.turn_right:
        #     self.ship_angle -= self.turn_speed * delta_time

        # if self.turn_left:
        #     self.ship_angle += self.turn_speed * delta_time

        # self.ship_speed *= 0.99



    # def on_key_press(self, key, modifiers):
    #     if key == arcade.key.SPACE:
    #         print("Fire")

    #     if key == arcade.key.A:
    #         self.turn_left = True
            
    #     if key == arcade.key.D:
    #         self.turn_right = True
            
    #     if key == arcade.key.W:
    #         self.thrust_mode = True
    
    # def on_key_release(self, key, modifiers):
    #     if key == arcade.key.W:
    #         self.thrust_mode = False
    #     if key == arcade.key.A:
    #         self.turn_left = False
    #     if key == arcade.key.D:
    #         self.turn_right = False
        


mainWindow = window(800, 600, 'Asteroids Clone')
arcade.run()