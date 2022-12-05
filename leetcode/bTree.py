# -*- coding:utf-8 -*-
from operator import le
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinTree:
    def __init__(self):
        self.root = None
        self.ls = []

    def add(self, data):
        node = TreeNode(data)
        if self.root is None:
            self.root = node
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0]
            if rootNode.left is None:
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right is None:
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0)


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if node is None:
                return 0
            val = (val << 1) | node.val
            if node.left is None and node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)

        return dfs(root, 0)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

    def numColor(self, root: TreeNode) -> int:
        s = set()

        def getColor(root: TreeNode):
            if root is None:
                return

            getColor(root.right)
            getColor(root.left)
            s.add(root.val)

        getColor(root)
        return len(s)

    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # 剑指 Offer 27. 二叉树的镜像
        if not root:
            return root

        right = self.mirrorTree(root.right)
        left = self.mirrorTree(root.left)
        root.left, root.right = right, left
        return root

    def maxDepth(self, root: TreeNode) -> int:
        # 剑指 Offer 55 - I. 二叉树的深度
        """深度优先搜索
        """
        # if root is None:
        #     return 0
        # else:
        #     left_height = self.maxDepth(root.left)
        #     right_height = self.maxDepth(root.right)
        #     return max(left_height, right_height) + 1
        """广度优先搜索
        """
        if root is None:
            return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res

    def iterationDFSBTree(self, root):
        # 迭代+栈实现二叉树 深度优先搜索 遍历
        if root == None:
            return
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            print(cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        # 226. 翻转二叉树
        if not root:
            return root
        left_node = self.invertTree(root.left)
        right_node = self.invertTree(root.right)
        root.left, root.right = right_node, left_node
        return root

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # 617. 合并二叉树, 深度优先搜索实现
        if not root1:
            return root2
        if not root2:
            return root1

        res = TreeNode(root1.val + root2.val)
        res.left = self.mergeTrees(root1.left, root2.left)
        res.right = self.mergeTrees(root1.right, root2.right)
        return res


if __name__ == '__main__':
    b_tree = BinTree()
    s = Solution()
    for i in [10, 5, 15, 3, 7, 0, 18]:
        b_tree.add(i)

    # print(b_tree.root.val)
    print(s.iterationBTree(b_tree.root))
