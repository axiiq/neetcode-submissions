# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = root
        queue = [root]

        while queue:
            tmp = queue.pop(0)

            # obě jsou menší
            if p.val <= tmp.val and q.val <= tmp.val:
                lca = tmp.left
                queue.append(tmp.left)

            # obě jsou větší
            if tmp.val <= p.val and tmp.val <= q.val:
                lca = tmp.right
                queue.append(tmp.right)

            # q je větší nebo p je větší
            if p.val <= tmp.val <= q.val or q.val <= tmp.val <= p.val:
                return tmp
