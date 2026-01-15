"""Фикстуры для автотестов"""

import pytest

from controller import GameController
from dungeon import create_dungeon
from entities import Armor, Enemy, Player, Room, Weapon


@pytest.fixture
def simple_layout() -> list[str]:
    return ["St", "E", " ", "Ex"]


@pytest.fixture
def dungeon(simple_layout: list[str]) -> list[Room]:
    return create_dungeon(simple_layout)


@pytest.fixture
def player() -> Player:
    """Тестовый игрок."""
    return Player(
        name="Test",
        hp=10,
        description="Test player",
        weapon=Weapon("Stick", 1, 100),
        armor=Armor("Cloth", 0),
    )


@pytest.fixture
def enemy() -> Enemy:
    """Тестовый враг."""
    return Enemy(
        name="Enemy",
        hp=5,
        description="Enemy",
        death_description="Dead",
        weapon=Weapon("Stick", 1, 100),
        armor=Armor("None", 0),
    )


@pytest.fixture
def dungeon_with_enemy(enemy: Enemy) -> list[Room]:
    """Подземелье с врагом."""
    return [
        Room("St", "start"),
        Room("E", "enemy room", enemy=enemy),
        Room("Ex", "exit"),
    ]


@pytest.fixture
def dungeon_with_exit() -> list[Room]:
    """Подземелье с выходом."""
    return [
        Room("St", "start"),
        Room("Ex", "exit"),
    ]


@pytest.fixture
def controller(player: Player, dungeon_with_enemy: list[Room]) -> GameController:
    """Контроллер с врагом."""
    return GameController(player, dungeon_with_enemy)