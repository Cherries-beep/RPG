from controller import GameController
from entities import Room


def test_cannot_go_forward_if_enemy_alive(controller):
    controller.current_index = 1
    room = controller.dungeon[1]
    actions = controller._get_available_actions(room=room)

    assert actions == ["attack"]


def test_attack_kills_enemy(player, enemy):
    dungeon = [
        Room("St", "start"),
        Room("E", "enemy room", enemy=enemy),
    ]
    controller = GameController(player=player, dungeon=dungeon)
    controller.current_index = 1
    controller._attack(dungeon[1])

    assert not enemy.is_alive()


def test_exit_available_only_in_exit_room(player, dungeon_with_exit):
    controller = GameController(player, dungeon_with_exit)

    actions_start = controller._get_available_actions(room=dungeon_with_exit[0])
    actions_exit = controller._get_available_actions(room=dungeon_with_exit[1])

    assert "exit" not in actions_start
    assert "exit" in actions_exit
