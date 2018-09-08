import unittest


def kangaroo(x1, v1, x2, v2):
    if x1 > x2 and v1 > v2:
        print("NO")
        return "NO"
    if x2 > x1 and v2 > v1:
        print("NO")
        return "NO"
    if x1 != x2 and v1 == v2:
        print("NO")
        return "NO"
    if x1 == x2:
        print("YES")
        return "YES"
    x1_smaller = x1 < x2
    current_x1 = x1
    current_x2 = x2
    hops = 0
    while current_x1 != current_x2:
        current_x1 += v1
        current_x2 += v2
        hops += 1
        new_x1_smaller = current_x1 < current_x2
        if current_x1 == current_x2:
            print("YES")
            return "YES"
        if x1_smaller != new_x1_smaller:
            print("NO")
            return "NO"
        x1_smaller = new_x1_smaller
    print("YES")
    return "YES"


class TestKangaroo(unittest.TestCase):
    def test_kangaroo(self):
        self.assertEqual(kangaroo(1, 10, 10, 1), "YES")

if __name__ == '__main__':
    print(unittest.main())