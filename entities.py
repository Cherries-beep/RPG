"""Сущности игры. Содержит структуры данных для игрока, противников, комнат и экипировки."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Weapon:
    """Оружие персонажа"""

    name: str
    damage: int
    hit_chance: int


@dataclass
class Armor:
    """Броня персонажа"""

    name: str
    defense: int


@dataclass
class Enemy:
    """Противник"""

    name: str
    hp: int
    description: str
    death_description: str
    weapon: Weapon
    armor: Armor

    def is_alive(self) -> bool:
        """
        Проверить жив ли противник

        Returns:
            bool: True если противник жив, иначе False.
        """
        return self.hp > 0


@dataclass
class Player:
    """Игрок"""

    name: str
    hp: int
    description: str
    weapon: Weapon
    armor: Armor

    def is_alive(self) -> bool:
        """
        Проверить жив ли игрок

        Returns:
            bool: True если игрок жив, иначе False.
        """
        return self.hp > 0


@dataclass
class Room:
    """Комната подземелья"""

    room_type: str
    description: str
    is_cleared: bool = False
    enemy: Optional[Enemy] = None

    def has_enemy(self) -> bool:
        """
        Проверить наличие живого противника в комнате

        Returns:
            bool: True если в комнате есть живой враг
        """
        return self.enemy is not None and self.enemy.is_alive()

    def clear_if_enemy_dead(self) -> None:
        """Очистить комнату от противника, если он погиб"""
        if self.enemy and not self.enemy.is_alive():
            self.enemy = None
            self.is_cleared = True
