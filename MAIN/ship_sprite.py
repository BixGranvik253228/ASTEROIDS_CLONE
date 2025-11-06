import arcade
import math
from pathlib import Path

class window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=1/60)
        self.set_location(200, 100)
        arcade.set_background_color(arcade.color.BLACK)

        # self properties
        self.ship_angle = 0.0
        self.ship_speed = 0.0
        self.ship_x = self.width / 2
        self.ship_y = self.height / 2
        self.thrust_mode = False
        self.go_right = False
        self.go_left = False
        self.rotate_speed = 4
        self.ship_acceleration = 1.1

        # ship_path = Path('../SPRITES/ship.png')
        # self.ship = arcade.Sprite("./ship.png")
        # self.ship_test = arcade.Sprite(":resources:images/space_shooter/playerShip1_green.png")
        ship_path = str(Path(__file__).parent/'ship.png') # I don't understand this
        self.ship = arcade.Sprite(ship_path)


        self.sprites = arcade.SpriteList()
        self.sprites.append(self.ship)
        # self.sprites.append(self.ship_test)

        # self.ship_test.center_x = self.width / 2
        # self.ship_test.center_y = self.height / 2

        # self.ship properties
        self.ship.center_x = self.width / 2
        self.ship.center_y = self.height / 2
        self.ship.angle = 0
        self.ship.speed = 10
        self.ship.acceleration = 100
        self.ship.go_right = False
        self.ship.go_left = False
        self.ship.go_up = False
        self.ship.go_down = False

        
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
        if self.go_left == True:
            # self.ship.center_x -= self.ship.acceleration * delta_time
            self.ship.turn_left(self.rotate_speed)
        if self.go_right == True:
            # self.ship.center_x += self.ship.acceleration * delta_time
            self.ship.turn_right(self.rotate_speed)
        if self.ship.go_up == True:
            # self.ship.center_y += self.ship.acceleration * delta_time
            self.ship.strafe(self.ship.speed)
        if self.ship.go_down == True:
            # self.ship.center_y -= self.ship.acceleration * delta_time
            pass
        
        self.sprites.update()
        


    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            print("Fire")

        if key == arcade.key.A:
            self.go_left = True
            
        if key == arcade.key.D:
            self.go_right = True
        
        if key == arcade.key.W:
            self.ship.go_up = True
            
        
        if key == arcade.key.S:
            self.ship.go_down = True
    
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.ship.go_up = False
        
        if key == arcade.key.S:
            self.ship.go_down = False

        if key == arcade.key.A:
            self.go_left = False
        if key == arcade.key.D:
            self.go_right = False
        


mainWindow = window(800, 600, 'Asteroids Clone')
arcade.run()