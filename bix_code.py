import arcade

class myWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(200, 0)
    
    def on_update(self, delta_time):
        print(delta_time)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(100, 100, 50, arcade.color.AERO_BLUE)

        

myWindow(1000, 900, 'Test Window')
arcade.run()
