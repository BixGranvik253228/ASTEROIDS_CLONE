import arcade

screenSize = arcade.get_display_size()

class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        x = int((screenSize[0] / 2) - (width / 2))
        y = int((screenSize[1] / 2) - (height / 2))
        self.set_location(x, y)
        
        
        xText = x + (width / 2)
        yText = y + (height / 2)
        self.start_button = arcade.Text(
            "PLAY",
            xText, yText,
            arcade.color.WHITE,
            20, 
            anchor_x="center", anchor_y="center"
        )

    def on_update(self, delta_time):
        print('')        
    
    def on_draw(self):
        self.clear()
        arcade.set_background_color(arcade.color.BLACK)
        self.start_button.draw()
        


GameWindow(800, 600, 'Test Window')
arcade.run()
