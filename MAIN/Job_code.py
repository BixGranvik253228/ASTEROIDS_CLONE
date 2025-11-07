import arcade
import math
import pathlib as path

screenSize = arcade.get_display_size()

class StartWindow(arcade.View):
    def __init__(self):
        super().__init__()
        self.window.background_color = arcade.color.BLACK


        self.title_name = arcade.Text(
            text="ASTEROIDS",
            x=800 / 2,
            y=350,
            color=arcade.color.WHITE,
            font_size=40, width= 300,
            anchor_x="center", 
            anchor_y="center"
        )

        self.start_button = arcade.Text(
            text="Press SPACE to play",
            x=800 / 2,
            y=290,
            color=arcade.color.WHITE, 
            font_size=13,
            anchor_x="center", 
            anchor_y="center"
        )

        
        self.game_startable = True      
            

    def on_draw(self):
        self.clear()
        self.title_name.draw()
        self.start_button.draw()
    
    def on_key_press(self, key, modifiers):
        if key == arcade.key.P:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.window.background_color = arcade.color.AMAZON
    
    def on_draw(self):
        self.clear()


def main():
    main_window = arcade.Window(800, 600, "Asteroids Clone")
    start_view = StartWindow()
    main_window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()
