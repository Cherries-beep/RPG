from dungeon import create_dungeon, create_player
from entities import Room
from typing import List

def test_create_player():
    player = create_player()

    assert player.name
    assert player.hp == 10
    assert player.weapon is not None
    assert player.armor is not None


def test_create_dungeon_rooms_count(dungeon: list[Room], simple_layout: list[str]):
    assert len(dungeon) == len(simple_layout)
    assert all(isinstance(room, Room) for room in dungeon)


def test_dungeon_has_start_and_exit(dungeon: list[Room]):
    room_types = [room.room_type for room in dungeon]

    assert "St" in room_types
    assert "Ex" in room_types


def test_enemy_created_in_enemy_room():
    layout = ["E"]
    dungeon = create_dungeon(layout)
    room = dungeon[0]

    assert room.room_type == "E"
    assert room.enemy is not None
    assert room.enemy.hp > 0
