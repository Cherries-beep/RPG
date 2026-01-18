"""Модуль генерации игровых данных. Отвечает за создание игрока, врагов и подземелья"""

import json
import random
from pathlib import Path
from typing import Any, Dict, List

from entities import Armor, Enemy, Player, Room, Weapon

DATA_DIR = Path(__file__).parent / "data"


def load_json(filename: str) -> Dict[str, Any]:
    """Загрузить данные из json-файла

    Args:
        filename: Имя файла.

    Returns:
        Содержимое json-файла
    """
    with open(DATA_DIR / filename, encoding="utf-8") as file:

        return json.load(file)


def create_player() -> Player:
    """Создать игрока на основе данных из player.json

    Returns:
        Player: Экземпляр игрока.
    """
    data = load_json("player.json")
    weapon_data = data["weapon"]
    armor_data = data["armor"]

    return Player(
        name=random.choice(data["names"]),
        hp=data["hp"],
        description=random.choice(data["descriptions"]),
        weapon=Weapon(
            name=weapon_data["name"],
            damage=weapon_data["damage"],
            hit_chance=weapon_data["hit_chance"],
        ),
        armor=Armor(
            name=armor_data["name"],
            defense=armor_data["defense"],
        ),
    )


def create_enemy() -> Enemy:
    """Создать случайного противника

    Returns:
        Enemy: Экземпляр противника.
    """
    data = load_json("enemies.json")
    enemy_data = random.choice(data["enemies"])

    return Enemy(
        name=enemy_data["name"],
        hp=enemy_data["hp"],
        description=enemy_data["description"],
        death_description=enemy_data["death_description"],
        weapon=Weapon(**enemy_data["weapon"]),
        armor=Armor(**enemy_data["armor"]),
    )


def create_dungeon(map_layout: list[str]) -> list[Room]:
    """Создать подземелье по заданной карте

    Args:
        map_layout: Список типов комнат.

    Returns:
        list: Список комнат подземелья.
    """
    descriptions = load_json("rooms.json")["room_descriptions"]

    dungeon: list[Room] = []

    for room_type in map_layout:
        enemy = create_enemy() if room_type == "E" else None

        if enemy is None:
            is_cleared = True
        else:
            is_cleared = False

        dungeon.append(
            Room(
                room_type=room_type,
                description=random.choice(descriptions),
                enemy=enemy,
                is_cleared=is_cleared,
            )
        )

    return dungeon
