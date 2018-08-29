import unittest


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

    def solve(self):
        pass


class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        left_height = -1 if root.left is None else self.getHeight(root.left)
        right_height = -1 if root.right is None else self.getHeight(root.right)

        return max(left_height, right_height) + 1



class TestMyBST(unittest.TestCase):
    def test_get_height(self):
        my_tree = Solution()
        root = None
        for i in range(6)[1::]:
            data = int((i * 2) % 5)
            root = my_tree.insert(root, data)

        self.assertEqual(2, my_tree.getHeight(root))


if __name__ == '__main__':
    unittest.main()
