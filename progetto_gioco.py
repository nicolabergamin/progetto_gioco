import arcade
import random
import math

WIDTH = 800
HEIGHT = 600
TITLE = "progetto_gioco"

class progetto_gioco(arcade.Window):
    def __init__(self):
        super().__init__(WIDTH, HEIGHT, TITLE)

        self.player = None
        self.enemy = None
        self.bullet = None
        self.lista_player = arcade.SpriteList()
        self.lista_enemy = arcade.SpriteList()
        self.lista_bullet = arcade.SpriteList()

        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.mute = False
        self.velocita = 4
        self.setup()

    def setup(self):
        self.player = arcade.Sprite("./assets/main_character.png")
        self.player.center_x = 400
        self.player.center_y = 300
        self.player.scale = 1.0
        self.lista_player.append(self.player)

    def on_draw(self):
        self.clear()
        self.lista_player.draw()

    def on_update(self, delta_time):
        change_x = 0
        change_y = 0
        
        if self.up_pressed:
            change_y += self.velocita
        if self.down_pressed:
            change_y -= self.velocita
        if self.left_pressed:
            change_x -= self.velocita
        if self.right_pressed:
            change_x += self.velocita
        
        self.player.center_x += change_x
        self.player.center_y += change_y

        if change_x < 0:
            self.player.scale = (-1, 1)
        if change_x > 0:
            self.player.scale = (1, 1)

        if self.player.center_x < 0:
            self.player.center_x = 0
        elif self.player.center_x > WIDTH:
            self.player.center_x = WIDTH
        
        if self.player.center_y < 0:
            self.player.center_y = 0
        elif self.player.center_y > HEIGHT:
            self.player.center_y = HEIGHT


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.D:
            self.right_pressed = True
    
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.D:
            self.right_pressed = False


def main():
    game = progetto_gioco()
    arcade.run()

if __name__ == "__main__":
    main()