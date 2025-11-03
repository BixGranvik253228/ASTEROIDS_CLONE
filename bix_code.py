import arcade

class window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200, 100)
        arcade.set_background_color(arcade.color.BLACK)
        self.c_x = 100
        self.c_y = 100
        self.x_speed = 300
        self.y_speed = 200
    
    

    

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(self.c_x, self.c_y, 50, arcade.color.RED, 0, 10)

    def on_update(self, d):
        self.c_x += self.x_speed * d
        self.c_y += self.y_speed * d

        if self.c_x > self.width or self.c_x < 0:
            self.x_speed *= -1
        if self.c_y > self.height or self.c_y < 0:
            self.y_speed *= -1
        


mainWindow = window(800, 600, 'Asteroids Clone')
arcade.run()