import arcade

screenSize = arcade.get_display_size()

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        x = int((screenSize[0] / 2) - (width / 2))
        y = int((screenSize[1] / 2) - (height / 2))
        self.set_location(x, y)
        
        

    def on_update(self, delta_time):
        print('')        
    
    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.BLACK)
        


GameWindow(800, 600, 'Test Window')
arcade.run()
