import arcade

class myWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200, 100)
    
    def on_update(self, delta_time):
        print(delta_time)

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(100, 100, 50, arcade.color.RED)
        arcade.set_background_color(arcade.color.AMAZON)

        

myWindow(800, 600, 'Test Window')
arcade.run()