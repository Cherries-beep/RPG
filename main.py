"""Точка входа в консольную игру"""

from controller import GameController
from dungeon import create_dungeon, create_player

if __name__ == "__main__":
    map_layout = ["St", "E", " ", "E", "Ex"]

    player = create_player()
    dungeon = create_dungeon(map_layout)

    game = GameController(player, dungeon)
    game.run()