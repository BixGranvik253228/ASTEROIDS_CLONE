import arcade
import math

class window(arcade.Window):
    # override initialize function
    def __init__(self, width, height, title):
        super().__init__(width, height, title, update_rate=1/60)
        self.set_location(200, 100)
        arcade.set_background_color(arcade.color.BLACK)

        # ship properties
        self.ship_angle = 0.0
        self.ship_speed = 0.0
        self.ship_x = self.width / 2
        self.ship_y = self.height / 2
        self.thrust_mode = False
        self.turn_right = False
        self.turn_left = False
        self.turn_speed = 4.0
        self.ship_acceleration = 1.0

    
    

    
    # override draw function
    def on_draw(self):
        self.clear()
        # arcade.draw_circle_filled(self.c_x, self.c_y, 50, arcade.color.WHITE, 0, 10)

        # ship hull
        arcade.draw_triangle_outline(
            self.ship_x + math.cos(self.ship_angle) * 15,
            self.ship_y + math.sin(self.ship_angle) * 15,
            self.ship_x + math.cos(self.ship_angle + 140 / 180 * math.pi) * 15,
            self.ship_y + math.sin(self.ship_angle + 140 / 180 * math.pi) * 15,
            self.ship_x + math.cos(self.ship_angle - 140 / 180 * math.pi) * 15,
            self.ship_y + math.sin(self.ship_angle - 140 / 180 * math.pi) * 15,
            arcade.color.WHITE,
            2
        )

    # def on_update(self, d):
        # self.c_x += self.x_speed * d
        # self.c_y += self.y_speed * d

        # if self.c_x > self.width or self.c_x < 0:
        #     self.x_speed *= -1
        # if self.c_y > self.height or self.c_y < 0:
        #     self.y_speed *= -1
        # pass

    # override update function
    def on_update(self, delta_time):
        # update ship speed
        if self.thrust_mode:
            self.ship_speed += 500 * delta_time

        
        # update ship position
        self.ship_x += math.cos(self.ship_angle) * self.ship_speed * delta_time
        self.ship_y += math.sin(self.ship_angle) * self.ship_speed * delta_time

        ## update ship angle
        # result will be positive value when angle upper 180 degree
        diff_to_left = math.pi - self.ship_angle
        # result will be positive value when angle lower 180 degree
        diff_to_right = - self.ship_angle

        # can make the following two into one functino?
        if self.turn_right:
            self.ship_angle -= self.turn_speed * delta_time

        if self.turn_left:
            self.ship_angle += self.turn_speed * delta_time

        # friction
        self.ship_speed *= 0.99
        
        # if self.turn_left:
        #     if diff_to_left > 0:
        #         self.ship_angle += 0.1 * delta_time
        #         diff_to_left -= 0.1 * delta_time
        #     elif diff_to_left < 0:
        #         self.ship_angle -= 0.1 * delta_time
        #         diff_to_left += 0.1 * delta_time
                
            


    # override key press function
    def on_key_press(self, key, modifiers):
        
        if key == arcade.key.SPACE:
            print("Fire")
        if key == arcade.key.A:
            # print("Rotate left")
            self.turn_left = True
            
        if key == arcade.key.D:
            # print("Rotate right")
            self.turn_right = True
            
        if key == arcade.key.W:
            # print("Thrust")
            self.thrust_mode = True
    
    # override key release function
    def on_key_release(self, key, modifiers):
        if key == arcade.key.W:
            self.thrust_mode = False
        if key == arcade.key.A:
            self.turn_left = False
        if key == arcade.key.D:
            self.turn_right = False
        


mainWindow = window(800, 600, 'Asteroids Clone')
arcade.run()