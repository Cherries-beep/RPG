import random

from entities import Enemy, Player


class AutoBattle:
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy
        self.log: list[str] = []

    def _hit(self, attacker, defender) -> None:
        roll = random.randint(0, 100)

        if attacker.weapon.hit_chance >= roll:
            damage = max(attacker.weapon.damage - defender.armor.defense, 0)
            defender.hp -= damage
            self.log.append(f"{attacker.name} hits {defender.name} for {damage} damage")
        else:
            self.log.append(f"{attacker.name} misses {defender.name}")

    def fight(self) -> list[str]:
        while self.player.is_alive() and self.enemy.is_alive():
            self._hit(self.player, self.enemy)

            if not self.enemy.is_alive():
                self.log.append(f"{self.enemy.name} died")
                break

            self._hit(self.enemy, self.player)

            if not self.player.is_alive():
                self.log.append(f"{self.player.name} died")

        return self.log
