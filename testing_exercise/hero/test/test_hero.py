import unittest

from project.hero import Hero


class HeroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Angel', 10, 90.5, 50.5)

    def test_initialization_hero(self):
        self.assertEqual(self.hero.username, 'Angel')
        self.assertEqual(self.hero.level, 10)
        self.assertEqual(self.hero.health, 90.5)
        self.assertEqual(self.hero.damage, 50.5)

    def test_battle_expect_raise_error_if_both_heroes_have_same_username(self):
        with self.assertRaises(Exception) as ex:
            enemy = Hero('Angel', 5, 70, 15)
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_expect_raise_error_if_enemy_helth_is_less_than_zero_or_equal(self):
        with self.assertRaises(ValueError) as ex:
            enemy = Hero('Dimo', 5, 0, 15)
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Dimo. He needs to rest", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            enemy = Hero('Dimo', 5, -1, 15)
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Dimo. He needs to rest", str(ex.exception))

    def test_battle_expect_raise_error_if_hero_health_is_less_tan_zero_or_equal(self):
        with self.assertRaises(ValueError) as ex:
            self.hero.health = -1
            enemy = Hero('Dimo', 5, 11, 15)
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.hero.health = 0
            enemy = Hero('Dimo', 5, 11, 15)
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_expect_return_draw_if_health_of_both_of_heroes_is_equal_to_zero(self):
        enemy = Hero('Dimo', 10, 90.5, 50.5)
        self.assertEqual(self.hero.battle(enemy), 'Draw')

    def test_battle_expect_hero_increase_level_by_one_if_enemy_health_is_less_than_zero_or_equal_after_battle(self):
        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 9.5, 5.5)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.level, 11)

        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 50.5, 5.5)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.level, 11)

    def test_battle_expect_hero_increase_health_by_five_if_enemy_health_is_less_than_zero_or_equal_after_battle(self):
        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 9.5, 5.5)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.health, 40.5)

        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 50.5, 5.5)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.health, 40.5)

    def test_battle_expect_hero_increase_damage_by_five_if_enemy_health_is_less_than_zero_or_equal_after_battle(self):
        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 9.5, 5.5)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.damage, 55.5)

        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 50.5, 5.5)
        self.hero.battle(enemy)
        self.assertEqual(self.hero.damage, 55.5)

    def test_battle_expect_hero_return_correct_result_if_enemy_health_is_less_than_zero_or_equal_after_battle(self):
        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 9.5, 5.5)
        self.assertEqual("You win", self.hero.battle(enemy))

        self.hero = Hero('Angel', 10, 90.5, 50.5)
        enemy = Hero('Dimo', 10, 50.5, 5.5)
        self.assertEqual("You win", self.hero.battle(enemy))

    def test_battle_expect_enemy_hero_increase_level_by_one_if_hero_health_is_less_than_zero_or_equal_after_battle(
            self):
        self.hero = Hero('Angel', 10, 9.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 95.5)
        self.hero.battle(enemy)
        self.assertEqual(enemy.level, 11)

        self.hero = Hero('Angel', 10, 90.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 9.5)
        self.hero.battle(enemy)
        self.assertEqual(enemy.level, 11)

    def test_battle_expect_enemy_hero_increase_health_by_five_if_hero_health_is_less_than_zero_or_equal(self):
        self.hero = Hero('Angel', 10, 9.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 95.5)
        self.hero.battle(enemy)
        self.assertEqual(enemy.health, 45.5)

        self.hero = Hero('Angel', 10, 95.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 9.5)
        self.hero.battle(enemy)
        self.assertEqual(enemy.health, 45.5)

    def test_battle_expect_enemy_hero_increase_damage_by_five_if_hero_health_is_less_than_zero_or_equal(self):
        self.hero = Hero('Angel', 10, 9.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 95.5)
        self.hero.battle(enemy)
        self.assertEqual(enemy.damage, 100.5)

        self.hero = Hero('Angel', 10, 95.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 9.5)
        self.hero.battle(enemy)
        self.assertEqual(enemy.damage, 14.5)

    def test_battle_expect_enemy_hero_return_correct_result_if_hero_health_is_less_than_zero_or_equal_after_battle(
            self):
        self.hero = Hero('Angel', 10, 9.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 95.5)
        self.assertEqual(self.hero.battle(enemy), 'You lose')

        self.hero = Hero('Angel', 10, 95.5, 5.5)
        enemy = Hero('Dimo', 10, 95.5, 9.5)
        self.assertEqual(self.hero.battle(enemy), 'You lose')

    def test_hero_str_method_expect_return_correct_result(self):
        self.assertEqual("Hero Angel: 10 lvl\nHealth: 90.5\nDamage: 50.5\n", str(self.hero))


if __name__ == '__main__':
    unittest.main()
