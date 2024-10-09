import random


class Warrior:
    def __init__(self):
        self.first_warrior_hp = 100
        self.first_warrior_endurance = 100
        self.first_warrior_armor = 100
        self.first_warrior_attack_bonus = 10
        self.second_warrior_hp = 100
        self.second_warrior_endurance = 100
        self.second_warrior_armor = 100
        self.second_warrior_attack_bonus = 10
        self.result_first_warrior = 'alive'
        self.result_second_warrior = 'alive'
        self.round = 0
        self.first_warrior_checker_hp = 0
        self.first_warrior_checker_arm = 0
        self.first_warrior_checker_end = 0
        self.second_warrior_checker_hp = 0
        self.second_warrior_checker_arm = 0
        self.second_warrior_checker_end = 0

    def first_warrior(self, action_first_warrior, action_second_warrior):
        self.first_warrior_checker_hp = 0
        self.first_warrior_checker_arm = 0
        self.first_warrior_checker_end = 0
        if action_first_warrior == 'attack':
            if self.first_warrior_endurance > 0:
                self.first_warrior_checker_end = -10
                self.first_warrior_endurance -= 10
            else:
                self.first_warrior_attack_bonus = 0
            if action_second_warrior == 'defence':
                if self.second_warrior_armor > 0:
                    self.first_warrior_checker_arm = random.randint(0, 10)
                    self.first_warrior_checker_hp = random.randint(0, self.first_warrior_attack_bonus
                                                                   + 10)
                    self.second_warrior_armor -= self.first_warrior_checker_arm
                    self.second_warrior_hp -= self.first_warrior_checker_hp
                else:
                    self.first_warrior_checker_hp = random.randint(self.first_warrior_attack_bonus, 20
                                                                   + self.first_warrior_attack_bonus)
                    self.second_warrior_hp -= self.first_warrior_checker_hp
            else:
                self.first_warrior_checker_hp = random.randint(self.first_warrior_attack_bonus, 20
                                                               + self.first_warrior_attack_bonus)
                self.second_warrior_hp -= self.first_warrior_checker_hp

    def second_warrior(self, action_first_warrior, action_second_warrior):
        self.second_warrior_checker_hp = 0
        self.second_warrior_checker_arm = 0
        self.second_warrior_checker_end = 0

        if action_second_warrior == 'attack':
            if self.second_warrior_endurance > 0:
                self.second_warrior_checker_end = -10
                self.second_warrior_endurance -= 10
            else:
                self.second_warrior_attack_bonus = 0
            if action_first_warrior == 'defence':
                if self.first_warrior_armor > 0:
                    self.second_warrior_checker_arm = random.randint(0, 10)
                    self.second_warrior_checker_hp = random.randint(0, self.second_warrior_attack_bonus + 10)
                    self.first_warrior_armor -= self.second_warrior_checker_arm
                    self.first_warrior_hp -= self.second_warrior_checker_hp
                else:
                    self.second_warrior_checker_hp = random.randint(self.second_warrior_attack_bonus, 20
                                                                    + self.second_warrior_attack_bonus)
                    self.first_warrior_hp -= self.second_warrior_checker_hp
            else:
                self.second_warrior_checker_hp = random.randint(self.second_warrior_attack_bonus, 20
                                                                + self.second_warrior_attack_bonus)
                self.first_warrior_hp -= self.second_warrior_checker_hp

        if self.first_warrior_hp < 10:
            self.first_warrior_hp = 10
        if self.first_warrior_hp < 10:
            self.first_warrior_hp = 10
        if self.second_warrior_endurance < 0:
            self.second_warrior_endurance = 0
        if self.second_warrior_armor < 0:
            self.second_warrior_armor = 0
        if self.first_warrior_armor < 0:
            self.first_warrior_armor = 0
        if self.first_warrior_endurance < 0:
            self.first_warrior_endurance = 0

        self.log_round(action_first_warrior, action_second_warrior)

        if self.first_warrior_hp <= 10:
            self.result_first_warrior = 'defeat'

        if self.second_warrior_hp <= 10:
            self.result_second_warrior = 'defeat'

        if self.first_warrior_hp <= 10 or self.second_warrior_hp <= 10:
            self.final()

        else:
            self.start_battle()

    def start_battle(self):
        chose_first_warrior = random.randint(1, 3)
        chose_second_warrior = random.randint(1, 3)
        if chose_first_warrior == 1:

            action_first_warrior = 'attack'

        else:
            action_first_warrior = 'defence'

        if chose_second_warrior == 1:
            action_second_warrior = 'attack'

        else:
            action_second_warrior = 'defence'

        self.round += 1
        self.first_warrior(action_first_warrior, action_second_warrior)
        self.second_warrior(action_first_warrior, action_second_warrior)

    def log_round(self, action_first_warrior, action_second_warrior):
        print("Раунд №", self.round)
        print('1: ', action_first_warrior, '; 2:', action_second_warrior, sep='')
        print("Health_first_warrior -= ", self.second_warrior_checker_hp,
              " Health_second_warrior -= ", self.first_warrior_checker_hp, sep='')
        print("Health_first_warrior = ", self.first_warrior_hp,
              " Health_second_warrior = ", self.second_warrior_hp, sep='')
        print("Armor_first_warrior -= ", self.second_warrior_checker_arm,
              " Armor_second_warrior -= ", self.first_warrior_checker_arm, sep='')
        print("Armor_first_warrior = ", self.first_warrior_armor,
              " Armor_second_warrior = ", self.second_warrior_armor, sep='')
        if self.first_warrior_checker_end == -10:
            print("Endurance_first_warrior -= 10", end=' ')
        if self.second_warrior_checker_end == -10:
            print("Endurance_second_warrior -= 10")
        print("Endurance_first_warrior = ", self.first_warrior_endurance,
              " Endurance_second_warrior = ", self.second_warrior_endurance, sep='')
        print("Конец раунда \n ----------------------")

    def final(self):
        check = 0
        if self.result_first_warrior == 'defeat':
            print("Первый боец доблестно сражался?"
                  "Сохранить им жизнь? *Ответьте Да/Нет, обратитесь к методу answear*")
        elif self.result_second_warrior == 'defeat':
            check = 1
            print("Второй боец доблестно сражался?"
                  "Сохранить им жизнь? *Ответьте Да/Нет, обратитесь к методу answear*")
        else:
            check = 2
            print("Бойцы доблестно сражался?"
                  "Сохранить им жизнь? *Ответьте Да/Нет, обратитесь к методу answear*")
        final_answear = str(input())
        if final_answear == 'Нет':
            if check == 0:
                print("Второй боец добивает первого бойца")
            elif check == 1:
                print("Первый боец добивает второго бойца")
            else:
                print("Львы съедают бойцов")
        else:
            print("Бойцы заслужили право стать свободными!")


battle = Warrior()
battle.start_battle()
