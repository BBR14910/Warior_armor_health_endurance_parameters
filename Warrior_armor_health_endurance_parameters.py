import random


class Warrior:
    def __init__(self):
        self.warrior_hp = 200
        self.warrior_endurance = 100
        self.warrior_armor = 100
        self.warrior_attack_bonus = 10

    def battle(self, first_warrior, second_warrior):
        """
        Принимает на вход два воина. Рассчитывает кто из них победит в битве
        """
        round = 0
        while first_warrior.warrior_hp > 10 and second_warrior.warrior_hp > 10:
            action_first_warrior = "attack"
            action_second_warrior = "attack"
            second_warrior_checker_hp = 0
            second_warrior_checker_arm = 0
            second_warrior_checker_end = 0
            first_warrior_checker_hp = 0
            first_warrior_checker_arm = 0
            first_warrior_checker_end = 0
            first_warrior_attack_bonus = 0
            second_warrior_attack_bonus = 0
            chose_first_warrior = random.randint(1, 3)
            chose_second_warrior = random.randint(1, 3)
            round += 1

            if chose_first_warrior == 2:
                action_first_warrior = "defence"
            if chose_second_warrior == 2:
                action_second_warrior = "defence"

            if action_second_warrior == "attack":
                if second_warrior.warrior_endurance > 0:
                    second_warrior_checker_end = -10
                    second_warrior.warrior_endurance -= 10
                else:
                    second_warrior_attack_bonus = 0
                if action_first_warrior == "defence":
                    if first_warrior.warrior_armor > 0:
                        second_warrior_checker_arm = random.randint(0, 10)
                        second_warrior_checker_hp = random.randint(
                            0, second_warrior_attack_bonus + 10
                        )
                        first_warrior.warrior_armor -= second_warrior_checker_arm
                        first_warrior.warrior_hp -= second_warrior_checker_hp
                    else:
                        second_warrior_checker_hp = random.randint(
                            second_warrior_attack_bonus,
                            20 + second_warrior_attack_bonus,
                        )
                        first_warrior.warrior_hp -= second_warrior_checker_hp
                else:
                    second_warrior_checker_hp = random.randint(
                        second_warrior_attack_bonus, 20 + second_warrior_attack_bonus
                    )
                    first_warrior.warrior_hp -= second_warrior_checker_hp

            if action_first_warrior == "attack":
                if first_warrior.warrior_endurance > 0:
                    first_warrior_checker_end = -10
                    first_warrior.warrior_endurance -= 10
                else:
                    first_warrior_attack_bonus = 0
                if action_second_warrior == "defence":
                    if second_warrior.warrior_armor > 0:
                        first_warrior_checker_arm = random.randint(0, 10)
                        first_warrior_checker_hp = random.randint(
                            0, first_warrior_attack_bonus + 10
                        )
                        second_warrior.warrior_armor -= first_warrior_checker_arm
                        second_warrior.warrior_hp -= first_warrior_checker_hp
                    else:
                        first_warrior_checker_hp = random.randint(
                            first_warrior_attack_bonus, 20 + first_warrior_attack_bonus
                        )
                        second_warrior.warrior_hp -= first_warrior_checker_hp
                else:
                    first_warrior_checker_hp = random.randint(
                        first_warrior_attack_bonus, 20 + first_warrior_attack_bonus
                    )
                    second_warrior.warrior_hp -= first_warrior_checker_hp

            if first_warrior.warrior_hp < 10:
                first_warrior.warrior_hp = 10
            if first_warrior.warrior_hp < 10:
                first_warrior.warrior_hp = 10
            if second_warrior.warrior_endurance < 0:
                second_warrior.warrior_endurance = 0
            if second_warrior.warrior_armor < 0:
                second_warrior.warrior_armor = 0
            if first_warrior.warrior_armor < 0:
                first_warrior.warrior_armor = 0
            if first_warrior.warrior_endurance < 0:
                first_warrior.warrior_endurance = 0

            print("Раунд №", round)
            print("1: ", action_first_warrior, "; 2:", action_second_warrior, sep="")
            print(
                "Health_first_warrior -= ",
                second_warrior_checker_hp,
                " Health_second_warrior -= ",
                first_warrior_checker_hp,
                sep="",
            )
            print(
                "Health_first_warrior = ",
                first_warrior.warrior_hp,
                " Health_second_warrior = ",
                second_warrior.warrior_hp,
                sep="",
            )
            print(
                "Armor_first_warrior -= ",
                second_warrior_checker_arm,
                " Armor_second_warrior -= ",
                first_warrior_checker_arm,
                sep="",
            )
            print(
                "Armor_first_warrior = ",
                first_warrior.warrior_armor,
                " Armor_second_warrior = ",
                second_warrior.warrior_armor,
                sep="",
            )
            if first_warrior_checker_end == -10:
                print("Endurance_first_warrior -= 10", end=" ")
            if second_warrior_checker_end == -10:
                print("Endurance_second_warrior -= 10")
            print(
                "Endurance_first_warrior = ",
                first_warrior.warrior_endurance,
                " Endurance_second_warrior = ",
                second_warrior.warrior_endurance,
                sep="",
            )
            print("Конец раунда \n ----------------------")

        check = 0
        if first_warrior.warrior_hp <= 10 and second_warrior.warrior_hp <= 10:
            print(
                "Бойцы доблестно сражался?"
                "Сохранить им жизнь? *Ответьте Да/Нет, обратитесь к методу answear*"
            )
        elif first_warrior.warrior_hp <= 10:
            check = 1
            print(
                "Второй боец доблестно сражался?"
                "Сохранить им жизнь? *Ответьте Да/Нет, обратитесь к методу answear*"
            )
        else:
            check = 2
            print(
                "Первый боец доблестно сражался?"
                "Сохранить им жизнь? *Ответьте Да/Нет, обратитесь к методу answear*"
            )
        final_answear = str(input())
        if final_answear == "Нет":
            if check == 2:
                print("Второй боец добивает первого бойца")
            elif check == 1:
                print("Первый боец добивает второго бойца")
            else:
                print("Львы съедают бойцов")
        else:
            print("Бойцы заслужили право стать свободными!")


first_warrior = Warrior()
second_warrior = Warrior()
first_warrior.battle(first_warrior, second_warrior)
