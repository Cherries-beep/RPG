"""
Контроллер игрового процесса. Отвечает за игровой цикл и действия игрока.
"""

from typing import List

from entities import Player, Room


class GameController:
    """Управлять игровым процессом"""

    def __init__(self, player: Player, dungeon: List[Room]) -> None:
        """
        Инициализировать контроллер игры.

        Args:
            player: Экземпляр игрока.
            dungeon: Список комнат подземелья.
        """
        self.player = player
        self.dungeon = dungeon
        self.current_index = self._find_start()

    def _find_start(self) -> int:
        """Найти стартовую комнату.

        Returns:
            int: Индекс стартовой комнаты.
        """
        for index, room in enumerate(self.dungeon):
            if room.room_type == "St":
                return index
        raise ValueError("Start room not found")

    def run(self) -> None:
        """Запустить основной игровой цикл."""
        while True:
            room = self.dungeon[self.current_index]
            print("\n------------------------")
            print(f"You are in room: {room.room_type}")
            print(room.description)

            if room.enemy and room.enemy.is_alive():
                print(f"Enemy here: {room.enemy.name} (HP: {room.enemy.hp})")

            actions = self._get_available_actions(room)
            print("\nAvailable actions:")

            for i, action in enumerate(actions, start=1):
                print(f"{i}. {action}")

            choice = self._get_user_choice(len(actions))
            action = actions[choice - 1]

            if action == "go_forward":
                self.current_index += 1

            elif action == "go_back":
                self.current_index -= 1

            elif action == "attack":
                self._attack(room)
                print("Enemy defeated!")

            elif action == "exit":
                print("You have left the dungeon.")
                break

    def _get_available_actions(self, room: Room) -> List[str]:
        """Получить список доступных действий

        Args:
            room: Текущая комната.

        Returns:
            List: Список действий.
        """
        if room.has_enemy():
            return ["attack"]

        actions: List[str] = []

        if room.room_type != "Ex" and self.current_index < len(self.dungeon) - 1:
            actions.append("go_forward")

        if room.room_type != "St" and self.current_index > 0:
            actions.append("go_back")

        if room.room_type == "Ex":
            actions.append("exit")

        return actions

    def _attack(self, room: Room) -> None:
        """Убить противника в комнате.

        Args:
            room: Комната с противником.
        """
        if room.enemy:
            room.enemy.hp = 0

    def _get_user_choice(self, max_choice: int) -> int:
        """Получить корректный ввод пользователя."""
        while True:

            try:
                choice = int(input())

                if 1 <= choice <= max_choice:
                    return choice

            except ValueError:
                pass