from combat import AutoBattle
from entities import Enemy, Player


def test_autobattle_player_wins(player: Player, enemy: Enemy):
    enemy.hp = 1
    battle = AutoBattle(player=player, enemy=enemy)
    log = battle.fight()

    assert not enemy.is_alive()
    assert any("died" in entry for entry in log)


def test_enemy_wins_battle(player: Player, enemy: Enemy):
    player.hp = 1
    battle = AutoBattle(player=player, enemy=enemy)
    battle.fight()

    assert not player.is_alive()


def test_damage_zero_if_armor_stronger(player: Player, enemy: Enemy):
    enemy.armor.defense = 100
    battle = AutoBattle(player=player, enemy=enemy)
    battle.fight()

    assert any("for 0 damage" in entry for entry in battle.log)


def test_battle_log_not_empty(player, enemy):
    battle = AutoBattle(player=player, enemy=enemy)
    battle.fight()

    assert len(battle.log) > 0
