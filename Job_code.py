import arcade

screenSize = arcade.get_display_size()

class GameWindow(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.set_location(((screenSize[0] / 2) - (width / 2)), ((screenSize[1] / 2) - (height / 2)))

    def on_update(self, delta_time):
        print(delta_time)
    
    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.AMAZON)

GameWindow(800, 600, 'Test Window')
arcade.run()
