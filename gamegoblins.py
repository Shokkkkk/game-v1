import random


class Unit:
    name: str
    desc: str
    health: int
    damage: int


class Character(Unit):

    @property  # описываем как определить смерть
    def is_death(self) -> bool:
        return self.health <= 0

    def get_damage(self, attacker: Unit) -> None:
        print(f'{self.name} get damage {attacker.damage} points.')
        self.health = self.health - attacker.damage


class Golum(Character):
    name = "Golum"
    desc = "A foul creature"
    health = 5
    damage = 4


class Elf(Character):
    name = "Elf"
    desc = "A heavenly creature"
    health = 7
    damage = 6


class Ork(Character):
    name = "Ork"
    desc = "An underwater creature "
    health = 8
    damage = 2


class Gnome(Character):
    name = "Gnome"
    desc = "A mountain creature"
    health = 8
    damage = 2


if __name__ == '__main__':

    arena = [Golum(), Elf(), Ork(), Gnome()]

    fighter_one = random.choice(arena)
    print(f'{fighter_one.name} is {fighter_one.desc}')
    fighter_two = random.choice(arena)
    print(f'{fighter_two.name} is {fighter_two.desc}')

    while True:

        if fighter_two == fighter_one:
            print(f"{fighter_one.name} HARAKIRI!!")
            break

        fighter_one.get_damage(fighter_two)
        fighter_two.get_damage(fighter_one)

        if fighter_one.is_death:
            print(f'{fighter_one.name} pogib!')
            break

        if fighter_two.is_death:
            print(f'{fighter_two.name} sdoh!')
            break
