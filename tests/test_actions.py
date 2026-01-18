from controller import GameController
from entities import Enemy, Player, Room


def test_cannot_go_forward_if_enemy_alive(controller: GameController):
    controller.current_index = 1
    room = controller.dungeon[1]
    actions = controller._get_available_actions(room=room)

    assert actions == ["attack"]


def test_attack_kills_enemy(player: Player, enemy: Enemy):
    dungeon = [
        Room(room_type="St", description="start"),
        Room(room_type="E", description="enemy room", enemy=enemy),
    ]
    controller = GameController(player=player, dungeon=dungeon)
    controller.current_index = 1
    controller._attack(dungeon[1])

    assert not enemy.is_alive()


def test_exit_available_only_in_exit_room(
    player: Player, dungeon_with_exit: list[Room]
):
    controller = GameController(player, dungeon_with_exit)

    actions_start = controller._get_available_actions(room=dungeon_with_exit[0])
    actions_exit = controller._get_available_actions(room=dungeon_with_exit[1])

    assert "exit" not in actions_start
    assert "exit" in actions_exit


def test_actions_only_attack_if_enemy_alive(controller: GameController):
    controller.current_index = 1
    room = controller.dungeon[1]

    actions = controller._get_available_actions(room)

    assert actions == ["attack"]


def test_actions_after_enemy_dead(controller: GameController):
    room = controller.dungeon[1]
    room.enemy.hp = 0
    room.clear_if_enemy_dead()

    actions = controller._get_available_actions(room)

    assert "attack" not in actions
    assert "go_forward" in actions


def test_exit_only_in_exit_room(player: Player, dungeon_with_exit):
    controller = GameController(player, dungeon_with_exit)

    assert "exit" not in controller._get_available_actions(dungeon_with_exit[0])
    assert "exit" in controller._get_available_actions(dungeon_with_exit[1])
