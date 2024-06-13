import random


class Infantryman:
    def __init__(self, name):
        self.name = f"Пехотинец {name}"
        self.health = 100
        self.attack_power = 10
        self.defense_power = 15

    def attack(self, opponent):
        damage = self.attack_power - (0.4 * opponent.defense_power)
        opponent.health -= max(0, damage)
        self.health += 3
        return damage


class Archer:
    def __init__(self, name):
        self.name = f"Лучник {name}"
        self.health = 100
        self.attack_power = 15
        self.defense_power = 10

    def attack(self, opponent):
        damage = self.attack_power - (0.4 * opponent.defense_power)
        opponent.health -= max(0, damage)
        self.health += 3
        return damage


def create_characters():
    player_characters = []
    computer_characters = []

    player_name = input("Введите имя для вашего Пехотинца: ")
    player_characters.append(Infantryman(player_name))
    player_name = input("Введите имя для вашего Лучника: ")
    player_characters.append(Archer(player_name))

    computer_characters.append(Infantryman("Компьютерный Пехотинец"))
    computer_characters.append(Archer("Компьютерный Лучник"))

    return player_characters, computer_characters


def choose_character(characters, player_type="player"):
    print(f"{player_type.capitalize()} персонажи:")
    for i, char in enumerate(characters):
        print(f"{i + 1}. {char.name} (Здоровье: {char.health:.2f})")

    if player_type == "player":
        choice = int(input("Выберите номер персонажа для атаки: ")) - 1
    else:
        choice = random.randint(0, len(characters) - 1)

    return characters[choice]


def game_turn(attacker, defender):
    damage = attacker.attack(defender)
    print(f"{attacker.name} атаковал {defender.name} и нанес урон {damage:.2f}.")
    print(f"Здоровье {defender.name}: {defender.health:.2f}")
    if defender.health <= 0:
        print(f"{defender.name} был побежден!")
        return True
    return False


def main():
    player_characters, computer_characters = create_characters()
    turn = random.choice(["player", "computer"])
    print(f"{turn.capitalize()} ходит первым!")

    last_attacker = None

    while player_characters and computer_characters:
        if turn == "player":
            if last_attacker and last_attacker in player_characters:
                attacker = last_attacker
            else:
                attacker = choose_character(player_characters, "player")
            defender = last_attacker if last_attacker else choose_character(computer_characters, "computer")

            if game_turn(attacker, defender):
                computer_characters.remove(defender)
            turn = "computer"
        else:
            if last_attacker and last_attacker in computer_characters:
                attacker = last_attacker
            else:
                attacker = choose_character(computer_characters, "computer")
            defender = last_attacker if last_attacker else choose_character(player_characters, "player")

            if game_turn(attacker, defender):
                player_characters.remove(defender)
            turn = "player"

        last_attacker = attacker

    if player_characters:
        print("Поздравляем! Вы победили!")
    else:
        print("Компьютер победил!")


if __name__ == "__main__":
    main()
