# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        larg_diam = [0]

        def height(root):
            if root is None:
                return 0
        
            l_height = height(root.left)
            r_height = height(root.right)
            larg_diam[0] = max(larg_diam[0], l_height + r_height)

            return 1 + max(r_height, l_height)

        height(root)
        return larg_diam[0]
        
