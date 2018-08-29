import collections
import unittest

class ChangeMaker:
    def __init__(self, target, coins):
        self.target = target
        self.coins = coins
        self.num_coins = None
        self.coin_vals = None
        self.get_change()

    def get_change(self):
        num_coins = [0 for _ in range(self.target + 1)]
        coin_vals = [0 for _ in range(self.target + 1)]
        coins = self.coins
        coins.sort()
        for target in range(self.target + 1):
            for coin in coins:
                if target - coin < 0:
                    break
                num_coins[target] = num_coins[target - coin] + 1
                coin_vals[target] = coin
        self.num_coins = num_coins
        self.coin_vals = coin_vals


class TestChangeMaker(unittest.TestCase):
    def test_get_change(self):
        t = 10
        coins = [1, 2, 3, 5, 6]
        cm = ChangeMaker(t, coins)
        print(str([i for i in range(cm.target + 1)]))
        print(str(cm.num_coins))
        print(str(cm.coin_vals))
        # self.assertEqual(4, cm.get_change())


if __name__ == '__main__':
    unittest.main()