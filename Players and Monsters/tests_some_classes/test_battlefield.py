import unittest

from project.battle_field import BattleField

from project.player.beginner import Beginner

from project.player.advanced import Advanced

from project.card.magic_card import MagicCard

from project.card.trap_card import TrapCard


class testBattlefield(unittest.TestCase):
    def setUp(self):
        self.battlefield = BattleField()

    def test_if_attacker_is_dead_should_raise_error(self):
        attacker = Beginner("Simo")
        enemy = Advanced('Dimo')
        attacker.health = 0
        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(cm.exception), "Player is dead!")

    def test_if_enemy_is_dead_should_raise_error(self):
        attacker = Beginner("Simo")
        enemy = Advanced('Dimo')
        enemy.health = 0
        with self.assertRaises(ValueError) as cm:
            self.battlefield.fight(attacker, enemy)
        self.assertEqual(str(cm.exception), "Player is dead!")


    def test_enemy_should_increase_health_points(self):
        enemy = Beginner("Simo")
        attacker = Advanced('Dimo')
        card = MagicCard('Magic')
        enemy.card_repository.cards.append(card)
        self.battlefield.fight(attacker, enemy)
        self.assertEqual(enemy.health, 170)
        self.assertEqual(card.damage_points, 35)

    def test_attacker_should_increase_health_points(self):
        attacker = Beginner("Simo")
        enemy = Advanced('Dimo')
        card = MagicCard('Magic')
        attacker.card_repository.cards.append(card)
        self.battlefield.fight(attacker, enemy)
        self.assertEqual(attacker.health, 170)
        self.assertEqual(card.damage_points, 35)

    def test_fight_should_decrease_players_health(self):
        attacker = Advanced("Simo")
        enemy = Beginner('Dimo')
        attacker_card = MagicCard('Magic')
        enemy_card = TrapCard('Trap')
        attacker.card_repository.cards.append(attacker_card)
        enemy.card_repository.cards.append(enemy_card)
        self.battlefield.fight(attacker, enemy)
        self.assertEqual(enemy.health, 90)
        self.assertEqual(attacker.health, 180)
        

if __name__ == "__main__":
    unittest.main()
